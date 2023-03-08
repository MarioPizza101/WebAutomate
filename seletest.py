from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

directory_path = "/Users/mthomati/Downloads/Scripts/Automation/Jenkins/"
url = "https://ec.synnex.com/stellr-reseller-portal/consolidated_invoice"
user = 'admin'

options = Options()
options.headless = False
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path=directory_path+'chromedriver',options=options)

### OPEN URL
print("Opening URL ...")
driver.get(url)
time.sleep(2)
