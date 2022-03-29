# pip install pyotp
import pyotp

SECRET = "4Y5UDG35KNJMYYQDOIML32WUH3ML5EZE" # chave secreta do usuário

totp = pyotp.TOTP(SECRET)

code = input("Code: ")

print(f"Code Valid: {totp.verify(code)}")

