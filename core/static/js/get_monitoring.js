var chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/monitoring/');

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var flowPerMin = JSON.parse(data['message']);
    var flowPerSeconds = parseFloat(flowPerMin)/60;
    var last_value;
    if($('#qtd_liquidovar last_value').text != ""){
        last_value = parseFloat($('#qtd_liquido').text);
    } else {
        last_value = 0.0;
    }
    document.querySelector('#qtd_liquido').textContent = (last_value + flowPerSeconds).toString();
    //document.querySelector('#qtd_faltante').textContent = total - qtd_liquido
    //document.querySelector('#qtd_total_diario').textContent = total
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

window.onload = function(e) {
    setTimeout(setInterval(function(){
        chatSocket.send(JSON.stringify({'message': 'enviado request'}));
    }, 1000), 10000);
};