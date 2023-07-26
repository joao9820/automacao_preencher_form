import pyautogui, time, pandas as pd;

#Espera um tempo para executar as etapas do pyautogui
pyautogui.PAUSE = 1

email = ""
password = ""
url = "http://localhost:3000"

# Pyautogi controla o mouse, teclado e tela do pc. Logo não é possível executar comandos em segundo plano
# Outras bibliotecas python são capazes de executar em segundo plano
# Para interromper algum código de automação, basta arrastar o mouse para o limite superior esquerdo da tela

# O pyautogi trabalha com coordenadas, então não é possível verificar campos por um identificador
# Uma ferramenta que é possível utilizar identificadores é o Selenium, usado principalmente para automatizar testes

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#redimensiona a janela
pyautogui.hotkey("win", "up")

pyautogui.write()
pyautogui.press("enter")


# Tempo em segundos
time.sleep(3)

#selecionar campo de e-mail, necessário executar o find-position mouse, varia de resolução para resolução
pyautogui.click(x=1180, y=450)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(password)

#Antes de inserir informações nos inputs, verificar se o caps lock está desativado

pyautogui.press("tab", 3)
pyautogui.press("enter")

tabela = pd.read_csv("produtos.csv")
print(tabela)


