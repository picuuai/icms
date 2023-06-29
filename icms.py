from selenium import webdriver
from selenium.webdriver.common.by import By
import time as horario
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os


options = Options()
#options.add_argument("--headless")  # Executar o Chrome em modo headless (sem interface gráfica)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_experimental_option('prefs', {
    'download.default_directory': os.getcwd(),
    'download.prompt_for_download': False,
    'safebrowsing.enabled': True
})

driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://www2.fazenda.mg.gov.br/arrecadacao/ctrl/ARRECADA/ARRECADA/DOCUMENTO_ARRECADACAO?ACAO=VISUALIZAR")

print("escolhendo tipo")
horario.sleep(1)


print("selecionar")

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/div/div[1]" ).click()


driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/div/div[2]/span[2]" ).click()


driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[3]/tbody/tr/td/a/img" ).click()

print("selecionar cliente")

WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/form/table[2]/tbody/tr[3]/td[3]/a/img")))

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[2]/tbody/tr[3]/td[2]/input" ).send_keys("476.503.984.00-27")


driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[2]/tbody/tr[3]/td[3]/a/img" ).click()

print("aguardando selecionar dae")


WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[3]/td[2]/div/div")))


driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[3]/td[2]/div/div/div[1]" ).click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[3]/td[2]/div/div/div[2]/span[10]" ).click()


print("carregando datas")

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[4]/td[2]/input[1]" ).send_keys('07/07/2023')
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[5]/td[2]/input[1]" ).send_keys('07/07/2023')

print("carregando competencias")


print("mensal")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[6]/td[3]/div/div[1]" ).click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[6]/td[3]/div/div[2]/span[2]" ).click()

print("mes")

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[7]/td[2]/div/input" ).click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[7]/td[2]/div/div[2]/span[7]" ).click()

print("ano")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[8]/td[2]/div/input" ).click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[8]/td[2]/div/div[2]/span[2]" ).click()

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[10]/td[2]/input" ).send_keys("123456")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[11]/td/div/table/tbody/tr[1]/td[2]/input" ).send_keys("10,00")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[4]/tbody/tr[12]/td[2]/textarea" ).send_keys("Dae ref. 06/2023")


driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table[5]/tbody/tr/td[1]/a/img" ).click()


WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/form/table/tbody/tr[2]/td[1]/a/img")))

print("salvando dae")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/form/table/tbody/tr[2]/td[1]/a/img" ).click()

horario.sleep(5)

driver.quit()