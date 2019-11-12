document.querySelector('#set_clock_300').onclick = function(e){
    let user_code = window.location.href.split('/')[-1];
    $.get("/user/" + user_code + "/300", function(response) {
        console.log(response);
    });
};

document.querySelector('#set_clock_1000').onclick = function(e){
    let user_code = window.location.href.split('/')[-1];
    $.get("/user/" + user_code + "/1000", function(response) {
        console.log(response);
    });
};
