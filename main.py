
#Usar o alias (auto) para substituir a palava pyautogui
import pyautogui as auto
import time
import os

#Definir o tempo de espera do comando auto
auto.PAUSE = 0.5

#Abre o menu iniciar
auto.press('win')
#Abre o app escolhido + o comando de enter
auto.write('firefox')
auto.press('enter')
time.sleep(2)
auto.write('github.com')
auto.press('enter')
#Abrir uma nova aba no navegador
time.sleep(2)
auto.hotkey('ctrl', 't')
auto.write('classroom.google.com')
auto.press('enter')
time.sleep(2)
auto.hotkey('ctrl', 't')
auto.write('https://meusenai.senai.br/')
auto.press('enter')
#Abrir o Windows Explorer
time.sleep(2)
auto.hotkey('win', 'e')
auto.press('enter')
time.sleep(2)
auto.hotkey('alt', 'f4')
auto.press('enter')

#desligar o computador
time.sleep(2)
os.system('shutdown /s')

