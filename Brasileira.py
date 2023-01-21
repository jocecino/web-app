from selenium import webdriver as opcoes 
from selenium.webdriver.common.by import By
import time

driver = opcoes.Chrome()
driver.get("https://casino.betfair.com/pt-br/c/roleta")

time.sleep(3)

sequencias_anteriores = [[1,3,], [2,4,], [3,5],[4,6],[5,7],[6,8],[26,26],[36,35],[6,23,12]]

lista=[]

while True:
    for x in range(8):
        elem = driver.find_elements(By.CLASS_NAME,'number')
        elem2 = elem[-x-1].text
        lista.append(elem2)
        
    if lista[-8:] in sequencias_anteriores or lista[-8:][::-1] in sequencias_anteriores:
        print("Sequencia repetida: " + str(lista[-8:]))
        # emitir alerta aqui
    else:
        sequencias_anteriores.append(lista[-2:])
    print(lista[-8:])
    lista = []
    lista.clear()

    time.sleep(39)
    
    
    
   