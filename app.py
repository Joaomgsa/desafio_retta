import os 
import requests

from flask import Flask, render_template, request, redirect, url_for, flash

from services.ConvertToRoman import ConvertToRoman
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')  

@app.route('/')
def index():
    return render_template('index.html')


def validateInput(selected_option, number):
    if(selected_option == "Arábicos - Romanos"):
        if not number.isdigit():
            return "Digite um número válido"
        
    elif (selected_option == "Romanos - Arábicos"):
        if not number.isalpha():
            return "Digite um Algarismo Romano válido"
    
    return None

@app.route('/converter', methods=['POST'])
def converter():
    try:
        selected_option=request.form.get("opcoes")
        number= request.form.get("NCONVERTIDO")
        
        error = validateInput(selected_option, number)
        if error:
            flash(error, 'error')
            return redirect(url_for('index'))
        
        converter = ConvertToRoman(num=number,option = selected_option)
        result = converter.handle()
        flash(f'Resultado da conversão: {result}', 'success')
        
        
        return render_template('result.html', result = result)
    
    except Exception as e:
        return str(e)


def medals():
    api_url = os.getenv('API_BASE_URL')
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
    if response.status_code >= 300:
        return None
    
    return render_template('olympics.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7000)