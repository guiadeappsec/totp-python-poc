# pip install pyotp
import pyotp

# pip install qrcode[pil]
# macos: pip install qrcode"[pil]"
import qrcode

ISSUER = "MyCompany" # nome da empresa / produto
USER_ID = "myuser@email.com" # identificador do usuário
SECRET = "4Y5UDG35KNJMYYQDOIML32WUH3ML5EZE" # chave secreta do usuário

uri = pyotp.totp.TOTP(SECRET).provisioning_uri(name=USER_ID, issuer_name=ISSUER)
print(f"URI: {uri}")

img = qrcode.make(uri)
img.save("qrcode.png")
print("QRCode saved to qrcode.png")


