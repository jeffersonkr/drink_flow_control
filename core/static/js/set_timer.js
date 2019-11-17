window.onload = function(e){
    var timer = location.href.split("/").pop();
    setTimeout(
        function closeSolenoid(){
            var site = location.href.split("/");
            var faltante = $('#qtd_faltante').text();
            site.pop();
            site = site.join("/");
            url = site + '/' + faltante;
            console.log(url);
            location.replace(url);
        }, parseInt(timer)*1000);
};

