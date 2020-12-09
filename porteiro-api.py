from flask import Flask,jsonify,request
import pandas as pd
import csv, os
import http

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
    msg = 'Visita para apt {}!'.format(request.args['apartamento'])
    salvarMensagem(msg)
    return 'Testa notificação'

#cloud
@app.route('/api/notificacoes')
def obterNotificacoes():
    
    if(not os.path.exists(os.path.join(os.getcwd(),'dados.csv'))):
        df = pd.DataFrame(columns=['mensagem','status'])
        df.to_csv('dados.csv',index=False)
    
    base = pd.read_csv('dados.csv')
    mensagens = base.query('status == 0')
    dicio = mensagens.to_dict()
    
    # atualizar status
    atualizarStatus(base)
    
    if(mensagens.empty):
        return '', http.HTTPStatus.NO_CONTENT
    elif(dicio):
        print('retornando mensagens...',dicio)
        return jsonify(dicio['mensagem'][1])

# fghsfjhghlkjsf
def salvarMensagem(msg):
    if(not os.path.exists(os.path.join(os.getcwd(),'dados.csv'))):
        df = pd.DataFrame(columns=['mensagem','status'])
        df.to_csv('dados.csv',index=False)
    base = pd.read_csv('dados.csv')    
    novaMensagem = pd.DataFrame([[msg,0]], columns=['mensagem','status'])
    baseAtualizada = base.append(novaMensagem, ignore_index=True)
    baseAtualizada.to_csv('dados.csv', index=False)
    
        
def atualizarStatus(dataFrame):
    dataFrame['status'] = 1
    dataFrame.to_csv('dados.csv', index=False)