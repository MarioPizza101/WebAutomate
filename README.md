# Web Automation Documentation 

This repo contains a Python script for performing a web automation task to
open a web session to Synnex. The `main` branch is under active development and may not offer a stable interface.

## Requirements
* Python 3.6+


### Imports
Import all necessary modules

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
```


### Global Variables
Specify the directory path where the web driver is located.  Define the URL to access along with the default username

```python
directory_path = "/Users/mthomati/Downloads/Scripts/Automation/Jenkins/"
url = "https://ec.synnex.com/stellr-reseller-portal/consolidated_invoice"
user = 'admin'
```


### Class and Constructor
A class object holding all web automation tasks.  When an object is built, an initializer is created to specify options and setup attributes with the driver and url

```python
class Auto:
    def __init__(self,url):
        options = Options()
        options.headless = False
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(executable_path=directory_path+'chromedriver',options=options)
        self.url = url
```


### Class: Open Method
When the 'open' method is called, it will reference the driver attribute and open the URL.  Afterwards, pause for 2 seconds.

```python
def open(self):
        print("Opening URL ...")
        self.driver.get(self.url)
        time.sleep(2)
```


### Main Function
A main function holding all of the actions needed to run for this web automation job

```python
def main():
    auto = Auto(url)
    auto.open()
```



### Run Main
When the script run, run the 'main' function

```python
if __name__ == '__main__':
    main()
```