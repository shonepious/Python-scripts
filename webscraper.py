import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

scraper = input("which webpage would you like to scrape for credentials?")

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
options = Options()

driver.get(f"{scraper}")
repo = driver.find_elements(By.CLASS_NAME, "repo")
time.sleep(1)

links = []
complete_link = []


def link_looper(next_page):
    driver.get(next_page)
    page_after_repo = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    if not page_after_repo:
        print("Cannot resolve repository from this GitHub page.")
    for a in page_after_repo:
        if "py" in a.text:
            link = f"{next_page}/blob/main/{a.text}"
            credentials(link)


def credentials(page_link):
    html = f"{driver.page_source}"
    if "password" in html:
        print(f"Credentials found at {page_link}")
    else:
        print("No credentials were found at this address.")


for i in repo:
    links.append(i.text)
for repos in links:
    repo_link = f"{scraper}/{repos}"
    complete_link.append(repo_link)
    link_looper(repo_link)
