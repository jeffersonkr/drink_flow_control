$(".li_camera").on("click", function(){
    $(window).css("background-color","#FF0000");
    setTimeout(function(){
        $(window).css("background-color","#FFFFFF"); 
    },800);
})