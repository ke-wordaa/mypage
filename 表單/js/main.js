var no= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
$("body").ready(function () {
    $('#push').attr('disabled', true);
    $('#push').css('background-color','gray');
    $("input").on('keyup', function () {
        if($(this).val() != "")
        {
            if($('#pwd').val() === '163' && $('#um').val() != "" && $('#um').val()>=1 && $('#um').val()<=47){
                    $('#push').attr('disabled', false);
                    $('#push').css('background-color','#2691b9');
                }
            else{
                    $('#push').attr('disabled', true);
                    $('#push').css('background-color','gray');
                }
        }
        else
        {
            $('#push').attr('disabled', true);
            $('#push').css('background-color','gray');
        }
    });
    $("#push").click(function () 
    { 
        var username = $("#um").val();
        var password = $("#pwd").val();
        for (let i = 0; i <= username; i++) {
            console.log(i)
            if (username == no[i]) {
                if(password == "163")
                {
                    alert(String(no[i])+'你好')
                    window.open("../page/load.html","點餐系統",config = 'height=800,width=600')
                }
            }
        }
    });
});
function load(){
    alert("目前沒功能")
    $("button").html(String (r));
}       
    
