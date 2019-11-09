$(".li_camera").on("click", function(){
    $('#shutter').addClass('on');
    setTimeout(function() {
        $('#shutter').removeClass('on');
    }, 30*2+45);/* Shutter speed (double & add 45) */
})


