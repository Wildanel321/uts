# PowerShell verification script for Dart Project Lab
$ErrorActionPreference = "Stop"
Write-Host "=====================================================" -ForegroundColor Cyan
Write-Host "   DART PROJECT LAB — POWERSHELL VERIFICATION SCRIPT " -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan

$dartCmd = Get-Command dart -ErrorAction SilentlyContinue
if (-not $dartCmd) {
    Write-Error "Dart SDK is not found in PATH. Please install Dart SDK first."
    exit 1
}

Write-Host "Dart SDK Version: " -NoNewline
& dart --version

Write-Host "`nLaunching Dart Verification Runner..." -ForegroundColor Yellow
& dart run tool/verify_all.dart
if ($LASTEXITCODE -ne 0) {
    Write-Host "`nVerification failed with exit code $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}
Write-Host "`nAll verifications succeeded!" -ForegroundColor Green
