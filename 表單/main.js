var no= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
let r =false

$("body").ready(function () {
    $('#push').css('background-color','gray');
    Text_um = '帳號名稱(座號)'
    $("#um").on('keyup', function () {
        var t = $(this).val().length
        if($(this).val() != ""){
            $('#le').html('輸入字數:'+ `${t}`);
            $('#push').css('background-color','#2691b9');
        }
        else{
            console.log(Text_um)
            $('#le').html(Text_um);
            $('#push').attr('disabled', true);
            $('#push').css('background-color','gray');

        }
    });
    $("#push").click(function () 
    { 
        alert("a")
        var username = $("#um").val();
        var password = $("#pwd").val();
        console.log(password)
        
        for (let i = 0; i <= username; i++) {
            console.log(i)
            if (username == no[i]) {
                if(password == "163")
                {
                    r=true
                    alert(String(no[i])+'你好')
                    window.open("./load.html","點餐系統",config = 'height=800,width=600')
                }
                else
                {
                    alert("密碼錯誤!")
                    break
                }
            }
        }
    });
});

function load(){
    
    alert("目前沒功能")
    $("button").html(String (r));
}   
    
