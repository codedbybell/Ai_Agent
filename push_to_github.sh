#!/bin/bash

cd "/Users/berraturan/Desktop/staj/Ai Agent Tutorial/Ai_Agent" || exit
git remote set-url origin https://github.com/codedbybell/Ai_Agent_Domain_Scraper.git

git stash push --include-untracked -m "Auto stash before pull"
git pull origin main --rebase
git stash pop || true

if [ -n "$(git status --porcelain)" ]; then
    git add .
    git commit -m "Auto update domains $(date '+%Y-%m-%d %H:%M:%S')"
    git push origin main
else
    echo "No changes to commit."
fi
