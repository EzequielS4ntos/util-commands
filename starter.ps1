# definição de varialves para facil manuseio
$app_url = "https://github.com/EzequielS4ntos/util-commands/app.zip"
$zip_dir = "$env:TEMP\app.zip"
$app_dir = "$env:TEMP\app"

# Requisição HTTP -arquivo de destino
Invoke-RestMethod $app_url -OutFile $zip_dir

# se existir o path, remova-o
if(Test-Path $zip_dir){Remove-Item $zip_dir} 

# cria o novo diretório zip | só para não exibir nada na tela
New-Item -ItemType File -Path $zip_dir | Out-Null

# Extrai o zip para o path de destino
Expand-Archive -Path $zip_dir -DestinationPath $app_dir -Force

python "$app_dir\main.py"