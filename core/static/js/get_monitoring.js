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
};

document.querySelector('#set_clock_300').onclick = function(e) {
    setTimeout(setInterval(function(){
        chatSocket.send(JSON.stringify({'message': 'enviado request'}));
    }, 1000), 10000);
    let user_code = location.href.split('/')[-1]
    $.get("/user/" + user_code + "/OK", function(response) {
        alert(response);
    });
};

document.querySelector('#set_clock_1000').onclick = function(e) {
    setTimeout(setInterval(function(){
        chatSocket.send(JSON.stringify({'message': 'enviado request'}));
    }, 1000), 60000);
    let user_code = location.href.split('/')[-1]
    $.get("/user/" + user_code + "/OK", function(response) {
        alert(response);
    });
};