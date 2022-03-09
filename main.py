
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import inventory
import openwallet

points = 0
#add layered
myCode = {'Name': 'Atom', 'password': '1234', 'value': 200}
targetbag = ['Gold','Ruby']
bag = {'Gold': 0, 'Ruby': 0}

openwallet.addToInventory(inventory, bag)
openwallet.displayInventory(bag)
inventory.total_worth(bag)
