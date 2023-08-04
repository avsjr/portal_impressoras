import subprocess
from flask import Flask, request, jsonify, render_template

# ... your printer data and other routes ...

@app.route('/addPrinter', methods=['POST'])
def add_printer():
    data = request.get_json()
    printer_name = data.get('printerName')

    # Define a dictionary to map printer names to their corresponding paths
    printer_paths = {
        "ADM - Frente e Verso": "\\192.0.0.61\\csc-adm-frenteverso-sp5200s",
        "ADM - Preto": "\\192.0.0.61\\csc-adm-preto-sp5200s",
        "ADM - Rascunho": "\\192.0.0.61\\csc-adm-rascunho-sp5200s",
        # Add more printer mappings here...
    }

    try:
        # Get the printer path based on the selected printer name
        printer_path = printer_paths.get(printer_name)
        if not printer_path:
            return jsonify({'message': 'Printer not found.'}), 404

        # Execute PowerShell script to add the selected printer
        script = f'(New-Object -ComObject WScript.Network).AddWindowsPrinterConnection("{printer_path}")'
        result = subprocess.run(['powershell', '-Command', script], capture_output=True, text=True, check=True)
        print(result.stdout)  # Print the output of the PowerShell script
        return jsonify({'message': 'Printer added successfully'}), 200
    except subprocess.CalledProcessError as e:
        print(e.stderr)  # Print any error message from the PowerShell script
        return jsonify({'message': 'Failed to add printer.'}), 500

# ... rest of your code ...
