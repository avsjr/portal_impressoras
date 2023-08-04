document.addEventListener('DOMContentLoaded', function() {
  // Botão de adicionar impressora
  let btnAdicionar = document.getElementsByClassName('btn-adicionar');

  // Evento de clique no botão de adicionar impressora
  // Using for-of loop
  for (const btn of btnAdicionar) {
  btn.addEventListener('click', function() {
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
