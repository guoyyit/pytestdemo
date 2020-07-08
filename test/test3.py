# python 循环相关
a=1
while(a<100):
    print(a)
    a+=1

b=1
while(b<5):
    print("真")
    b+=1
else:
    print("假")

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if(site=='Runoob'):
        print('停止',site)
        break
    else:
        print(site)

# range 用户生成序列
for s in range(100):
    print(s,end="")