#!/bin/bash
cd /Users/berraturan/Desktop/staj/Ai\ Agent\ Tutorial/Ai_Agent

# Git yapılandırması
git add domains.txt
git commit -m "Auto update domains $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main