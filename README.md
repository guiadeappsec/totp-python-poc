# totp-python-poc

How to integrate MFA into your application using authenticator apps and python.

## Setup

* Requirement: Python 3
* `python3 -m venv .venv`
* `pip install -r requirements.txt`

## PoC

The `gen_secret.py` contains the code to generate secret / seed.

The `generator.py` contains the code to generate the QRCode to scan with the authenticator app.

The `validator.py` contains the code to validate a token provided by the authenticator app.


## Notes

* This code works with Microsoft Authenticator and Authy.
* Unfortuantely, the code does not work with Google Authenticator.