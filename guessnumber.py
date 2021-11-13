import random
start = int(input('請決定隨機數字範圍起始值: '))
end = int(input('請決定隨機數字範圍結束值: '))

x = random.randint(start,end)
print('正確答案是:', x)#正確答案
count = 0
while(1):
    count += 1
    a = int(input("請輸入數字: "))
    if(a < x):
        print("比答案小")
    if(a > x):
        print("比答案大")
    if(a == x):
        print("猜對了!!!!")
        print("這是你猜的第", count, "次\n")
        break
    print("這是你猜的第", count, "次\n")
