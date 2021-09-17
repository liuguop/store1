# 有一个列表，[“北京”,”上海”,”广东”]
# 1)将中国所有省会城市添加到上述列表中

city = ['北京','上海','广东']
city.append(('石家庄','大连','深圳'))
print(city)
#
# #  2)广东成为第二大发达城市，将广东排在上海前面
#
city = ['北京','上海','广东']
city.append(('石家庄','大连','深圳'))
city[1] = city[2]
city[2] = '上海'
print(city)
#
# # 3)[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
gd = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
sum = 0
for i in range(0,len(gd)):
    print('i=',gd[i])
    sum += gd[i]
print('sum=',sum)
print('avage=',sum/len(gd))
print(len(gd))




# 有以下一个列表，求其中是5的倍数的和
a = [1,5,21,30,15,9,30,24]
sum = 0
for i in range(0,len(a)):
    #print('i=',a[i])
    if a[i] % 5 == 0:
        # %是求余,/是求商
        print(a[i],'是5的倍数')
        sum += a[i]
print('sum=',sum)



# 有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
# list = [1,2,3,4,5,6,7,8,9]
# # 实现效果：list = [9,8,7,6,5,4,3,2,1]
list = [1,2,3,4,5,6,7,8,9]
def R(list):
     return [i for i in reversed(list)]
print('list=',R(list))


# 请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a = {}
for i in list:
    if i not in a:
        a[i] = 1;
    else:
        a[i] += 1
print(a)


