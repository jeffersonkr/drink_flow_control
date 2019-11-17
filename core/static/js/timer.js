window.onload = function(e){
    var timer = location.href.split("/").pop();
    setTimeout(closeSolenoid, parseInt(timer)*1000);
};

function closeSolenoid(){
    site = location.href.split("/");
    site.pop();
    site = site.join("/");
    url = site + '/' + faltante;
    console.log(url);
    $.get(url);
};