<# 
    Task 1
    Storyline: In this task the powershell.exe was copied over and placed in the user directory. 
    Then the file was renamed, and in the console will print if the file was copied over successfully 
#>

# the powershell file 
$file = "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" 

# the user directory 
$user_dir = "C:\Users\ecraw\Desktop\"

# Copy the file over 
Copy-Item $file -Destination $user_dir

# create a random number 
$rand = Get-Random -Minimum 1000 -Maximum 9876

# the the location of wher the powershell file is currently stored in 
$fileLocation = $user_dir + "powershell.exe"

# new name to call the file
$newName = "EnNoB-" + $rand + ".exe"

# create a variable to store the new renamed file 
$newFile = $user_dir + $newName

# Rename the powershell file
Rename-Item -Path $fileLocation -NewName $newName

# check that the file copied successfully, if not print an error out

if (Test-Path $newFile)
{
    Write-Host -BackgroundColor "Green" -ForegroundColor "white" "file was created!"
} 
else
{
    Write-Host -BackgroundColor "Red" -ForegroundColor "white" "file was not created!"
}

<# 
    Task 2
    Storyline: In this task a READme.READ file was created which has a message inside and is saved to the Desktop
#>

# message to send 
$msg = "If you want your files restored, please contact me at emily.crawford@mymail.champlain.edu. I look forward to doing business with you."

# Create a README.READ file and save it to the desktop
$ReadMEfile = "C:\Users\ecraw\Desktop\READme.READ"
echo $msg | out-file -FilePath $ReadMEfile


# Check if the READme file was created, and print if the results  
if (Test-Path $ReadMEfile)
{
    Write-Host -BackgroundColor "Green" -ForegroundColor "white" "Readme file was created!"
} 
else
{
    Write-Host -BackgroundColor "Red" -ForegroundColor "white" "Readme file was not created!"
}

<# 
    Week 12 task 4
    Storyline: In this task it creates a file called update.bat, and writes the file out 
#>

# create the contents update.bat file,  
$writeUpdateFile = @'
# delete a file called step2.ps1
del "C:\Users\ecraw\Desktop\step2.ps1"
'@

# write to a file
$writeUpdateFile | out-file -FilePath ".\update.bat"
