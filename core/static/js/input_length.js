$(".one_number").keydown(function(){
    if (this.value.length == this.maxLength) {
        $(this).next('.one_number').focus();
    }
});