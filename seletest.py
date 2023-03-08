from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

directory_path = "/Users/mthomati/Downloads/Scripts/Automation/Jenkins/"
url = "https://ec.synnex.com/stellr-reseller-portal/consolidated_invoice"
user = 'admin'


class Auto:
    def __init__(self,url):
        options = Options()
        options.headless = False
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(executable_path=directory_path+'chromedriver',options=options)
        self.url = url
    
    def open(self):
        print("Opening URL ...")
        self.driver.get(self.url)
        time.sleep(2)

def main():
    auto = Auto(url)
    auto.open()


if __name__ == '__main__':
    main()