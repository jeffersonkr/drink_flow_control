$('#set_clock_300').on('click', function(){
    console.log('300ml');
    setTimeout(function(){
        home = (
            window.location.protocol + 
            "//" + window.location.host + 
            "/" + (window.location.href).split("/")[1]);
        window.location.replace(home);
    }, 10000);
 });

$('#set_clock_1000').on('click', function(){
    console.log('1000ml');
    setTimeout(function(){
        home = (
            window.location.protocol + 
            "//" + window.location.host + 
            "/" + (window.location.href).split("/")[1]);
        window.location.replace(home);
    }, 5000*3.3);
 });