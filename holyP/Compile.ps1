Set-Location $PSScriptRoot
$file = Read-Host -Prompt 'Input holyP Filename (file extension is not necessary)'
$keep = Read-Host -Prompt 'Keep C File (n)'
$fileC = $file + '.c'
$fileIn = $file + '.holyP'
$fileOut = $file + '.exe'
python holyP.py $fileIn $fileC
gcc $fileC -o $fileOut
Read-Host -Prompt "Press Enter to exit"

If(( $keep -eq "n")){
    Remove-Item $fileC
}

