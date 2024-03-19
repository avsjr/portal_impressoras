import win32print
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path='', static_folder='static')

def adicionar_impressora(printer_path):
    try:
        win32print.AddPrinterConnection(printer_path)
        print("Impressora adicionada com sucesso!")
        return jsonify({'message': 'Impressora adicionada com sucesso'}), 200
    except Exception as e:
        print(f"Erro ao adicionar a impressora: {e}")
        return jsonify({'message': f'Erro ao adicionar a impressora: {e}'}, 500)

@app.route('/adicionarImpressora', methods=['POST'])
def add_printer_route():
    data = request.json
    printer_name = data.get('printerName')
    caminho_impressora = None

    for printer_dict in [platina_csc_printers,
                        platina_log_printers,
                        masterline_main_printers,
                        masterline_log_printers,
                        masterline_flexo_printers,
                        masterline_emb_printers]:
        if printer_name in printer_dict:
            caminho_impressora = printer_dict[printer_name]
            break
    if caminho_impressora is None:
        return jsonify({'message': 'Printer not found'}), 404

    print(f"Trying to add printer: {caminho_impressora}")
    
    try:
        adicionar_impressora(caminho_impressora)
        print("Impressora adicionada com sucesso!")
        return jsonify({'message': 'Impressora adicionada com sucesso'}), 200
    except win32print.error as e:
        print(f"Erro ao adicionar a impressora: {e}")
        return jsonify({'message': f'Erro ao adicionar a impressora: {e}'}, 500)

platina_csc_printers = {
    "PL CSC ADM": "\\\\192.0.0.61\\csc-adm-preto-sp5200s",
    "Exportação": "\\\\192.0.0.61\\csc-exportacao-preto-sp377sf",
    "Comercial": "\\\\192.0.0.61\\csc-comercial-preto-sp5200s",
    "Marketing": "\\\\192.0.0.61\\csc-mkt-preto-c368",
    "Financeiro": "\\\\192.0.0.61\\csc-financeiro-1102w"
}
platina_log_printers = {
    "PL LOG ADM": "\\\\192.0.0.61\\platina-log-adm-preto",
    "Ambulatório": "\\\\192.0.0.61\\platina-log-ambulatorio-preto-m320f",
    "Expedição": "\\\\192.0.0.61\\platina-log-exp-preto-c368",
    "Expedição Zebra": "\\\\192.0.0.61\\log-exp-zebra-zt230",
    "Portaria Zebra": "\\\\192.0.0.61\\platina-log-rec-zgk420t",
    "Segurança": "\\\\192.0.0.61\\platina-log-seg-preto-sp3710sf"
}
masterline_main_printers = {
    "MLN ADM": "\\\\192.0.0.61\\mln-adm-a3-mpc3503",
    "Almoxarifado Pigmento - Sankhya": "\\\\192.0.0.61\\mln-almoxpigmento-sankhya-zebrazm400",
    "Almoxarifado Quimico": "\\\\192.0.0.61\\mln-almoxquimica-preto-brother8157",
    "Almoxarifado Quimico - Etiquetas": "\\\\192.0.0.61\\mln-almoxquimica-etiquetas-zebrazm400",
    "Almoxarifado Rótulos": "\\\\192.0.0.61\\mln-almoxrotulos-preto-b400v4ps",
    "Almoxarifado Rótulos - Sankhya": "\\\\192.0.0.61\\mln-almoxrotulos-sankhya-zebrazt410",
    "Ambulatório": "\\\\192.0.0.61\\mln-ambulatorio-preto-sp5210sf",
    "RH": "\\\\192.0.0.61\\mln-dp-preto-mpc3003",
    "Envase": "\\\\192.0.0.61\\mln-envase-preto-sp5200s",
    "Etiquetas Corpore01": "\\\\192.0.0.61\\mln-etiquetas-corpore01-zebrazt410",
    "Etiquetas Corpore02": "\\\\192.0.0.61\\mln-etiquetas-corpore02-zebrazt410",
    "Etiquetas Corpore03": "\\\\192.0.0.61\\mln-etiquetas-corpore03-zebrazt410",
    "Etiquetas Corpore05": "\\\\192.0.0.61\\mln-etiquetas-corporeO5-zebrazt411",
    "Etiquetas Corpore06": "\\\\192.0.0.61\\mln-etiquetas-corpore06-zebrazt411",
    "Etiquetas Corpore07": "\\\\192.0.0.61\\mln-etiquetas-corpore07-zebrazt411",
    "Fisico Quimico - Sankhya": "\\\\192.0.0.61\\mln-fisicoquimico-sankhyal-zebrazt411",
    "Manutenção": "\\\\192.0.0.61\\mln-manutencao-preto-sp5210sf",
    "P&D": "\\\\192.0.0.61\\mln-ped-preto-mpc3003",
    "Pesagem": "\\\\192.0.0.61\\mln-presagem-preto-sp4510sf",
    "Pesagem - Sankhya01": "\\\\192.0.0.61\\mln-pesagem-sankhya-zebras4m",
    "Pesagem - Sankhya02": "\\\\192.0.0.61\\mln-pesagem-sankhya-zebrazt410"
}
masterline_log_printers = {
    "MLN LOG ADM": "\\\\192.0.0.61\\mln-log-g2-preto-sp377sfwx",
    "MLN LOG ADM - Sankhya": "\\\\192.0.0.61\\mln-log-g2-zebra-gk420t",
    "MLN LOG Estoque": "\\\\192.0.0.61\\mln-log-estoque-preto-sp5210sf",
    "MLN LOG Estoque - Sankhya": "\\\\192.0.0.61\\mln-log-estoque-sankhya-gk420t"
}
masterline_emb_printers = {
    "MLN EMB ADM": "\\\\192.0.0.61\\mln-embalagem-preto-sp5200s",
    "MLN EMB - Sankhya": "\\\\192.0.0.61\\mln-emabalagem-sankhya-zebrazm400"
}
masterline_flexo_printers = {}

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

if __name__ == '__main__':
    app.run(debug=True)
