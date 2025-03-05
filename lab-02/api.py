from flask import Flask , request , jsonify
from cipher.caesar.caesar_cipher import CaesarCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
@ap.route("/api/caesar/encrypt",methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text =data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypted_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@ap.route("/api/caesar/encrypt",methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text =data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypted_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

    #main function
    if __name__ == "main":
        app.run(host="0.0.0.0", port=5000, debug=True)

