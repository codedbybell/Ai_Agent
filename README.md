
# 💌✨ Ai Agent – Auto Domain Scraper & Updater ✨💌

Hi there! 👋 Welcome to Ai Agent, a cute little Python-powered helper that loves to collect fresh temporary email domains from all over the internet. 

It keeps them safe in a tidy list for you… and even updates itself on GitHub every week! 🤖💛

---

## ✨ What does it do?

- 🍬 Searches the web for temporary / fake / disposable email services
- 🍬 Scrapes domains directly from each site
- 🍬 Avoids duplicates (because nobody likes clutter 😌)
- 🍬 Saves them in domains.txt so you always have them
- 🍬 Pushes to GitHub automatically every week ✨

---

## 🌸 Folder Structure

Ai_Agent/
- ├─ 🧩 agent_search.py    # Main script to search & scrape
- ├─ 📜 domains.txt        # Automatically updated list of domains
- ├─ 🚀 push_to_github.sh  # Shell script to commit & push changes
- └─ 💌 README.md          # You are here 💛


---

## 💡 How to run?

✨ Make sure you have Python 3 and Chrome installed.

1. **Run the agent:**
   python agent_search.py

   This will:
   - Search Bing for temp mail sites
   - Scrape domains from supported websites
   - Save results into `domains.txt` (no duplicates!)

2. **Weekly Automation:**
   - A cron job runs `push_to_github.sh` every week at your chosen time.
   - It automatically commits and pushes any new domains to this repository.

---

## 🛠️ Requirements

- Python 3.x  
- Google Chrome & ChromeDriver
- Selenium & WebDriver Manager

Install dependencies:
pip install selenium webdriver-manager

---

That’s it! 🎉 Watch it do its thing… Your new domains will magically appear in domains.txt ✨

---

## 🐣 Can I add more sites?

Of course, sweetie! 
🍭 Just add new scraping logic to agent_search.py, and it will handle the rest (no duplicates, promise ✨).

---

## ✨ Maintained with Love

Made with ☕, 💻 and 💛 by @codedbybell (https://github.com/codedbybell)
If you like this project, don’t forget to ⭐ star it and share the love! 🌈💌

---

## Collecting cute little email domains, one scrape at a time. ✨🧸💛
