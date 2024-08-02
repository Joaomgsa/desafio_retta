from flask import Flask, render_template, request, redirect, url_for, session

from services.ConvertToRoman import ConvertToRoman

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter', methods=['POST'])
def converter():
    try:
        selected_option=request.form.get("opcoes")
        number= request.form.get("number")
        
        result = ConvertToRoman(selected_option, number)
        return render_template('result.html', result = result)
    
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7000)