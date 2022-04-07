# Login to a remote SSH server 
 New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential 'emily.crawford@cyber.local') -Port '2222'


while ($True)    
{
    # Add a prompt to run commands 
    $the_cmd = read-host -Prompt "Please enter a command"

    # Run command on a remote SSH server
    (Invoke-SSHCommand -index 0 $the_cmd).Output
}

# Upload a file to the remote system
Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential 'emily.crawford@cyber.local') -Path 'C:\Users\ecraw\Desktop\SYS320-visual-studio-repo\SYS320-Automation-And-Scipting\SYS320-SP22\Week11\class\test.txt' -Destination '/home/emily.crawford/' -Port '2222'


