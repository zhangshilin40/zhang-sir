import random
# 循环实现：猜拳游戏：
'''
(1)电脑随机产生石头剪刀布，
(2)键盘输入你要出的拳，（布：0 剪刀: 1 石头: 2），
(3)判断哪方赢
'''

while True:
    print("***石头剪刀布游戏***")
    # dic = {'0': "布", "1": "剪刀", "2": "石头", "Q": "退出", "q": "退出"}   # 字典
    print('0：布',  "1：剪刀", "2：石头", "Q/q：退出")
    # print("规则", dic)
    # 玩家输入
    per = input("请输入你的选择 布：0 剪刀：1 石头：2   退出：Q/q  ：\n")
    if per == "Q" or per == "q":
        print("游戏结束")
        break

    # 判断玩家输入的是不是数字
    if per.isdigit():
        per = int(per)
    else:
        print("输入有误，请重新输入")
        continue

    if per == 0:
        print("玩家：布")
    elif per == 1:
        print("玩家：剪刀")
    elif per == 2:
        print("玩家：石头")

    # 电脑随机生成一个0-2之间的整数
    com = random.randint(0, 2)

    # 玩家输入的值必须是0,1,2三个中的一个
    if per in (0, 1, 2):
        # 判断电脑出的拳
        if com == 0:
            print("电脑：布")
        elif com == 1:
            print("电脑：剪刀")
        else:
            print("电脑：石头")
    # 判断哪方赢
        # 剪刀1 - 布0 == 1   石头2-剪刀1 == 1  布0 - 石头2 == -2
        # if ((per - com) == 1) or ((per - com) == -2):
        if ((per - com) == 1) or ((com - per) == 2):
            print("玩家赢")
        elif com == per:
            print("平局")
        else:
            print("电脑赢")
    else:
        print("输入有误，请输入0，1，2")

'''
if (com == 1 and per == 2) or (com == 0 and per == 1) or(com == 2 and per == 0 ):
    print("玩家赢")
elif com == per:
    print("平局")
else:
    print("电脑赢")
'''
