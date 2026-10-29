# Automated GitHub Push Script for Smart Campus Complaint System
param(
    [string]$RepoName = "smart-campus-complaint-system",
    [string]$GitHubUsername = "rajbhaskar0427"
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Push Smart Campus Complaint System to GitHub" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan

$git = "C:\Users\Hello\.gemini\antigravity\scratch\mingit\cmd\git.exe"
$projDir = "C:\Users\Hello\.gemini\antigravity\scratch\SmartCampusComplaintSystem"
Set-Location $projDir

Write-Host "Target: https://github.com/$GitHubUsername/$RepoName.git" -ForegroundColor Yellow

# Check if remote already exists
$existingRemote = & $git remote get-url origin 2>$null
if ($null -eq $existingRemote) {
    & $git remote add origin "https://github.com/$GitHubUsername/$RepoName.git"
    Write-Host "[✓] Added remote origin: https://github.com/$GitHubUsername/$RepoName.git" -ForegroundColor Green
} else {
    Write-Host "[✓] Remote origin already set to: $existingRemote" -ForegroundColor Green
}

Write-Host "`nAttempting to push main branch to GitHub..." -ForegroundColor Cyan
& $git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[🎉 SUCCESS] Project pushed successfully to https://github.com/$GitHubUsername/$RepoName" -ForegroundColor Green
} else {
    Write-Host "`n[ℹ️ Note] If authentication is required:" -ForegroundColor Yellow
    Write-Host "1. Create the repository on GitHub if not already created: https://github.com/new (Name: $RepoName)" -ForegroundColor White
    Write-Host "2. Generate a Personal Access Token (PAT) with 'repo' scope at: https://github.com/settings/tokens" -ForegroundColor White
    Write-Host "3. Run: & '$git' remote set-url origin https://<YOUR_TOKEN>@github.com/$GitHubUsername/$RepoName.git" -ForegroundColor White
    Write-Host "4. Run: & '$git' push -u origin main" -ForegroundColor White
}
