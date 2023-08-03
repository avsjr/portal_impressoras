document.addEventListener('DOMContentLoaded', function() {
    // Botão de adicionar impressora
    var btnAdicionar = document.getElementById('adicionar-impressora');

    // Evento de clique no botão de adicionar impressora
    btnAdicionar.addEventListener('click', function() {
        var printerPath = "\\\\Printserver01\\Xerox5"; // Altere o caminho da impressora conforme necessário
        var shell = new ActiveXObject("WScript.Shell");

        // Executa o comando de adição da impressora
        shell.Run('(New-Object -ComObject WScript.Network).AddWindowsPrinterConnection("' + printerPath + '")', 0, true);
    });
});
