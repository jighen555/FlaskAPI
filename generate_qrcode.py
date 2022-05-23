from flask import Flask, request
import json
import qrcode
import string
import random

app = Flask(__name__)


@app.post('/generateQRCode')
def generate_qr_code():
    try:
        data = request.json
        url = data['url']
        img = qrcode.make(url)
        qr_name = ''.join((random.choice(string.ascii_lowercase) for x in range(20)))
        img.save(qr_name + ".jpg")
        description = 'E stato generato il QRCode correttamente con nome ' + qr_name
        return json.dumps({'Result': 'OK', 'Description': description})
    except:
        description = 'Errore durante la generazione del QRCode '
        return json.dumps({'Result': 'KO', 'Description': description})


if __name__ == '__main__':
    app.run()
