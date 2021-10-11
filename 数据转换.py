import pymysql
import xlrd
import xlwt
host="localhost"
user="root"
password=""
database="xlxs1"
# 改
def update(sql,param):
    # 连接
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()  # 控制台
    cursor.execute(sql,param)
    # 数据库提交到数据库里
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()
# 查
def select(sql,param,mode="all",size=1):
    # 连接
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()  # 控制台
    cursor.execute(sql,param)
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    # 数据库提交到数据库里
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()
# 增
def insert(sql,param):
    # 连接
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()  # 控制台
    cursor.execute(sql,param)
    # 数据库提交到数据库里
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()
# 删
def delete(sql,param):
    # 连接
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()  # 控制台
    cursor.execute(sql,param)
    # 数据库提交到数据库里
    con.commit()
    # 关闭资源
    cursor.close()
    con.close()
# CREATE DATABASE xlxs CHARACTER SET utf8;
# CREATE TABLE `1月`(
# 	日期 VARCHAR(30),
# 	服装名称 VARCHAR(50),
# 	价格_件 DOUBLE(8,1),
# 	本月库存数量 DOUBLE(8,1),
# 	销售量_每日 DOUBLE(8,1)
# );
wd = xlrd.open_workbook(filename=r"C:\Users\刘\Desktop\Jason python\day9\2020年每个月的销售情况.xlsx",encoding_override=True)
for i in range(0,12):
    sheet = wd.sheet_by_index(i)
    rows = sheet.nrows
    for i in range(1,rows):
        a = sheet.row_values(i)
        sql = "insert into 1月 values(%s,%s,%s,%s,%s) "
        param = [a[0],a[1],a[2],a[3],a[4]]
        insert(sql,param)
#
# sheet = wd.sheet_by_name("2月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 2月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("3月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 3月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("4月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 4月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("5月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 5月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("6月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 6月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("7月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 7月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("8月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 8月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("9月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 9月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("10月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 10月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("11月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 11月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)
#
# sheet = wd.sheet_by_name("12月")
# rows = sheet.nrows
# for i in range(1,rows):
#     a = sheet.row_values(i)
#     sql = "insert into 12月 values(%s,%s,%s,%s,%s) "
#     param = [a[0],a[1],a[2],a[3],a[4]]
#     insert(sql,param)





