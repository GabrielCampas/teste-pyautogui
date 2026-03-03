import pyautogui
import time

# Abrindo o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(0.75)

# Pesquisando o site
pyautogui.write("localiza cep")
time.sleep(0.5)

# Clicando na URL
pyautogui.press("enter")
time.sleep(0.5)

# Colocando o cursor na caixa de texto
pyautogui.click(x=396, y=336)
time.sleep(0.5)

# Escrevendo o CEP
pyautogui.write("17209373")
time.sleep(0.5)

# Clicando em "Buscar"
pyautogui.click(x=704, y=471)
