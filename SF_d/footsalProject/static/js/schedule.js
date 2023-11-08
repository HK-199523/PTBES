//下記でテンプレート内
const eventData = JSON.parse(document.getElementById("event-data").textContent);
console.log(eventData)
//下記でunicodeをデコードする。
//でもjson.dumpsでできたので意味ないけど直すのめんどいのでこのまま行く
const Uchenge = $.parseJSON(eventData)
var today = new Date;
var today_format = today.getFullYear()+"-"+today.getDate()+"-"+today.getDate()
let finalEvent = [];
for(var i = 0;i < Uchenge.length;i++){
    let final = {
        id:Uchenge[i].id,
        title:Uchenge[i].title,
        start:Uchenge[i].start_date,
        end:Uchenge[i].end_date,
        color:Uchenge[i].color
    }
    finalEvent.push(final);
}

document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.querySelector('.calendar');
    const calendar = new FullCalendar.Calendar(calendarEl, {
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
        },
        navLinks: true,
        businessHours: true,
        editable: true,
        locale: 'ja',
        buttonText: {
            prev:     '前月',
            next:     '次月',
            today:    '今日',
            month:    '月',
            week:     '週',
            day:      '日',
            list:     '予定リスト'
        },
        events: finalEvent,
        eventDidMount: function(info) {
            console.log(info.event.description);
        },
        eventClick:function(info){
            var category,content,StartTime,EndTime;
            for(var i = 0;i < Uchenge.length;i++){
                if(info.event.id==Uchenge[i].id){
                    category = Uchenge[i].period;
                    content = f_con_list[i];
                    StartTime = Uchenge[i].start_time;
                    EndTime = Uchenge[i].end_time;
                    break;
                }
            }
            $('#modalTerm').html(info.event.title); // モーダルのタイトルをセット
            $('#startTimezone').html(StartTime);
            $('#endTimezone').html(EndTime);
            $('#detilCategry').html(category);
            $('#modalBody').html(content); // モーダルの本文をセット
            $('#modalArea').fadeIn(); // モーダル着火
        }
    });
    calendar.render();

    $('#closeModal , #modalBg').click(function(){
        $('#modalArea').fadeOut();
    });
});

//下記はモーダルの
