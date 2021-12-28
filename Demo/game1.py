"""用python设计一个游戏"""


temp=input("猜数字游戏：")
guess=int(temp)

if guess==8:
    print("你猜对了！*^____^*")

else:
    if guess<8:
        print("小啦！/ㄒoㄒ/~~")
    else:
        print("大啦！￣﹏￣；")
print("游戏结束，不玩了！")
