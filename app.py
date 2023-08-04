from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__, static_url_path='', static_folder='static')

# Define printer data for each office
platina_csc_printers = [
    { "nome": "ADM - Frente e Verso", "caminho": "\\192.0.0.61\\csc-adm-frenteverso-sp5200s" },
    { "nome": "ADM - Preto", "caminho": "\\192.0.0.61\\csc-adm-preto-sp5200s" },
    { "nome": "ADM - Rascunho", "caminho": "\\192.0.0.61\\csc-adm-rascunho-sp5200s" },
    { "nome": "Comercial - Preto", "caminho": "\\192.0.0.61\\csc-comercial-preto-sp5200s" },
    { "nome": "Comercial - Rascunho", "caminho": "\\192.0.0.61\\csc-comercial-rascunho-sp5200s" },
    { "nome": "Exportação - Frente e Verso ", "caminho": "\\192.0.0.61\\csc-exportacao-frenteverso-sp377sfnwx" },
    { "nome": "Exportação - Preto", "caminho": "\\192.0.0.61\\csc-exportacão-preto-sp377sf" },
    { "nome": "Exportação - Rascunho", "caminho": "\\192.0.0.61\\csc-exportacao-rascunho-sp377sfnwx" },
    { "nome": "Marketing - A3 ", "caminho": "\\192.0.0.61\\csc-mkt-a3-c368" },
    { "nome": "Marketing - Colorida", "caminho": "\\192.0.0.61\\csc-mkt-colorida-c368" },
    { "nome": "Marketing - Frente e Verso", "caminho": "\\192.0.0.61\\esc-mkt-frenteverso-c368" },
    { "nome": "Marketing - Preto", "caminho": "\\192.0.0.61\\esc-mkt-preto-c368" },
]

platina_log_printers = [
    
]

masterline_main_printers = [
    
]

masterline_log_printers = [
    
]

masterline_flexo_printers = [
    
]

masterline_emb_printers = [
    
]

# Define routes for each office's printer page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pl_csc')
def pl_csc():
    return render_template('pl_csc.html', impressoras=platina_csc_printers)

@app.route('/pl_log')
def pl_log():
    return render_template('pl_log.html', impressoras=platina_log_printers)

@app.route('/ml_main')
def ml_main():
    return render_template('ml_main.html', impressoras=masterline_main_printers)

@app.route('/ml_log')
def ml_log():
    return render_template('ml_log.html', impressoras=masterline_log_printers)

@app.route('/pl_flexo')
def pl_flexo():
    return render_template('pl_flexo.html', impressoras=masterline_flexo_printers)

@app.route('/pl_emb')
def pl_emb():
    return render_template('pl_emb.html', impressoras=masterline_emb_printers)

# Define routes for other office's printer pages...

if __name__ == '__main__':
    app.run(debug=True)