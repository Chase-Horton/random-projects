Set-Location $PSScriptRoot
$file = Read-Host -Prompt 'Input holyP Filename (file extension is not necessary)'
$fileIn = $file +'.holyP'
python runLexer.py $fileIn
python runParser.py $fileIn

Read-Host -Prompt "Press Enter to exit"

