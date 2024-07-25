from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'que estou na página do instituto joga junto')
def step_on_instituto_page(context):
    context.browser = Firefox()
    context.browser.get('https://www.jogajuntoinstituto.org/')
          
    title = context.browser.title
    assert 'Instituto Joga Junto' in title, "Título não encontrado"

@when(u'preencho o formulário de contato')
def step_impl(context):
    input_name = context.browser.find_element(By.NAME,'nome').send_keys('Lucila')
    input_email = context.browser.find_element(By.NAME,'email').send_keys('l7u7c7@gmail.com')
    subject = context.browser.find_element(By.NAME,'assunto')
    input_message = context.browser.find_element(By.NAME,'body').send_keys('Teste auto')
  
    select_subject = Select(subject)
    select_subject.select_by_visible_text('Ser facilitador')                                                           


@when(u'aperto o botão enviar')
def step_impl(context):
   button_submit = context.browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/section[8]/div[1]/form/button/p').submit()

@then(u'os dados são recebidos com sucesso')
def step_impl(context):   
    # import ipdb; ipdb.sset_trace()
    wait = WebDriverWait(context.browser, 10)

    alert = wait.until(EC.alert_is_present())
    
    assert 'Dados recebidos' in alert.text, "Dados não foram recebidos"


   # https://github.com/InstitutoJogaJuntoOrg/teste_de_contrato