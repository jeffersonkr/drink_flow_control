document.querySelector('#set_clock_300').onclick = function(e){
    let url = location.href;
    location.replace(url + '/300');

    window.onload = function(e){
        var timer = location.href.split("/").pop();
        setTimeout(closeSolenoid, parseInt(timer)*1000);
    };
    
    function closeSolenoid(){
        var site = location.href.split("/");
        var faltante = $('#qtd_faltante').text();
        site.pop();
        site = site.join("/");
        url = site + '/' + faltante;
        console.log(url);
        location.replace(url);
    };
};

document.querySelector('#set_clock_1000').onclick = function(e){
    let url = location.href;
    location.replace(url + '/1000');
};


