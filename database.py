from flask import Flask
import json
jsonfileread=''
with open('storage.json','r') as f:
    jsonfileread=json.load(f)
app=Flask(__name__)
@app.route('/colorsearch<color>')
def home(color):
    try:
        return f'{jsonfileread[f"{color}"]}'
    except KeyError:
        return 'err'
@app.route('/<addclr>&<clrcode>')
def addcolor(addclr, clrcode):
    nextthing=f'"{clrcode}"'
    thingtoadd=f'"{addclr}":{nextthing}'
    with open('storage.json','r')as f:
        jsonfileread=f.read()
    with open('storage.json','w')as f:
        thing=thingtoadd.strip('{').strip('}')
        char='}'
        f.write(f'{jsonfileread[0:-1]},\n{thing}\n{char}')
        print('added')
    return 'added color!'
if __name__=="__main__":
    app.run()