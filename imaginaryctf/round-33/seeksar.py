alphabet = bytes(range(32, 127))
enc = b"M'HG\\BOE@CZ@QPQVMBS@EFNBOE@*@NFBO@RVBTBSgT@EFNBOE@xEpEsyqG^"
key = bytearray(len(enc))
partial = b'ictf{'
orig = 0
for i, c in enumerate(enc):
    if i >= len(partial): break
    offset = (alphabet.find(c) - partial[i]) % len(alphabet)
    key[orig] = offset
    orig = offset
print(key, orig)
