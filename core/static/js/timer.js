document.querySelector('#set_clock_300').onclick = function(e){
    let user_id = $("#user_id").text();
    $.get("/user/" + user_id + "/300", function(response) {
        console.log(response);
    });
};

document.querySelector('#set_clock_1000').onclick = function(e){
    console.log("window.location.href");
    let url = location.href;
    location.replace(url + '/1000');
};
