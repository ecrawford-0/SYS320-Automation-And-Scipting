# Get a list of running processes 
# Get-Process

# Get list of members
# Get-Process | Get-Member 

# Get a list of processes and extract name, id, and path
# Get-Process | Select-Object ProcessName, id, Path  

# Save the Output to a CSV File 
# Get-Process | Select-Object ProcessName, id, Path | Export-Csv -Path `
# C:\Users\ecraw\Desktop\processes.csv

# System Services and properties
# Get-Service | get-member
# Get-Service | select-object Status, Name, DisplayName, BinaryPathName | export-csv -Path `
# $outputName



# Get a list of running services 
$outputName = "C:\Users\ecraw\Desktop\runningServices.csv"
Get-Service | Where-Object { $_.Status -eq "Running" } |  export-csv -Path `
$outputName


# Check to see if the file exists
if (Test-Path $outputName)
{
    Write-Host -BackgroundColor "Green" -ForegroundColor "white" "Services file was created!"
} 
else
{
    Write-Host -BackgroundColor "Red" -ForegroundColor "white" "Services file was not created!"
}