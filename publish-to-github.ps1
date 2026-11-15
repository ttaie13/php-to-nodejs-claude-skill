# Publish all project files, including .claude and .github.
# Author: Tariq Al-Taie
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Git is not installed. Install Git for Windows first.' }
if (-not (Test-Path '.git')) { git init -b main }
git add -A
Write-Host 'Files staged for publication:'
git diff --cached --name-only
if (-not (git diff --cached --quiet)) { git -c user.name='Tariq Al-Taie' -c user.email='ttaie13@users.noreply.github.com' commit -m 'Publish PHP to Node.js Claude Skill' }
if (-not (git remote | Select-String '^origin$')) { git remote add origin https://github.com/ttaie13/php-to-nodejs-claude-skill.git }
git branch -M main
git push -u origin main
Write-Host 'Published to https://github.com/ttaie13/php-to-nodejs-claude-skill'
