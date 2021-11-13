import random
x = random.randint(1,100)
print(x)
while(1):
    a = int(input("請輸入數字: "))
    if(a < x):
        print("比答案小")
    if(a > x):
        print("比答案大")
    if(a == x):
        print("猜對了")
        break
