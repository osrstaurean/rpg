from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

myCode = {'Name': 'Atom', 'password': '1234', 'value': 200}
bag = {'Gold': 0, 'Ruby': 0}

def items():
    bag = 0

def displayInventory(bag):
    points = 0
    itemtotal = 0
    # add layered

    print("Total number of items " + str(itemtotal))
    displayInventory(bag)
    print(bag)
def addToInventory(bag, additems):
    bag = {'Gold': 0, 'Ruby': 0}
    targetbag = ['Gold', 'Ruby','Gold','btc']
    bag = addToInventory(bag, targetbag)
    displayInventory(bag)
