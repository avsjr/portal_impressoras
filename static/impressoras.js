document.addEventListener('DOMContentLoaded', function() {
  let btnAdicionar = document.getElementsByClassName('btn-adicionar');

  for (let button of btnAdicionar) {
    button.addEventListener('click', function() {
      let printerName = this.previousElementSibling.innerText.trim();

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
          alert('Printer added successfully.');
        } else if (response.status === 404) {
          alert('Printer not found.');
        } else {
          alert('Failed to add printer.');
        }
      })
      .catch(error => {
        alert('Error: ' + error);
      });
    });
  }
});
