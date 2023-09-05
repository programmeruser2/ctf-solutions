import pyshark 
cap = pyshark.FileCapture('cap.pcapng', display_filter='json')
#print(dir(cap[0].json))
#print(cap[1].json.value_string)
s = ''
for p in cap:
    if hasattr(p,'json') and hasattr(p.json,'value_string'):
        s += p.json.value_string 
print(s)


