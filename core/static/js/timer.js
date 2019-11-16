var timer = location.href;
time = timer.split("/")[this.length - 1];
console.log(time);

window.onload = function(e){
    setTimeout(closeSolenoid, parseInt(time)*1000);
};

function closeSolenoid(){
    site = location.href.split("/").pop().join("/");
    faltante = parseFloat($("#qtd_faltante").text());
    url = site + '/' + faltante;
    console.log(url);
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        success: function(data){
            console.log("solenoide fechado")
        },
    });
};