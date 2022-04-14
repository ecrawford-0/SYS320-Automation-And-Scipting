# Create commandline parameters to copy a file and place it into an evidence directory

param(

[Parameter(Mandatory = $true)]
[int]$reportNo,

[Parameter(Mandatory = $true)]
[String]$filePath

)

# Create a directory with the report number
$reportDir = "rpt$reportNo"

# creating a new directory
mkdir $reportDir

# copy the file into the new directory
copy-item $filePath $reportDir