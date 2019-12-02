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
    } else {
        document.querySelector('#qtd_faltante').textContent = (parseFloat($('#qtd_faltante').text()) - MilliPerSeconds.toFixed(2))
        if(timer > parseFloat($('#qtd_liquido').text())){
            console.log(MilliPerSeconds);
            if(timer <= MilliPerSeconds/2 + parseFloat($('#qtd_liquido').text())){
                var site = location.href.split("/");
                var faltante = $('#qtd_faltante').text();
                site.pop();
                site = site.join("/");
                url = site + '/update/' + faltante;
                location.replace(url);
            }
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