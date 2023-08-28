document.addEventListener('DOMContentLoaded', function() {
  let btnAdicionar = document.getElementsByClassName('btn-adicionar');

  for (let button of btnAdicionar) {
    button.addEventListener('click', function() {
      let printerName = this.closest('.impressora').querySelector('.printer-name').innerText.trim();
      console.log('Printer name:', printerName); // Log the printer name

      // Make a POST request to the Python server to add the printer
      fetch('/addPrinter', {
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
    });
  }
});
