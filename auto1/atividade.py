from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

browser = Firefox()
 
link = "https://google.com"

browser.get(link)

input_area = browser.find_element(By.ID,"APjFqb" )

input_area.send_keys("Instituto Joga Junto")
input_area.send_keys(Keys.ENTER)

from time import sleep; sleep(3)
result_search = browser.find_elements(By.TAG_NAME, "h3")
#outra maneira de busca
# result_search = browser.find_elements(By.PARTIAL_LINK_TEXT, "Instituto Joga Junto")  
print(result_search)

#Usado para clicar sem a necessidade do check abaixo
# for result in result_search:    
#     result.click()
#     print("Instituto Joga Junto")

#Este jeito não roda no meu pc
check = False

for result in result_search:
    while check == False:   
        if result.text == "Instituto Joga Junto" :
            result.click()
            print("oi")
            check = True

assert "Instituto Joga Junto" in browser.title, "Título não encontrado"
sleep(5)
accept_cookie = browser.find_element(By.ID,"adopt-accept-all-button").click()

field_name = browser.find_element(By.ID, "nome").send_keys("Lucila")
field_email = browser.find_element(By.ID, "email").send_keys("l7u7c7@gmail.com")
field_subject = browser.find_element(By.ID, "assunto")

# import ipdb; ipdb.sset_trace()
select_subject= Select(field_subject)

assunto = select_subject.select_by_visible_text("Ser facilitador")
field_message = browser.find_element(By.NAME, "body"). send_keys("Olá, teste de automação via vscode.")

submit_button = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")
submit_button.submit()
sleep(3)

browser.quit()