import random
from DBUtils import select
from DBUtils import update

def welcome():
    print('-----------------------------------')
    print('----         中国农业银行        ----')
    print('----         账户管理系统        ----')
    print('----            V1.0           ----')
    print('-----------------------------------')
    print('*** 1.开户                      ****')
    print('*** 2.存钱                      ****')
    print('*** 3.取钱                      ****')
    print('*** 4.转账                      ****')
    print('*** 5.查询                      ****')
    print('*** 6.Bye！                     ****')
    print('-----------------------------------')


bank = {}
bank_name = '中国农业银行北京市昌平支行'


def bank_addUser(account, username, password, country, province, street, house, money, bank_name):
    # 1.判断数据库是否已满
    #if len(bank) >= 100:
    sql1 = "select count(*) from bankUser "
    param1 = []
    data1 = select(sql1,param1)
    if data1[0][0] >= 100:
        # print('数据库满了')
        return 3
    # 2.判断用户是否存在
    #if username in bank:u
    sql2 = "select * from bankUser  where username  = %s"
    param2 = [username]
    data2 = select(sql2, param2)  # ("adfadf","贾生","adsfadsfa")
    if len(data2) != 0:
        # print('用户已存在')
        return 2
    # 3.正常开户
    # bank[username] = {
    #     "account": account,
    #     "password": password,
    #     "country": country,
    #     "province": province,
    #     "street": street,
    #     "house": house,
    #     "money": money,
    #     "bank_name": bank_name
    # }
    sql3 = "insert into bankUser  values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
    param3 = [account, username, password, country, province, street, house, money, bank_name]
    update(sql3, param3)
    # print(bank)
    return 1


def addUser():
    while 1:
        account = random.randint(00000000, 99999999)
        # 账号
        username = input('请输入你的名字:')
        # 用户名
        password = str(input('请输入六位数的密码:'))
        # 密码

        if len(password) < 6 or len(password) > 6:
            print('输入错误，请重新输入,密码必须是六位')
            continue
        country = input('请输入国家：')
        # 国家
        province = input('请输入省份：')
        # 省份
        street = input('请输入街道：')
        # 街道
        house = input('请输入门牌号：')
        # 门牌号house number
        address = country + province + street + house
        # 地址
        money = int(input('请输入金额：'))
        # 金钱
        sta = bank_addUser(account, username, password, country, province, street, house, money, bank_name)
        if sta == 3:
            print('对不起，用户库已满，请携带证件到其他银行办理！')
        elif sta == 2:
            print("对不起，该用户已存在！请勿重复开户！")
        elif sta == 1:
            print('恭喜你，开户成功，以下是你的开户信息')
            info = '''
                        ----------个人信息------
                        用户名：%s
                        密码：%s
                        账号：%s
                        地址信息
                            国家：%s
                            省份：%s
                            街道：%s
                            门牌号: %s
                        金额：%s
                        开户行地址：%s
                        ------------------------
                    '''
            print(info % (username, password, account, country, province, street, house, money, bank_name))
            break


def put_money(account, money1):
    # if a in bank[username].values():
    #     bank[username]['money'] += b
    #     info = '''
    #         ----------存款凭证--------------
    #                 用户名：%s
    #                 银行账户：%s
    #                 存入金额：%s
    #                 账户余额：%s
    #                 开户行名称：%s
    #     '''
    #     print(info % (username, a, b, bank[username]['money'], bank_name))
    sql = "select * from bankUser where account = %s"
    param = [account]
    username = select(sql,param)
    if account == username[0][0]:
        sql3 = " update bankUser set money = money + %s where account = %s "
        param3 = [int(money1),account]
        money = update(sql3,param3)
        return True
    else:
        return False


# def give_money(q, w, r, username):
def give_money(account,password,money):
    # ra = q in bank[username].values()
    sql = "select * from bankUser where account = %s"
    param = [account]
    username = select(sql,param)
    # if ra == False:
    #     return 1
    # elif w != bank[username]['password']:
    #     return 2
    # elif bank[username]['money'] < r:
    #     return 3
    # else:
    #     bank[username]['money'] -= r
    #     info = '''
    #         ------------存款凭证------------
    #                 用户名:%s
    #                 银行账号：%s
    #                 取款金额：%s
    #                 账户余额：%s
    #                 开户行名称：%s
    #
    #     '''
    #     print(info % (username, q, r, bank[username]['money'], bank_name))
    #     return 0
    if account == username[0][0]:
        if password == username[0][2]:
            if int(money) <= username[0][7]:
                sql1 = "update bankUser set money = money - %s where account = %s and password = %s and %s <= money"
                param1 = [int(money),account,password,int(money)]
                money = update(sql1,param1)
                return True
            else:
                return 3
        else:
            return 2
    else:
        return 1

# parameter1 转出的账号,parameter2 转入的账号,parameter3 转出账户的密码
# parameter4 转出的金额 parameter5 转出用户名,parameter6 转入用户名
# def zz(parameter1, parameter2, parameter3, parameter4, parameter5, parameter6):
def zz (account,account1,password,money):
    sql = "select * from bankUser where account = %s"
    param = [account]
    username = select(sql,param)
    sql1 = "select * from bankUser where account = %s"
    param1 = [account1]
    username1 = select(sql1, param1)
    if account == username[0][0]:
        if account1 == username1[0][0]:
            if password == username[0][2]:
                if int(money) <= username[0][7]:
                    sql2 = "update bankUser set money = money - %s where account = %s and password = %s and %s <= money"
                    param2 = [int(money),account,password,int(money)]
                    money2 = update(sql2,param2)
                    sql3 = "update bankUser set money = money + %s where account = %s "
                    param3 = [int(money), account1]
                    money3 = update(sql3, param3)
                    return True
                else:
                    return 3
            else:
                return 2
    else:
        return 1

#     existence1 = parameter1 in bank[parameter5].values()
#     existence2 = parameter2 in bank[parameter6].values()
#     if existence1 and existence2:
#         if parameter3 == bank[parameter5]['password']:
#             if bank[parameter5]['money'] >= parameter4:
#                 bank[parameter5]['money'] -= parameter4
#                 bank[parameter6]['money'] += parameter4
#                 info = '''
#                                     ------------转账凭证------------
#                                             转入用户名:%s
#                                             转入账号：%s
#                                             转入金额：%s
#                                             转入账户余额：%s
#                                             开户行名称：%s
#
#                                 '''
#                 print(info % (parameter6, parameter2, parameter4, bank[parameter6]['money'], bank_name))
#                 return 0
#             else:
#                 return 3
#         else:
#             return 2
#     else:
#         return 1


# parameter1 账号,parameter2 账号密码 , parameter3 用户名
# def cx(parameter1, parameter2, parameter3):
def cx(account,password):
    sql = "select * from bankUser where account = %s"
    param = [account]
    username = select(sql, param)
    if account == username[0][0]:
        if password==username[0][2]:
            return username
        else:
            print("密码输入错误")
    else:
        print("用户不存在")
    return
#     if parameter1 in bank[parameter3].values():
#         if parameter2 == bank[parameter3]['password']:
#             info = '''
#                         ------------个人信息------------
#                                 当前账号:%s
#                                 密码：%s
#                                 余额：%s元
#                                 国家：%s
#                                 省份：%s
#                                 街道：%s
#                                 门牌号：%s
#                                 开户行名称：%s
#                     '''
#             # 每个元素都可传入%
#             print(info % (
#                 parameter3, parameter2, bank[parameter3]['money'], bank[parameter3]['country'],
#                 bank[parameter3]['province'], bank[parameter3]['street'], bank[parameter3]['house'],
#                 bank_name))
#         else:
#             print("密码不正确！")
#     else:
#         print("该用户不存在！")


while True:
    welcome()
    number = input('请输入你想办理的业务序号(1.开户 2.存钱 3.取钱 4.转账 5.查询 6.Bye):')
    # 序号
    # 添加用户
    if number == '1':
        addUser()


    # 存钱
    elif number == '2':
        account1 = int(input("请输入相应的账号："))
        putmoney = int(input("请输入存放的金额："))
        e = put_money(account1, putmoney)
        print(e)

    # 取钱
    elif number == '3':
        # username = input("请输入用户名：")
        account = int(input("请输入相应的账号："))
        password = int(input("请输入相应的账号密码："))
        givemoney = int(input("请输入要取的金额："))
        qw = give_money(account, password, givemoney)
        print(qw)

    # 转账
    elif number == '4':
        account = int(input("请输入相应的转出账号："))
        account1 = int(input("请输入相应的转入账号："))
        password = int(input("请输入相应的转出账号密码："))
        zmoney = int(input("请输入转出金额："))
        # username = input("请输入转出用户名：")
        # username_1 = input("请输入转出用户名：")
        oo = zz(account, account1, password, zmoney)
        print(oo)


    # 查询
    elif number == '5':
        account = int(input("请输入相应的账号："))
        password = int(input("请输入相应的账号密码："))
        # username = input("请输入用户名：")
        qa = cx(account, password)
        print(qa)


    # 退出
    elif number == '6':
        print('欢迎你下次光临')
        break

    # 意外
    else:
        print('对不起，没有你想办的业务序号')
        print('是否继续办理业务')
        b = input('请输入是或否:')
        if b == '是':
            continue
        elif b == '否':
            print('退卡成功')
            break
        else:
            print('退卡成功')
            break






