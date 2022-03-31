# Send an email using Powershell

# array to hold email list to spam
$toSend = @('emily.crawford@mymail.champlain.edu', 'crawford@mymail.champlain.edu', 'emily@mymail.champlain.edu')

# Message body 
$msg = "Hello"

while ($true) 
{
    foreach ($email in $toSend) 
    {
        # Send the email 
        write-host "Send-MailMessage - from 'emily.crawford@mymail.champlain.edu' -To $email -Subject 'Tisk Tisk'`
        -Body $msg -SmtpServer X.X.X.X"

        # Pause for one second
        # start-sleep 1
    }
}