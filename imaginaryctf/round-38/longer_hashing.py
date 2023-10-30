import hlextend 
from Crypto.Util.number import long_to_bytes, bytes_to_long
partial = int(input('partial p='))
gh = input('given hash=')
append = bytes_to_long(b'\x00')
sha = hlextend.new('sha256')
print(long_to_bytes(append), long_to_bytes(partial), 1024 // 8, gh)
res = sha.extend(long_to_bytes(append), long_to_bytes(partial), 1024 // 8 - len(long_to_bytes(partial)), gh)
print('msg =', bytes_to_long(res))
print('hash =', sha.hexdigest())

