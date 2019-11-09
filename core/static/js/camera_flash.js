$(".li_camera").on("click", function(){
    this.css("background-color","#FF0000");
    setTimeout(function(){
        this.css("background-color","#FFFFFF"); 
    },800);
})