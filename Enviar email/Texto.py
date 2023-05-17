def texto1(nome, email, mensagem):
 return f''' <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Exemplo de E-mail</title>
        </head>
        <body>
            <h2>Olá!</h2>
            
            <p>Este é um exemplo de e-mail HTML.</p>
            
            <p>Alguns detalhes:</p>
            <ul>
                <li><strong>Nome:</strong> {nome} </li>
                <li><strong>E-mail:</strong> {email} </li>
                <li><strong>Mensagem:</strong> {mensagem} </li>
            </ul>
            
            <p>Atenciosamente,</p>
            
            <p>Seu Nome</p>

        </body>
        </html> '''

def texto2(mensagem): 
   return f''' <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>
                    <p>{mensagem}</p>

                </body>
                </html> '''