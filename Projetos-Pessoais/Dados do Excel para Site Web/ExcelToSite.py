import selenium.webdriver.edge.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl
import pyperclip
import pyautogui

wb = openpyxl.load_workbook('produtos_ficticios.xlsx')
ws = wb['Produtos']
driver = webdriver.Edge()
driver.get('https://cadastro-produtos-devaprender.netlify.app/')
sleep(5)
for row in ws.iter_rows(min_row=2, max_row=22):
    nome_produto = row[0].value
    pyperclip.copy(nome_produto)
    barra = driver.find_element(By.XPATH, '//*[@id="product_name"]')
    barra.send_keys(nome_produto)

    descricao = row[1].value
    pyperclip.copy(descricao)
    barra = driver.find_element(By.XPATH, '//*[@id="description"]')
    barra.send_keys(descricao)

    categoria = row[2].value
    pyperclip.copy(categoria)
    barra = driver.find_element(By.XPATH, '//*[@id="category"]')
    barra.send_keys(categoria)

    codigo_produto = row[3].value
    pyperclip.copy(codigo_produto)
    barra = driver.find_element(By.XPATH, '//*[@id="product_code"]')
    barra.send_keys(codigo_produto)

    peso = row[4].value
    pyperclip.copy(peso)
    barra = driver.find_element(By.XPATH, '//*[@id="weight"]')
    barra.send_keys(peso)

    dimensao = row[5].value
    pyperclip.copy(dimensao)
    barra = driver.find_element(By.XPATH, '//*[@id="dimensions"]')
    barra.send_keys(dimensao)

    botao = driver.find_element(By.XPATH, '//*[@class="btn btn-primary me-2"]')
    botao.click()
    sleep(3)

    preco = row[6].value
    pyperclip.copy(preco)
    barra = driver.find_element(By.XPATH, '//*[@id="price"]')
    barra.send_keys(preco)

    quantidade_estoque = row[7].value
    pyperclip.copy(quantidade_estoque)
    barra = driver.find_element(By.XPATH, '//*[@id="stock"]')
    barra.send_keys(quantidade_estoque)

    data_validade = row[8].value
    pyperclip.copy(data_validade)
    barra = driver.find_element(By.XPATH, '//*[@id="expiry_date"]')
    barra.send_keys(data_validade)

    cor = row[9].value
    pyperclip.copy(cor)
    barra = driver.find_element(By.XPATH, '//*[@id="color"]')
    barra.send_keys(cor)

    tamanho = row[10].value
    pyperclip.copy(tamanho)
    barra = driver.find_element(By.XPATH, '//*[@id="size"]')
    barra.click()
    sleep(1)
    if tamanho == 'Grande':
        barra = driver.find_element(By.XPATH, '//*[@value="Grande"]')
    elif tamanho == 'Médio':
        barra = driver.find_element(By.XPATH, '//*[@value="Médio"]')
    else:
        barra = driver.find_element(By.XPATH, '//*[@value="Pequeno"]')
    barra.click()

    material = row[11].value
    pyperclip.copy(material)
    barra = driver.find_element(By.XPATH, '//*[@id="material"]')
    barra.send_keys(material)

    botao2 = driver.find_element(By.XPATH, '//*[@class="btn btn-primary me-2"]')
    botao2.click()
    sleep(3)

    fabricante = row[12].value
    pyperclip.copy(fabricante)
    barra = driver.find_element(By.XPATH, '//*[@id="manufacturer"]')
    barra.send_keys(fabricante)

    pais_origem = row[13].value
    pyperclip.copy(pais_origem)
    barra = driver.find_element(By.XPATH, '//*[@id="country"]')
    barra.send_keys(pais_origem)

    observacoes = row[14].value
    pyperclip.copy(observacoes)
    barra = driver.find_element(By.XPATH, '//*[@id="remarks"]')
    barra.send_keys(observacoes)

    codigo_barras = row[15].value
    pyperclip.copy(codigo_barras)
    barra = driver.find_element(By.XPATH, '//*[@id="barcode"]')
    barra.send_keys(codigo_barras)

    localizacao_no_armazem = row[16].value
    pyperclip.copy(localizacao_no_armazem)
    barra = driver.find_element(By.XPATH, '//*[@id="warehouse_location"]')
    barra.send_keys(localizacao_no_armazem)

    botao3 = driver.find_element(By.XPATH, '//*[@class="btn btn-primary me-2"]')
    botao3.click()
    sleep(3)
    pyautogui.hotkey('Enter')
    sleep(3)

    botao4 = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]')
    botao4.click()
    sleep(3)

