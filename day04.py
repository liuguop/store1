shop = [
    ["劳力士手表",200000],
    ["Iphone 12X plus",12000],
    ["lenovo PC",6000],
    ["HUA WEI WATCH",1200],
    ["Mac PC",15000],
    ["辣条",2.5],
    ["老干妈",13]
]

money = input("请输入您的余额：")
money = int(money)

mycart = []

print('是否要抽一张优惠券？')
b = input('shi 或 fou : ')

if b == 'shi':
    import random
    card = random.randint(1,31)
    if card < 11:
        print('恭喜你获得老干妈7折优惠券1张')
        shop[6][1] = 0.7*shop[6][1]


    else:
        print('恭喜你获得联想电脑1折优惠券1张')
        shop[2][1] = 0.1*shop[2][1]
      

else:
    print('\t')

i = 0
while i < 3:
    print('----商品列表----')
    print('\t')
    for key, value in enumerate(shop):
        print('商品编号:',key, '\t',value)
        print('\t')
    chose = input("亲，输入您想要的商品编号：")

    if chose.isdigit():
        chose = int(chose)
        # 4.4 先判断是否存在该商品
        if chose > 6:
            print("对不起,您输入的商品不存在！")
        else:
            # 4.5 判断您的余额是否足够
            if money < shop[chose][1]:
                print("对不起，您的钱不够！")
            else:
                # 4.6 将商品添加到购物车 ，余额减去对应的钱
                mycart.append(shop[chose])
                money = money - shop[chose][1]
                print("恭喜，成功添加购物车！您的余额还剩￥：", money)
    elif chose == "q" or chose == "Q":
        print()
        break

    else:
        print("对不起，您输入有误，请重新输入！")
    i = i + 1

print("以下是您的购物小条，请拿好：")
for key, value in enumerate(mycart):
    print(key, value)
print("本次余额还剩：￥", money,)
print('\t')
print("拜拜了，您嘞！欢迎下次光临！")



