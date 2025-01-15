'''
Passo 1: Abrir o sistema
Passo 2: Fazer login
Passo 3: Importar base de dados dos produtos
Passo 4: Cadastrar 1 produto
Passo 5: Repetir passo 4 até acabar todos os produtos

'''

import pyautogui
import time
import pandas

time.sleep(5)


link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=448, y=887)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=945, y=568) #Email
pyautogui.write('teste@teste.gmail.com')
pyautogui.press('tab') #pyautogui.click(x=945, y=711) #Senha
pyautogui.write('12345')
pyautogui.press('tab') #pyautogui.click(x=945, y=796) #Logar
pyautogui.press('enter')
time.sleep(3)


tabela = pandas.read_csv('Automacao\produtos.csv')
time.sleep(3)

for linha in tabela.index:
    #Passo 4: Cadastrar 1 produto
    pyautogui.click(x=892, y=387) 

    #Codigo do produto
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    #Marca 
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    #Tipo
    tipo= tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    #Categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    #Preço unitário
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    #Custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    #Observações
    obs = tabela.loc[linha, 'obs']
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press('tab')

    #Enviar
    pyautogui.press('enter')

    #Voltar para o topo
    pyautogui.scroll(2000)

