print("1-100 NUMBER")
x=0
l= True
i=True
while (i==True):
    in_1 = int(input("one number:"))
    in_2 = int(input("two number:"))
    if int(in_1)>0 and int(in_1)<100 and int(in_2)>0 and int(in_2)<100 :
        while(l==True):
            or_text =input("你要做+法計算來是-法(+/-):") 
            if or_text=="+":
                sum =in_1+in_2
                if sum >100:
                    print("無法計算!")
                    break
                print(sum)
                break
            elif or_text=="-":
                sum=in_1-in_2
                if sum <0:
                    print("無法計算!")
                    break
                print(sum)
                break
            else:
                print('!!!請使用(+/-)來選擇!!!')
                continue
        while x!=4:
            scan = input("是否還要繼續(y/n):")
            if scan =='y' or scan =='Y':
               pass
            elif scan =='N' or scan=='n':
                i=False
                print("謝謝使用!")
            else:
                x+=1
                print("!!!請使用(y/n)來選擇!!!\n警告"+str(x)+"次\n")
                if x== 3:
                    print("禁止使用，退出程式!")
                    break
            break
        continue   
    else:
        print("無法計算!!")    