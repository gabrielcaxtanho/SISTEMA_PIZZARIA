
from flask import Flask, render_template, request, redirect, session, flash, url_for
#from twilio.rest import Client

## CRIAR INTEGRAÇÃO ENTRE AS FUNÇÕES

#account_sid = "YOUR ACCOUNT SID"
#auth_token  = "YOUR TOKEN"
#client = Client(account_sid, auth_token)
class PEDIDO:
    def __init__(self, cliente, pedido, mesa, status, senha):
        self.cliente = cliente
        self.pedido = pedido
        self.mesa = mesa
        self.status = status
        self.senha = senha
pedido1 = PEDIDO("CLIENTE EXEMPLO", "PEDIDO EXEMPLO", "MESA EXEMPLO", "STATUS EXEMPLO", "SENHA CLIENTE")
lista = [pedido1]

app = Flask(__name__)

app.secret_key = 'gabriel'



###ROTAS DO SITE
@app.route('/')
def index():
  #  for pedido in lista:
   #     if pedido.status == 'PRONTO':
   #         message = client.messages.create(
   #                    to="+your_number",
   #                  from_="twilio_number",
  #                   body=f'mas uma pizza pronta')
  #          print(message.sid)
    return render_template("lista.html", titulo="PEDIDOS", pedidos=lista)

@app.route('/novopedido')
def novo():
    return render_template('novo.html', titulo='Novo Pedido')

@app.route('/criar', methods=['POST',])
def criar():
    cliente = request. form['cliente']
    pedido = request. form['pedido']
    mesa = request. form['mesa']
    status = request.form['status']
    senha = request.form['senha']
    pedido = PEDIDO(cliente, pedido, mesa, status, senha)
    lista.append(pedido)
    return redirect('/')
##criar pagina para estilização apenas do status do pedido

@app.route('/atualizar')
def atualizar():
    return render_template('atualizar.html', titulo='Atualizar Pedido')



@app.route('/atualizarpedido', methods=['POST'])
def atualizarpedido():
    senha = request.form['senha']  # Obtém a senha do pedido do formulário
    novo_status = request.form['status']

    for pedido in lista:
        if pedido.senha == senha:
            pedido.status = novo_status
            flash(f'Status do pedido atualizado para: {novo_status}', 'success')
            return redirect('/')

    flash('Pedido não encontrado. Verifique a senha.', 'danger')
    return redirect('/atualizar')

@app.route('/deletar')
def deletar():
    return render_template('deletarpedido.html', titulo="REMOVER PEDIDO")

@app.route('/deletarpedido', methods=['POST'])
def deletarpedido():
    senha = request.form['senha'] ## pega a senha do pedido do formulario

    for pedido in lista:
        if pedido.senha == senha:
            lista.remove(pedido)
            return redirect('/')

    flash('Pedido não encontrado. Verifique a senha.', 'danger')
    return redirect('/deletar')




@app.route('/cozinha')
def cozinha():
    return render_template("cozinha.html", titulo="COZINHA", pedidos=lista)




@app.route('/painelsenhas')
def painelsenhas():
    return render_template("painel.html", titulo="SENHAS", pedidos=lista)



if __name__ == "__main__":
    app.run()





## UTILIZAR BIBLIOTECA DE SMS PARA GERENCIAMENTO DE PEDIDOS
## ESTILIZAÇÃO EM BOOTSTRAP
## INTEGRAÇÃO COM FLASK