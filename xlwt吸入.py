# 三国表格化
import xlwt
import pymysql
host="localhost"
user="root"
password=""
database="company"
#
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
#
#
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
sql = "select * from t_dept"
param = []
data = select(sql,param)
# print(data[0][0])

wb = xlwt.Workbook()
st = wb.add_sheet("t_dept")
st.write(0,0,"部门编号")
st.write(0,1,"部门名称")
st.write(0,2,"部门地址")
for i in range(1,5):
    for j in range(0,3):
        st.write(i,j,data[i-1][j])
        # st.write(1,0,data[0][0])

wb.save("三国集团.xls")


sql1 = "select * from t_employees"
param1 = []
data1 = select(sql1,param1)
# print(data1)

# wb1 = xlwt.Workbook()
st = wb.add_sheet("t_employees")
st.write(0,0,"empno")
st.write(0,1,"ename")
st.write(0,2,"job")
st.write(0,3,"MGR")
st.write(0,4,"hiredate")
st.write(0,5,"sal")
st.write(0,6,"comm")
st.write(0,7,"deptno")

for i in range(1,16):
    for j in range(0,8):
        st.write(i,j,data1[i-1][j])
        # st.write(1,0,data[0][0])

wb.save("三国集团.xls")


