document.addEventListener('DOMContentLoaded', function () {
    $(window).on('load resize',function(){
        var count;
        $('.text_limit').each(function() {
            var thisText = $(this).text();
            var textLength = thisText.length;
            if(800<=$(window).width()){
                count = 25;
                if (textLength > count) {
                    var showText = thisText.substring(0, count);
                    var insertText = showText += '....';
                    $(this).html(insertText);
                };
            }else{
                count = 10;
                if (textLength > count) {
                    var showText = thisText.substring(0, count);
                    var insertText = showText += '....';
                    $(this).html(insertText);
                };
            }
        });
    });
});