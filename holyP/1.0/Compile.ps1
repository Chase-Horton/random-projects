Set-Location $PSScriptRoot
$file = Read-Host -Prompt 'Input Filename'
$keep = Read-Host -Prompt 'Keep C File'
$fileC = $file + '.c'
$fileIn = $file +'.holyP'
$fileOut = $file + '.exe'
python holyP.py $fileIn $fileC
gcc $fileC -o $fileOut
Read-Host -Prompt "Press Enter to exit"

If(( $keep -eq "1")){
    Remove-Item $fileC
}

