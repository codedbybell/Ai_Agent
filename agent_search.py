from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import os

# ------------------------------
# Yardımcı fonksiyonlar
# ------------------------------

def human_sleep(min_s=2, max_s=4):
    time.sleep(random.uniform(min_s, max_s))

def human_scroll(driver):
    # Artık scroll yapmıyoruz
    return

def save_domain(domain: str):
    existing = set()
    if os.path.exists("domains.txt"):
        with open("domains.txt", "r", encoding="utf-8") as f:
            for line in f:
                existing.add(line.strip())
    if domain not in existing:
        with open("domains.txt", "a", encoding="utf-8") as f:
            f.write(domain + "\n")

# ------------------------------
# Asıl scraping fonksiyonu
# ------------------------------

def scrape_temp_mails(driver, current_site):
    found_any = False

    if "temp-mail.io" in current_site:
        try:
            change_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='change-button']"))
            )
            change_button.click()
            human_sleep()
            select_trigger = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-qa='selected-domain']"))
            )
            select_trigger.click()
            human_sleep()
            domain_buttons = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-qa='domain-option']"))
            )
            for btn in domain_buttons:
                d = btn.text.strip()
                if d:
                    print(f"📌 temp-mail.io domain: {d}")
                    save_domain(d)
                    found_any = True
        except Exception as e:
            print(f"❌ temp-mail.io domain alınamadı: {e}")

    if "tempmail.com.tr" in current_site:
        try:
            change_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button#change_email_btn"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", change_button)
            human_sleep()
            try:
                change_button.click()
            except:
                driver.execute_script("arguments[0].click();", change_button)
            human_sleep()
            select_elem = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "select#name_domain"))
            )
            for opt in select_elem.find_elements(By.TAG_NAME, "option"):
                if not opt.get_attribute("disabled"):
                    domain_value = opt.get_attribute("value").strip()
                    if domain_value:
                        print(f"📌 tempmail.com.tr domain: {domain_value}")
                        save_domain(domain_value)
                        found_any = True
        except Exception as e:
            print(f"❌ tempmail.com.tr domain alınamadı: {e}")

    if "tempail.com" in current_site:
        try:
            elem = driver.find_element(By.CSS_SELECTOR, "input#eposta_adres")
            val = elem.get_attribute("value")
            if val and "@" in val:
                domain = val.split("@")[1]
                print(f"📧 tempail.com: {val} (domain: {domain})")
                save_domain(domain)
                found_any = True
        except:
            pass

    if "tempmail.net" in current_site:
        try:
            elem = driver.find_element(By.CSS_SELECTOR, "input#eposta_adres")
            val = elem.get_attribute("value")
            if val and "@" in val:
                domain = val.split("@")[1]
                print(f"📧 tempmail.net: {val} (domain: {domain})")
                save_domain(domain)
                found_any = True
        except:
            pass

    if "tempmail.email" in current_site:
        try:
            for _ in range(3):
                elem = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.email-block__genEmail.js-email"))
                )
                val = elem.text.strip()
                if val and "@" in val:
                    domain = val.split("@")[1]
                    print(f"📧 tempmail.email: {val} (domain: {domain})")
                    save_domain(domain)
                    found_any = True
                try:
                    refresh_btn = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "button#js-btn-deleteEmail"))
                    )
                    refresh_btn.click()
                    human_sleep(3, 5)
                except:
                    break
        except:
            pass

    if "temp-mail.org" in current_site:
        try:
            elem = driver.find_element(By.CSS_SELECTOR, "input#mail")
            val = elem.get_attribute("value")
            if val and "@" in val:
                domain = val.split("@")[1]
                print(f"📧 temp-mail.org: {val} (domain: {domain})")
                save_domain(domain)
                found_any = True
        except:
            pass

    if "fakemail.net" in current_site:
        try:
            elem = driver.find_element(By.CSS_SELECTOR, "span#email")
            val = elem.text.strip()
            if val and "@" in val:
                domain = val.split("@")[1]
                print(f"📧 fakemail.net: {val} (domain: {domain})")
                save_domain(domain)
                found_any = True
        except:
            pass

    if "emailfake.com" in current_site:
        try:
            # 🔹 Önce domain girişindeki input'u al
            elem = driver.find_element(By.CSS_SELECTOR, "input#domainName2")
            val = elem.get_attribute("value")
            if val:
                print(f"📧 emailfake.com input domain: {val}")
                save_domain(val)

            # 🔹 Dropdown açma butonunu bul ve tıkla
            drop_button = driver.find_element(By.CSS_SELECTOR, "div.e7m.dropselect")
            driver.execute_script("arguments[0].scrollIntoView(true);", drop_button)
            human_sleep()
            try:
                drop_button.click()
            except:
                driver.execute_script("arguments[0].click();", drop_button)
            human_sleep(1, 2)

            # 🔹 Şimdi yeni açılan listeden domainleri al
            domain_elems = driver.find_elements(By.CSS_SELECTOR, "div#newselect p")
            for p in domain_elems:
                t = p.text.strip()
                if t:
                    print(f"📧 emailfake.com p domain: {t}")
                    save_domain(t)
        except Exception as e:
            print(f"❌ emailfake.com domain alınamadı: {e}")

    if "yopmail.com" in current_site:
        try:
            driver.get("https://yopmail.com/domain?d=all")
            time.sleep(3)
            items = driver.find_elements(By.CSS_SELECTOR, "body td")
            if not items:
                items = driver.find_elements(By.CSS_SELECTOR, "body *")

            # mevcut domainleri yükle
            existing_domains = set()
            if os.path.exists("domains.txt"):
                with open("domains.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        existing_domains.add(line.strip())

            # yeni domainleri burada topla
            new_yopmail_domains = []

            for it in items:
                text = it.text.strip()
                # Yopmail domain?d=all sayfasında '@' yok, doğrudan domain yazıyor
                if text and "." in text and "@" not in text:
                    clean_domain = text
                    if clean_domain not in existing_domains:
                        print(f"📌 yopmail domain: {clean_domain}")
                        save_domain(clean_domain)
                        new_yopmail_domains.append(clean_domain)

            if new_yopmail_domains:
                found_any = True
            else:
                print("ℹ️ Yopmail'de yeni domain bulunamadı.")
                found_any = True  # Domainler var ama yeni yok, yine de hata vermesin diye True yapıyoruz
        except Exception as e:
            print(f"❌ yopmail domain alınamadı: {e}")

    if "disposablemail.com" in current_site:
        try:
            elem = driver.find_element(By.CSS_SELECTOR, "span#email")
            val = elem.text.strip()
            if val and "@" in val:
                domain = val.split("@")[1]
                print(f"📧 disposablemail.com: {val} (domain: {domain})")
                save_domain(domain)
                found_any = True
        except:
            pass

    if "temporarymail.com" in current_site:
        try:
            # Change butonunu bekle ve tıkla
            change_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.viewChangeModal"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", change_btn)
            human_sleep()
            try:
                change_btn.click()
            except:
                driver.execute_script("arguments[0].click();", change_btn)
            human_sleep(2, 3)

            # Domain dropdown'unu bekle
            select_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "select#selectedDomain"))
            )
            for opt in select_elem.find_elements(By.TAG_NAME, "option"):
                val = opt.text.strip().replace("@", "")
                if val:
                    print(f"📧 temporarymail.com domain: {val}")
                    save_domain(val)
                    found_any = True
        except Exception as e:
            print(f"❌ temporarymail.com domain alınamadı: {e}")

    if not found_any:
        print("⚠️ Bu sitede uygun selector bulunamadı.")

# ------------------------------
# Bing arama ve gezinme
# ------------------------------

def search_temp_sites(query="tempmail", max_sites=5):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    print("🔎 Bing'e gidiliyor...")
    driver.get("https://www.bing.com")
    human_sleep(3, 5)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    human_sleep()
    search_box.send_keys(Keys.RETURN)
    print(f"✅ '{query}' için arama yapıldı.")
    human_sleep(4,6)

    links = driver.find_elements(By.CSS_SELECTOR, "li.b_algo h2 a")
    site_links = []
    for link in links:
        href = link.get_attribute("href")
        if href and href.startswith("http"):
            site_links.append(href)
            if len(site_links) >= max_sites:
                break

    print(f"✅ {len(site_links)} site bulundu:")
    for site in site_links:
        print("➡", site)

    skip_sites = [
        "tempail.com/en",
        "emailondeck.com",
        "temp-mail.org/tr",
        "tempail.com/tr/fake-mail/"
    ]

    for site in site_links:
        if any(skip in site for skip in skip_sites):
            print(f"⏩ {site} atlanıyor (listeye alınmadı).")
            continue
        print(f"\n🌐 {site} açılıyor...")
        try:
            driver.get(site)
            human_sleep(3,5)
            human_scroll(driver)
            human_sleep(1,2)
            print(f"✅ {site} sayfasına girildi. Şimdi scraping deneniyor...")
            scrape_temp_mails(driver, site)
        except Exception as e:
            print(f"❌ {site} açılırken hata: {e}")
        human_sleep(2,4)

    driver.quit()
    print("\n✅ Tüm siteler gezildi ve scraping tamamlandı!")

if __name__ == "__main__":
    search_terms = ["tempmail", "fake mail", "temporary mail", "disposable email"]
    for term in search_terms:
        print(f"\n🔎 '{term}' kelimesi için arama başlatılıyor...")
        search_temp_sites(term, max_sites=5)