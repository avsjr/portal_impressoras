console.log('Script loaded successfully');

document.addEventListener('DOMContentLoaded', function () {
    function adicionarImpressora(printerName) {
        console.log('Printer name:', printerName); // Log the printer name

        // Make a POST request to the Python server to add the printer
        fetch('/adicionarImpressora', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'printerName': printerName })
        })
            .then(response => {
                if (response.ok) {
                    console.log('Printer added successfully'); // Log success message
                    alert('Impressora adicionada com sucesso!');
                } else if (response.status === 404) {
                    console.log('Printer not found'); // Log not found message
                    alert('Impressora não encontrada.');
                } else {
                    console.log('Failed to add printer.'); // Log failure message
                    alert('Não foi possível adicionar a impressora.');
                }
            })
            .catch(error => {
                console.error('Error:', error); // Log error message
                alert('Error: ' + error);
            });
    }

    let btnAdicionar = document.querySelectorAll('.btn-adicionar');

    btnAdicionar.forEach(button => {
        button.addEventListener('click', function () {
            let printerName = this.parentElement.querySelector('.printer-name').innerText.trim();
            adicionarImpressora(printerName);
        }, { once: true });
    });
});