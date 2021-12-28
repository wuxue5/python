"""用python设计一个游戏"""


counts = 3

while counts > 0:
    temp = input("猜数字游戏：")
    guess = int(temp)

    #当guess=8时，输出print语句，并通过break结束if循环。
    if guess == 8:
        print("你猜对了！*^____^*")
        #break                       
    else:
        if guess < 8:
            print("小啦！/ㄒoㄒ/~~")
        else:
            print("大啦！￣﹏￣；")
            
    #counts=counts-1此语句的位置不同，导致结果也不同
            
    #此位置和if else并列，无论执行if语句还是else语句，都会让counts减一,但是需要输入三次8才能停止，故需要breank语句
    counts = counts-1

        #此位置只有在else语句的if else语句执行完后才会让counts减一,多次输入8则会一直让你输入，永不停止
        #counts = counts - 1

            #此位置只有在else语句的else语句执行完后才会让counts减一
            #counts = counts - 1
    
    
        
print("游戏结束，拜拜！")
