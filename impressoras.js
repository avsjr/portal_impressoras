// Defina uma lista de impressoras com seus respectivos caminhos
var impressoras = [
    { nome: "Impressora do Setor A", caminho: "\\\\Printserver01\\ImpressoraSetorA" },
    { nome: "Impressora do Setor B", caminho: "\\\\Printserver01\\ImpressoraSetorB" },
    { nome: "Impressora do Setor C", caminho: "\\\\Printserver02\\ImpressoraSetorC" },
    // Adicione mais impressoras aqui conforme necessário
];

  
  // Função para adicionar a impressora
  function adicionarImpressora(caminhoImpressora) {
    var shell = new ActiveXObject("WScript.Shell");
    shell.Run('(New-Object -ComObject WScript.Network).AddWindowsPrinterConnection("' + caminhoImpressora + '")', 0, true);
  }
  