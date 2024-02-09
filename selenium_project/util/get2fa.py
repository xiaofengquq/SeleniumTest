import pyotp

key = 'FHZ6HYMZZ7OVCCBJ4NPOQJS4OAHFOLTX'
totp = pyotp.TOTP(key)
print(totp.now())

