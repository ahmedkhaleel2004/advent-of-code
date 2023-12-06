$DayFolder = Get-Location
$scriptPath = Join-Path -Path $DayFolder -ChildPath "main.py"
$inputPath = Join-Path -Path $DayFolder -ChildPath "input.txt"

if ((Test-Path $scriptPath) -and (Test-Path $inputPath)) {
    Get-Content $inputPath | python $scriptPath
} else {
    Write-Host "Script or input file not found in $DayFolder."
}
