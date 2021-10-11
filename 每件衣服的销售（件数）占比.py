
import xlrd
import xlwt
wd = xlrd.open_workbook(filename=r"C:\Users\刘\Desktop\Jason python\day9\2020年每个月的销售情况.xlsx")
xiao = ["羽绒服","牛仔裤","风衣","皮草","T血","马甲","皮衣",
        "小西装","衬衫","休闲裤","卫衣","棉衣","铅笔裤" ]
jidu = [["1月","2月","12月"],
        ["3月","4月","5月"],
        ["6月","7月","8月"],
        ["9月","10月","11月"]
        ]
a = ["1月","2月","3月","4月","5月","6月","7月",
     "8月","9月","10月","11月","12月"]

# 全年的总销售额  ,"",
i = 0
sum = 0
while i < len(a):
    sheet = wd.sheet_by_index(i)
    rows = sheet.nrows
    for c in range(1,rows):
        data = sheet.row_values(c)
        sum = sum + data[2]*data[4]
        # print(c, "销售额：",sum)
    # print("全年的总销售额：",sum)
    i = i+1
print("全年的总销售额：",sum)
print(
"————————————————————————————————————————————————————————————————————"
    )
# 每件衣服的销售量占比

for k in xiao:
    sum1 = 0
    sum2 = 0
    for i in a:
        sheet = wd.sheet_by_name(i)
        rows = sheet.nrows
        for j in range(1,rows):
            data=sheet.row_values(j)
            sum1 = sum1 + data[4]
            if data[1] == k:
                sum2 = sum2 + data[4]
    print(k,"销量占比为：",sum2/sum1*100,"%")
print("总销量：",sum1)
print(
"————————————————————————————————————————————————————————————————————"
 )

# #每件衣服的月销售额占比（错的）
# yue1 = str(input("输入你要的月份各销售占比："))
# sum1 = 0
# sum2 = 0
# sheet = wd.sheet_by_name(yue1)
# rows = sheet.nrows
# for j in range(1,rows):
#     data = sheet.row_values(j)
#     sum1 = sum1 + data[2]*data[4]
# print("销售额和",sum1)
# for k in xiao:
#     for j in range(1, rows):
#         data = sheet.row_values(j)
#         if data[1] in k:
#             sum2 = sum2 + data[2] * data[4]
#             print(sum2)
#             b = (sum2 / sum1 )* 100
#             print(k, "销售额占比",b, "%")
#             break
# print(
#
#
#     )



# 每件衣服的销售额占比

for k in xiao:
    sum1 = 0
    sum2 = 0
    for i in a:
        sheet = wd.sheet_by_name(i)
        rows = sheet.nrows
        for j in range(1,rows):
            data=sheet.row_values(j)
            sum1 = sum1 + data[4]*data[2]
            if data[1] == k:
                sum2 = sum2 + data[4]*data[2]
    print(k,"销售额占比",sum2/sum1*100,"%")
print("销售额总和",round(sum1,2))
print(
"————————————————————————————————————————————————————————————————————"
 )
# 全年销量最低的衣服
# 最畅销的衣服是那种
list1={}
for k in xiao:
    sum1 = 0
    sum2 = 0
    for i in a:
        sheet = wd.sheet_by_name(i)
        rows = sheet.nrows#获取多少行
        cols = sheet.ncols#获取多少列
        for j in range(1,rows):
            data=sheet.row_values(j)
            sum1 = sum1 + data[4]
            if data[1] == k:
                sum2 = sum2 + data[4]
    list1[k]=sum2
print(list1)
i = max(list1, key=lambda x:list1[x])
o = min(list1, key=lambda x:list1[x])
print("全年最畅销的是：",i,"全年最不畅销的是：",o)
print(
"————————————————————————————————————————————————————————————————————"
 )
# 每个季度最畅销的衣服
list1={}
print("0.冬季 1.春季 2.夏季 3.秋季")
s = int(input("请输入你想知道的季度的序号: "))
for k in xiao:
    sum1 = 0
    sum2 = 0
    for i in jidu[s]:
        sheet = wd.sheet_by_name(i)
        rows = sheet.nrows#获取多少行
        cols = sheet.ncols#获取多少列
        for j in range(1,rows):
            data=sheet.row_values(j)
            sum1 = sum1 + data[4]
            if data[1] == k:
                sum2 = sum2 + data[4]
    list1[k]=sum2
i = max(list1, key=lambda x:list1[x])
o = min(list1, key=lambda x:list1[x])
print(s,"季度","最畅销的是：",i,"最不畅销的是：",o)



