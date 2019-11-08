function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

$('#set_clock_300').on('click', function(){
    console.log('300ml');
    setTimeout(async function(){
        home = (
            window.location.protocol + 
            "//" + window.location.host + 
            "/" + (window.location.href).split("/")[1]);
        $(".alert").show().fadeTo(3500, 0);
        await sleep(2500);
        window.location.replace(home);
    }, 10000);
    
 });

$('#set_clock_1000').on('click', function(){
    console.log('1000ml');
    setTimeout(async function(){
        home = (
            window.location.protocol + 
            "//" + window.location.host + 
            "/" + (window.location.href).split("/")[1]);
        $(".alert").show().fadeTo(3500, 0);
        await sleep(2500);
        window.location.replace(home);
    }, 5000*3.3);
 });
