# 打印10个数的求和结果
i = 0
sum = 0
while i <= 10:
    b = int(input('请输入一个数: ' ))
    print('b',b)
    sum += b
    print('sum', sum)
    i = i + 1
    if i == 10:
        print('10个数的总和为:',sum)
        break




# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
i = 0
sum = 0
a = 0
while i <= 10:
    b = int(input('请输入一个数: '))
    print('b',b)
    if b > a:
        a = b
    sum += b
    print('sum', sum)
    i = i + 1
    if i == 10:
        print('最大的数为：',a)
        print('10个数的总和为:',sum)
        print('平均数：',sum/i)
        break



# 使用random模块，如何产生 50~150之间的数？
import random
b = random.randint(50,150)
print(b)



# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
a = int(input('输入三角形的一条边长：'))
b = int(input('输入三角形的一条边长：'))
c = int(input('输入三角形的一条边长：'))
if (a + b > c and a - b < c) or (a + c > b and a - c < b) or (b + c > a and b - c < a):
    print('可以构成三角形')
    if a == b == c:
        print('为等边三角形')
    elif a == b or b == c or a == c:
        print('为等腰三角形')
    elif (a*a + b*b == c*c) or (c*c + b*b == a*a) or (a*a + c*c == b*b):
        print('为直角三角形')
    else:
        print('为普通三角形')
else:
    print('构不成三角形')



# 有以下两个数，使用+，-号实现两个数的调换。
a = 56
b = 78
a,b = b,a
print(a,b)


# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
print('欢迎来到极乐世界')
print('用户名：')
print('密码：')
i = 0
while i <= 3:
    用户名 = str(input('用户输入：'))
    密码 = str(input('用户输入：'))
    if 用户名 == 'root' and 密码 == 'admin' :
        print('欢迎客官光临')
        break
    else:
        print('输入错误，请重新输入')
    i = i + 1
    if i == 3:
        print('过于频繁操作，暂时禁止访问')
        break


# 编程实现下列图形的打印

print('打印三角形')
for i in range(int(input('请输入一个数字：'))):
    for j in range(0, 10 - i):
        print(end=" ")
    for k in range(10 - i, 10):
        print("*", end=" ")
    print("")








# 使用while循环实现99乘法表的打印。
for i in range(1,10):
    j=0
    while j<i:
        j+=1
        print('%d*%d=%-3d' % (j, i, j * i), end='')
    print()

# 编程实现99乘法表的倒叙打印
i = 1
while i < 10:
    j = 10
    while j > i:
        j -= 1
        print('%d*%d=%-3d' % (j, i, j * i), end='')
    print()
    i += 1

# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
jing = -20
up = 3
down = -2
num = 1
while jing < 0:
    print('day ',num,end="   ")
    jing += up
    print('up',jing,end="   ")
    if jing >= 0:
        break
    jing += down
    print('down',jing)
    if jing >= 0:
        break
    num += 1


# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
Sum = 0
factorial = 1
num = int(input('请输入一个数字：'))
for i in range(1,num+1):
    factorial = factorial*i
    Sum += factorial
print('阶乘之和：',Sum)





