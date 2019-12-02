$(document).ready(function(){
    var timer = location.href.split("/").pop();
    console.log(timer);
    setTimeout(
        function closeSolenoid(){
            var site = location.href.split("/");
            var faltante = $('#qtd_faltante').text();
            site.pop();
            site = site.join("/");
            url = site + '/update/' + faltante;
            location.replace(url);
        }, parseInt(timer)*50);
});

