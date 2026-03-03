import pyautogui
import time

# Automação para abrir o chrome

pyautogui.PAUSE = 1

# Entrando no Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Pressionando o atalho
pyautogui.click(x=734, y=508)

# Abrindo nova janela e pressionando outro atalho
pyautogui.hotkey("ctrl", "t")
pyautogui.click(x=928, y=485)


