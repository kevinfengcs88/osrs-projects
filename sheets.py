import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup
import time

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("osrsbis").sheet1

def scrape(site, int1):
    percent = sheet.cell(int1, 9).value
    result = requests.get(site)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, "html.parser")
    item = soup.find(id="item_stat_overall")
    sheet.update_cell(int1, 5, item.text)
    new_percent = sheet.cell(int1, 9).value
    if new_percent > percent:
        sheet.update_cell(int1, 10, "no")
    elif new_percent < percent:
        sheet.update_cell(int1, 10, "YES")

while True:
    scrape("https://www.ge-tracker.com/item/armadyl-helmet", 5)
    scrape("https://www.ge-tracker.com/item/armadyl-chestplate", 6)
    scrape("https://www.ge-tracker.com/item/armadyl-chainskirt", 7)
    scrape("https://www.ge-tracker.com/item/twisted-buckler", 8)
    scrape("https://www.ge-tracker.com/item/pegasian-boots", 9)
    scrape("https://www.ge-tracker.com/item/armadyl-crossbow", 10)
    scrape("https://www.ge-tracker.com/item/amulet-of-torture", 11)
    scrape("https://www.ge-tracker.com/item/avernic-defender-hilt", 12)
    scrape("https://www.ge-tracker.com/item/bandos-tassets", 13)
    scrape("https://www.ge-tracker.com/item/primordial-boots", 14)
    scrape("https://www.ge-tracker.com/item/ghrazi-rapier", 15)
    scrape("https://www.ge-tracker.com/item/arcane-prayer-scroll", 16)
    scrape("https://www.ge-tracker.com/item/dinh-s-bulwark", 17)
    scrape("https://www.ge-tracker.com/item/ancestral-hat", 18)
    scrape("https://www.ge-tracker.com/item/bandos-chestplate", 19)
    scrape("https://www.ge-tracker.com/item/bandos-godsword", 20)
    scrape("https://www.ge-tracker.com/item/dragon-hunter-lance", 21)

    time.sleep(600)
