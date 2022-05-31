import itertools as its
words = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
# 生成密码的位数
r = its.product(words,repeat=8)
dic = open('D:/data/1/12/pwd.txt','a')

for i in r:
    dic.write(''.join(i))
    dic.write(''.join('\n'))
    print(i)

dic.close()
print('密码本生成')