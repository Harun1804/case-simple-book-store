# Panduan Instalasi App
1. Jalankan perintah dibawah ini untuk menginstall depedencies
```
pip install -r /path/to/requirements.txt 
```
2. Gunakan perintah berikut untuk melakukan migration di masing masing service
```
flask db upgrade
```
3. Gunakan perintah berikut di masing masing module
```
flask run
```