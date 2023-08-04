from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__, static_url_path='', static_folder='.')

impressoras = [
    { "nome": "CSC-ADM-PRETO", "caminho": "\\\\192.0.0.61\\csc-adm-preto-ps5200s" },
    { "nome": "CSC-ADM-RASCUNHO", "caminho": "\\\\192.0.0.61\\csc-adm-rascunho-ps5200s" }
]

@app.route('/addPrinter', methods=['POST'])
def add_printer():
    data = request.json
    printer_name = data.get('printerName')

    caminho_impressora = None
    for printer in impressoras:
        if printer['nome'] == printer_name:
            caminho_impressora = printer['caminho']
            break

    if caminho_impressora is None:
        return jsonify({'error': 'Printer not found.'}), 404

    try:
        subprocess.run(['powershell', '(New-Object -ComObject WScript.Network).AddWindowsPrinterConnection("{}")'.format(caminho_impressora)], check=True)
        return jsonify({'message': 'Printer added successfully.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Failed to add printer.', 'details': str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)