#language: pt

Funcionalidade: Envio de dados ao formulário
    Cenário: Envio de dados com assunto quero ser facilitador
    
    Como usuário do site do Instituto Joga junto
    Quero preencher o formulário de contato
    Para enviar o formulário preenchido


    Dado que estou na página do instituto joga junto
    Quando preencho o formulário de contato
    E aperto o botão enviar
    Então os dados são recebidos com sucesso