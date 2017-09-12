import random
help = '''您好，我是猜数小游戏。
以下是游戏规则：
1.机器随机生成一位20以内的整数（含20）；
2.您有10次机会猜，每猜一次，机器会提示您输入的数大了或小了；
3.若您猜中或者用完10次机会，游戏结束。'''
print(help)
an_int = random.randint(1, 21)
for i in range(10):
    user_input = input("请您输入您猜的数字：")
    if user_input.isdigit():
        number = int(user_input)
        if number > an_int:
            print('您输入的数太大了！')
        elif number < an_int:
            print('您输入的数太小了！')
        else:
            print('恭喜您猜中了！')
            break
    else:
        print('客官，您耍我呢！请您输入整数！')
    j = 9 - i 
    print(f'你还有{j}次机会！')
        
    
