# Quick script to check Python environment in Cursor terminal
Write-Host "=== Python Environment Check ===" -ForegroundColor Cyan
Write-Host ""

Write-Host "1. Python version:" -ForegroundColor Yellow
python --version
Write-Host ""

Write-Host "2. Python path:" -ForegroundColor Yellow
(Get-Command python).Source
Write-Host ""

Write-Host "3. Pip version:" -ForegroundColor Yellow
python -m pip --version
Write-Host ""

Write-Host "4. Current directory:" -ForegroundColor Yellow
Get-Location
Write-Host ""

Write-Host "5. Python executable:" -ForegroundColor Yellow
python -c "import sys; print(sys.executable)"
Write-Host ""

Write-Host "=== To fix PATH in Cursor terminal ===" -ForegroundColor Green
Write-Host "Run this command (replace with your actual Python path if different):" -ForegroundColor Yellow
Write-Host '$env:Path = "C:\Python313;C:\Python313\Scripts;" + $env:Path' -ForegroundColor White
