param (
    [string]$CommitMessage
)

if ([string]::IsNullOrWhiteSpace($CommitMessage)) {
    Write-Host "[Error] Please provide a commit message." -ForegroundColor Red
    Write-Host "Example: .\upload_version.ps1 'v1.2.0 Add new feature'"
    exit 1
}

Write-Host "[1/4] Cleaning old build..." -ForegroundColor Cyan
if (Test-Path "dist\MeowHub.exe") { Remove-Item -Force "dist\MeowHub.exe" }

Write-Host "[2/4] Building new EXE..." -ForegroundColor Cyan
$pyinstaller = ".venv\Scripts\pyinstaller.exe"
if (-Not (Test-Path $pyinstaller)) {
    $pyinstaller = "pyinstaller"
}
& $pyinstaller MeowHub-OneFile.spec --noconfirm

if (-Not (Test-Path "dist\MeowHub.exe")) {
    Write-Host "[Error] Build failed, dist\MeowHub.exe not found!" -ForegroundColor Red
    exit 1
}

Write-Host "[3/4] Copying to releases folder..." -ForegroundColor Cyan
if (-Not (Test-Path "releases")) { New-Item -ItemType Directory -Path "releases" | Out-Null }
Copy-Item "dist\MeowHub.exe" -Destination "releases\MeowHub_Latest.exe" -Force

Write-Host "[4/4] Committing and pushing to GitHub..." -ForegroundColor Cyan
git add .
git commit -m $CommitMessage
git push

Write-Host "==============================================" -ForegroundColor Green
Write-Host " SUCCESS! Log and new EXE uploaded." -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Green
