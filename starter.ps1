# definição de varialves para facil manuseio
$app_url = "https://github.com/EzequielS4ntos/util-commands/archive/heads/main.zip"
$zip_dir = "$env:TEMP\app.zip"
$app_dir = "$env:TEMP\app"

# se existir o path, remova-o
if(Test-Path $zip_dir){Remove-Item $zip_dir} 
if(Test-Path $app_dir){Remove-Item $app_dir} 

# Requisição HTTP -arquivo de destino
Invoke-RestMethod $app_url -OutFile $zip_dir

# Extrai o zip para o path de destino
Expand-Archive -Path $zip_dir -DestinationPath $app_dir -Force

python "$app_dir\util-commands-heads-main\main.py"