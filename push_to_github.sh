#!/bin/bash

# Script konumuna git
cd "/Users/berraturan/Desktop/staj/Ai Agent Tutorial/Ai_Agent" || exit

# GitHub remote URL'sini güncelle (bir kere çalışır)
git remote set-url origin https://github.com/codedbybell/Ai_Agent_Domain_Scraper.git

# Her ihtimale karşı güncellemeleri çek
git pull origin main --rebase

# Commit oluştur (boş commit olmasın diye değişiklik kontrolü ekledik)
if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m "Auto update domains $(date '+%Y-%m-%d %H:%M:%S')"
    git push origin main
else
    echo "No changes to commit."
fi
