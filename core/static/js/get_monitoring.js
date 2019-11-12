mac_address = $('select[id=select_mac]').val()

var chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/monitoring/');

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = JSON.parse(data['message']);
    document.querySelector('#qtd_liquido').textContent = message[''];
    document.querySelector('#qtd_faltante').textContent = total - qtd_liquido
    document.querySelector('#qtd_total_diario').textContent = total
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
    fechar o calculo enviar qtd faltante pra banco
};

document.querySelector('#button_go').onclick = function(e) {
    setInterval(function(){
        chatSocket.send(JSON.stringify({'message': 'enviado request'}));
    }, 1000);
};