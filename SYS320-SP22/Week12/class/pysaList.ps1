# List the files in a directory and
# List all the files and print the full path
# Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path .\Documents | Select FullName

Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path .\Documents | export-csv `
-Path files.csv

# import the csv file
$fileList= import-csv -Path .\files.csv #-header FullName


# Loop through the results
foreach ($f in $fileList)
{
    Get-ChildItem $f.FullName
}