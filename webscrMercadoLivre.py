from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Inicialize o driver do Selenium
driver = webdriver.Chrome()

# Abra uma página da web
driver.get("https://lista.mercadolivre.com.br/calcados-roupas-bolsas/meninos/camisa-azul_PriceRange_85-0_Discount_5-100_BRAND_12046044_NoIndex_True#applied_filter_id%3Dprice%26applied_filter_name%3DPre%C3%A7o%26applied_filter_order%3D2%26applied_value_id%3D85.0-*%26applied_value_name%3DMais+de+R%2485%26applied_value_order%3D3%26applied_value_results%3D5%26is_custom%3Dfalse")
time.sleep(1)
aceitar_cookies = driver.find_element(By.XPATH, "//button[@data-testid='action:understood-button']").click()

# Encontre os elementos que você deseja clicar para abrir novas abas
elements_to_click = driver.find_elements(By.XPATH, "//h2[@aria-level='3']")

# Use ActionChains para abrir uma nova aba para cada elemento encontrado
action_chains = ActionChains(driver)
titles = []
shirts = []

for element in elements_to_click:
    action_chains.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
    
    # Agora você está na nova aba, alterne o foco para a nova aba
    driver.switch_to.window(driver.window_handles[-1])
    
    # Encontre o título na nova aba
    # .text extrai somente o texto do XPATH
    title_cel = driver.find_element(By.XPATH, "//h1[@class='ui-pdp-title']")
    titles.append(title_cel.text)

    # Encontrar cor da blusa
    shirt = driver.find_element(By.XPATH, "//span[@id='picker-label-COLOR_SECONDARY_COLOR']")
    titles.append(shirt.text)                    

    # Feche a aba atual para voltar à página anterior
    driver.close()

    # Volte à primeira aba original
    driver.switch_to.window(driver.window_handles[0])

# Printando o dados coletados 
for title in titles:
    print(title,"\n")

# for sht in shirts:
#     print(sht)


# Feche o driver quando terminar
driver.quit()
