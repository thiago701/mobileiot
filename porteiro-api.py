from flask import Flask,jsonify,request

mensagem = ''
app = Flask(__name__)

@app.route('/')
def init():
    return 'Porteiro-API'

#local
@app.route('/api/falar', methods=['GET', 'POST'])
def receberFala(audio):
    print(audio)
    return 'Testa receber fala.'

#cloud
@app.route('/api/notificar')
def notificarMorador():
    print('teste notificar')
    mensagem = request.args['apartamento']
    return 'Testa notificação'

#cloud
@app.route('/api/notificacoes')
def obterNotificacoes():
    print('msg:',mensagem)
    if(mensagem != None):
        return (mensagem)
        
        
