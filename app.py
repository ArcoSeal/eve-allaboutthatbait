from flask import Flask, render_template, request

disablesound = False
naughty_words = ('ozone', 'cynosural field generator')

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', status=0, disablesound=disablesound)

@app.route('/', methods=['POST'])
def checkscan():
    global disablesound
    disablesound = ('disablesound' in request.form)

    scantext = request.form['scantext']
        
    if not scantext:
        return render_template('index.html', status=0, disablesound=disablesound)
    else:
        naughtyline = checkscanresults(scantext)

        if naughtyline:
            return render_template('index.html', status=2, status_reason=naughtyline, oldscan=scantext, disablesound=disablesound)
        else:
            return render_template('index.html', status=1, oldscan=scantext, disablesound=disablesound)

def checkscanresults(scantext):
    for word in naughty_words:
        if word in scantext.lower():
            naughtyline = next((ii for ii in scantext.split('\n') if word in ii.lower()))
            return naughtyline

    return None

if __name__ == '__main__':
    app.run()