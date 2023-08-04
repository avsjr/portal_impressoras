from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/addPrinter', methods=['POST'])
def add_printer():
    data = request.get_json()
    printer_name = data.get('printerName')
    
    try:
        # Execute PowerShell script to add printer
        script = f'(New-Object -ComObject WScript.Network).AddWindowsPrinterConnection("\\\\192.0.0.61\\csc-adm-preto-sp5200s")'
        result = subprocess.run(['powershell', '-Command', script], capture_output=True, text=True, check=True)
        print(result.stdout)  # Print the output of the PowerShell script
        return jsonify({'message': 'Printer added successfully'}), 200
    except subprocess.CalledProcessError as e:
        print(e.stderr)  # Print any error message from the PowerShell script
        return jsonify({'message': 'Failed to add printer.'}), 500

    
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

@app.route('/ml_flexo')
def pl_flexo():
    return render_template('ml_flexo.html', impressoras=masterline_flexo_printers)

@app.route('/ml_emb')
def pl_emb():
    return render_template('ml_emb.html', impressoras=masterline_emb_printers)

# Define routes for other office's printer pages...

if __name__ == '__main__':
    app.run(debug=True)