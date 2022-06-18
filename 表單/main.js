function a() {
    let username = Number(document.getElementById("um").value)
    let password = document.getElementById("pwd").value
    var no= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    for (let i = 0; i <= username; i++) {
        console.log(i)
        if (username == no[i]) {
            if(password == "163")
            {
                alert(String(no[i])+'你好')
            }
            else
            {
                alert("密碼錯誤!")
                break
            }
        }
        

        
    }
    
}