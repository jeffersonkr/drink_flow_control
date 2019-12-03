var chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/monitoring/');

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var flowPerMin = JSON.parse(data['message']);
    var MilliPerSeconds = (parseFloat(flowPerMin)*16.67);
    var last_value;
    var timer = location.href.split("/").pop();
    console.log($('#qtd_liquido').text())
    if($('#qtd_liquido').text() == ""){
        last_value = 0.0;
    } else {
        last_value = parseFloat($('#qtd_liquido').text());
    }
    document.querySelector('#qtd_liquido').textContent = ((last_value + MilliPerSeconds).toFixed(2)).toString();
    if(parseFloat($('#qtd_faltante').text()) - parseFloat($('#qtd_liquido').text()) < 0){
        document.querySelector('#qtd_faltante').textContent = 0.0
        var site = location.href.split("/");
        var faltante = $('#qtd_faltante').text();
        site.pop();
        site = site.join("/");
        url = site + '/update/' + faltante;
        location.replace(url);
    } else {
        document.querySelector('#qtd_faltante').textContent = (parseFloat($('#qtd_faltante').text()) - MilliPerSeconds.toFixed(2))
        if(parseFloat(timer) > parseFloat($('#qtd_liquido').text()) && parseFloat($('#qtd_faltante').text()) > 0 ){
            console.log(MilliPerSeconds);
            if(MilliPerSeconds < 50){
                if(parseFloat(timer) <= 1.2*MilliPerSeconds.toFixed(2) + parseFloat($('#qtd_liquido').text())){
                    var site = location.href.split("/");
                    var faltante = $('#qtd_faltante').text();
                    site.pop();
                    site = site.join("/");
                    url = site + '/update/' + faltante;
                    location.replace(url);
                }
            } else if(MilliPerSeconds < 100 && MilliPerSeconds > 50){
                if(parseFloat(timer) <= MilliPerSeconds.toFixed(2)/2 + parseFloat($('#qtd_liquido').text())){
                    var site = location.href.split("/");
                    var faltante = $('#qtd_faltante').text();
                    site.pop();
                    site = site.join("/");
                    url = site + '/update/' + faltante;
                    location.replace(url);
                }
            } else if(MilliPerSeconds < 150 && MilliPerSeconds > 100){
                if(parseFloat(timer) <= MilliPerSeconds.toFixed(2)/1.5 + parseFloat($('#qtd_liquido').text())){
                    var site = location.href.split("/");
                    var faltante = $('#qtd_faltante').text();
                    site.pop();
                    site = site.join("/");
                    url = site + '/update/' + faltante;
                    location.replace(url);
                }
            }
            
        } else if(parseFloat(timer) <= parseFloat($('#qtd_liquido').text())){
            var site = location.href.split("/");
            var faltante = $('#qtd_faltante').text();
            site.pop();
            site = site.join("/");
            url = site + '/update/' + faltante;
            location.replace(url);
        } else if(parseFloat($('#qtd_faltante').text()) == 0) {
            var site = location.href.split("/");
            var faltante = $('#qtd_faltante').text();
            site.pop();
            site = site.join("/");
            url = site + '/update/' + faltante;
            location.replace(url);
        }
    };
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

window.onload = function(e) {
    setInterval(function(){
        chatSocket.send(JSON.stringify({'message': 'enviado request'}));
    }, 1000);
};