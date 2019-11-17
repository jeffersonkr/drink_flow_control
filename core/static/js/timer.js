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
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        success: function(data){
            console.log("solenoide fechado")
        },
    });
};