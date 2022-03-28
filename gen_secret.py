import pyotp

print(f"SECRET: {pyotp.random_base32()}")