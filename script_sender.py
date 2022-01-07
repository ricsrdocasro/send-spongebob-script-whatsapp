from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from win32com.client import Dispatch

driver = webdriver.Chrome(executable_path='C:\Python39\Scripts\chromedriver')
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()

pessoa = driver.find_element_by_xpath("""/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[11]""")
pessoa.click()

caixa_de_texto = driver.find_element_by_xpath("""/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]""")

with open("C:/Users/Darth/OneDrive/Área de Trabalho/script_new.txt", "r") as script:
    for line in script:
        caixa_de_texto.send_keys(line)
