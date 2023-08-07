from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/addPrinter', methods=['POST'])
def add_printer():
    data = request.json
    printer_name = data.get('printerName')

    caminho_impressora = None

    # Check each printer dictionary for the given printer name
    for printer_dict in [platina_csc_printers, platina_log_printers, masterline_main_printers,
                         masterline_log_printers, masterline_flexo_printers, masterline_emb_printers]:
        if printer_name in printer_dict:
            caminho_impressora = printer_dict[printer_name]
            break

    if caminho_impressora is None:
        return jsonify({'message': 'Printer not found.'}), 404

    try:
        # Execute PowerShell script to add printer
        script = f'(New-Object -ComObject WScript.Network).AddWindowsPrinterConnection("{caminho_impressora}")'
        result = subprocess.run(['powershell', '-Command', script], capture_output=True, text=True, check=True)
        print(result.stdout)  # Print the output of the PowerShell script
        return jsonify({'message': 'Printer added successfully'}), 200
    except subprocess.CalledProcessError as e:
        print(e.stderr)  # Print any error message from the PowerShell script
        return jsonify({'message': 'Failed to add printer.'}), 500

           
# Define printer data for each office
platina_csc_printers = {
    "ADM - Frente e Verso": "\\\\192.0.0.61\\csc-adm-frenteverso-sp5200s",
    "ADM - Preto": "\\\\192.0.0.61\\csc-adm-preto-sp5200s",
    "ADM - Rascunho": "\\\\192.0.0.61\\csc-adm-rascunho-sp5200s",
    "Exportação - Frente e Verso": "\\\\192.0.0.61\csc-exportacao-frenteverso-sp377sfnwx",
    "Exportação - Preto": "\\\\192.0.0.61\\csc-exportacao-preto-sp377sf",
    "Exportação - Rascunho": "\\\\192.0.0.61\\csc-exportacao-rascunho-sp377sfnwx",
    "Comercial - Preto": "\\\\192.0.0.61\\csc-comercial-preto-sp5200s",
    "Comercial - Rascunho": "\\\\192.0.0.61\\csc-comercial-rascunho-sp5200s",
    "Marketing - A3": "\\\\192.0.0.61\\csc-mkt-a3-c368",
    "Marketing - Colorido": "\\\\192.0.0.61\\csc-mkt-colorida-c368",
    "Marketing - Frente e Verso": "\\\\192.0.0.61\\csc-mkt-frenteverso-c368",
    "Marketing - Preto": "\\\\192.0.0.61\\csc-mkt-preto-c368"
}


platina_log_printers = {
    "ADM - Colorida": "\\\\192.0.0.61\\platina-log-adc-colorida",
    "ADM - Preto": "\\\\192.0.0.61\\platina-log-adm-preto",
    "ADM - FRascunho": "\\\\192.0.0.61\\platina-log-adm-rascunho",
    "Ambulatório": "\\\\192.0.0.61\\platina-log-ambulatorio-preto-m320f",
    "Expedição - Frente e Verso": "\\\\192.0.0.61\\platina-log-exp-frenteverso-c368",
    "Expedição - Preto": "\\\\192.0.0.61\\platina-log-exp-preto-c368",
    "Expedição - Rascunho": "\\\\192.0.0.61\\platina-log-exp-rascunho-c368",
    "Expedição - Zebra": "\\\\192.0.0.61\\log-exp-zebra-zt230",
    "Recebimento": "\\\\192.0.0.61\\platina-log-rec-zgk420t",
    "Segurança - Frente e Verso": "\\\\192.0.0.61\\platina-log-seg-frenteverso-sp3710sf",
    "Segurança - Preto": "\\\\192.0.0.61\\platina-log-seg-preto-sp3710sf",
    "Segurança - Rascunho": "\\\\192.0.0.61\\platina-log-seg-rascunho-sp3710sf"
}

masterline_main_printers = {
    
}

masterline_log_printers = {
    
}

masterline_flexo_printers = {
    
}

masterline_emb_printers = {
    
}

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