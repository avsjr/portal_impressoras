$PrinterPath = "\\192.0.0.61\csc-adm-rascunho-sp5200s"
$printer = (New-Object -ComObject WScript.Network)

# Tenta adicionar a impressora
$success = $printer.AddWindowsPrinterConnection($PrinterPath)

if ($success) {
    Write-Host "Impressora instalada com sucesso: $PrinterPath"
} else {
    Write-Host "Erro ao instalar a impressora: $PrinterPath"
}
