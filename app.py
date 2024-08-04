import os 
import plotly.express as px
import pandas as pd

from flask import Flask, render_template,render_template_string, request, redirect, url_for, flash

from services.ConvertToRoman import ConvertToRoman
from services.GenerateTreeMap import GenerateTreeMap
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

@app.route('/treemap', methods=['GET'])
def treemap():
    try:
        graph_html = GenerateTreeMap().handle()
        return render_template('treemap.html', graph_html=graph_html)
    except Exception as e:
        return f"Erro: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7000)