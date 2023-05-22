import smtplib
import email.message
import pandas as pd

# leitura do arquivo Excel e carregamento em um DataFrame
df = pd.read_excel('C:/Users/devic/Downloads/email/Adequação de Franquia.xlsx')

# endereços de emails 
enviar_emails = {
    "Alessandro": "alessandro@suflex.com.br"
    }

# corpo do email
def corpo_email(cliente, mes, atual, nova):
    mensagem = f"""
<body>
	<p>Por favor, realize a adequação de franquia do {cliente}<br>
	<strong>Início:</strong> {mes}<br>
	<strong>Franquia Atual:</strong> {atual} etiquetas<br>
	<strong>Nova Franquia:</strong> {nova} etiquetas</p>
    <img src="https://ncdn0.infojobs.com.br/logos/2022/12/07/684545.jpg?f=44937.8036264236?v=1" alt="Imagem de exemplo">
	<p>Ricardo Pereira</p>
	<p>R. Purpurina, 400 | <a href="http://www.suflex.com.br">www.suflex.com.br</a><br>
	+55 11 976002471 | <a href="mailto:ricardo@suflex.com.br">ricardo@suflex.com.br</a></p>
</body>
</html>
    """
    return mensagem

# função que envia o email
def enviar_email(emails, cliente, mes, atual, nova):
    msg = email.message.Message()
    msg['Subject'] = f"[ADEQUAÇÃO DE FRANQUIA] - {cliente}"
    msg['From'] = 'alessandroneno9@gmail.com'
    msg['To'] = emails
    password = 'xdhczonitxzdmjpk' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email(cliente, mes, atual, nova))

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

# laço para enviar diferentes emails para diferentes clientes
for dados_clientes in df.values:
    for i in enviar_emails.items():
        enviar_email(i[1], dados_clientes[0], dados_clientes[1], dados_clientes[2], dados_clientes[3])
        