$(function(){
	console.log("{{news}}");
	/*This code is js code for respnsive-sideber below.*/
	var
	  winW = $(window).width(),
		winH = $(window).height(),
		nav = $('#mainnav ul a'),
		curPos = $(this).scrollTop();
        baseW = 800
	if (winW > 800){
		var headerH =0;
	}
	else{
		var headerH =70;
	}
	
	
	$('.panel').hide();
	$('#menuWrap').toggle(function(){
		$(this).next().slideToggle();
		$('#menuBtn').toggleClass('close');
	},
	function(){
		$(this).next().slideToggle();
		$('#menuBtn').removeClass('close');
	});

    /*This code is js code for dropdown-list below.*/
    
    $('.kari').on('click',function(event){
        $(event.target).siblings().slideToggle(500);
    });

    /*This code is js code for dropdown-list below.*/
    
    $(window).on('load resize',function(){
        if(1000<=$(window).width()){
			$('#classList1,#classList2,#classList3,#classList4,#classList5,#classList6').addClass('col-2');
			$('#mainDiv').addClass('container');
			$('.rowChild').addClass('col-3');
			$('.rowChild').removeClass('col-4');
		}else if(800<=$(window).width() && $(window).width()<1000){
			$('#classList1,#classList2,#classList3,#classList4,#classList5,#classList6').addClass('col-2');
			$('.rowChild').removeClass('col-3');
			$('.rowChild').addClass('col-4');
		}else{
            $('#classList1,#classList2,#classList3,#classList4,#classList5,#classList6').removeClass('col-2');
			$('#mainDiv').removeClass('container');
			$('.rowChild').removeClass('col-4');
			
        }
    });

	/*This is js code for limiting word length*/
	var count = 10;
	$('.text_limit').each(function() {
		var thisText = $(this).text();
		 var textLength = thisText.length;
		  if (textLength > count) {
			 var showText = thisText.substring(0, count);
			 var insertText = showText += '…';
			 $(this).html(insertText);
		 };
	 });

	 /*This is js code for getting practice field at googlemap and change field.*/
	 $('#kashiwai').on('click',function(){
		$('#accessBody div p').html('〒272-0802<br>千葉県市川市柏井町１丁目１１４９−１');
		$('#changeMap input').attr('class','btn btn-dark');
		$('#kashiwai').attr('class','btn nowBtn');
		$('#googlemapAll').attr('src','https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3851.2000549541185!2d139.96610031704492!3d35.739489029246855!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188110160e0d3b%3A0x4143fc6837d6cfdb!2z5biC5bed5biC56uL5p-P5LqV5bCP5a2m5qCh!5e0!3m2!1sja!2sjp!4v1656601474064!5m2!1sja!2sjp');
	});
	 $('#funabashi').on('click',function(){
		$('#accessBody div p').html('〒273-0866<br>千葉県船橋市夏見台６丁目４−１');
		$('#changeMap input').attr('class','btn btn-dark');
		$('#funabashi').attr('class','btn nowBtn');
		$('#googlemapAll').attr('src','https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d18322.172944870603!2d139.99288018618952!3d35.727861739275234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1z6Ii55qmL5biC6YGL5YuV5YWs5ZySIOS9k-iCsumkqA!5e0!3m2!1sja!2sjp!4v1656599328198!5m2!1sja!2sjp');
	});
	 $('#konodai').on('click',function(){
		$('#accessBody div p').html('〒272-0827<br>千葉県市川市国府台１丁目６−４');
		$('#changeMap input').attr('class','btn btn-dark');
		$('#konodai').attr('class','btn nowBtn');
		$('#googlemapAll').attr('src','https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d12953.102557126133!2d139.90130542699455!3d35.7440292908008!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1z5Zu95bqc5Y-w5L2T6IKy6aSo!5e0!3m2!1sja!2sjp!4v1656599414697!5m2!1sja!2sjp"');
	});
	 $('#tobu').on('click',function(){
		$('#accessBody div p').html('〒270-2222<br>千葉県松戸市高塚新田４２７');
		$('#changeMap input').attr('class','btn btn-dark');
		$('#tobu').attr('class','btn nowBtn');
		$('#googlemapAll').attr('src','https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5444.718530078881!2d139.9340764644631!3d35.764345328691114!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601883f8260889cd%3A0x633c24c49526bc36!2z5p2-5oi45biC5p2x6YOo44K544Od44O844OE44OR44O844Kv5L2T6IKy6aSo!5e0!3m2!1sja!2sjp!4v1656599486832!5m2!1sja!2sjp');
	});
	 $('#ichikawa').on('click',function(){
		$('#accessBody div p').html('〒272-0127<br>千葉県市川市塩浜４丁目９−１');
		$('#changeMap input').attr('class','btn btn-dark');
		$('#ichikawa').attr('class','btn nowBtn');
		$('#googlemapAll').attr('src','https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11890.566320761283!2d139.91438683858672!3d35.660042380322366!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60187d92ef2c18e7%3A0x4492e15924e85026!2z5aGp5rWc5biC5rCR5L2T6IKy6aSo!5e0!3m2!1sja!2sjp!4v1656599566475!5m2!1sja!2sjp');
	});

	/*This is js code for indicating SNS logo by scrolling place.*/
	$(window).scroll(function(){
        if(800>=$(window).scrollTop()){
            $("#snsLink").attr('class','logoNone')
        }else{
			$('#snsLink').attr('class','')
        }
    });
});

