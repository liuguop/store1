'''
    测试银行：
        使用参数化。
        测试银行的核心业务
'''
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_addUser

#开户
#username, password, country, province, street, door, money
da = [
    ["jason","123456","cn","安徽省","桃源路","s001",6000,3],
    ["jason","123456","cn","安徽省","桃源路","s001",6000,2],
    ["jasn","143456","cn","安徽省","桃源路","s001",6000,1],
    ["json","123456","cn","安徽省","桃源路","s001",6000,1]
]

@ddt
class TestBank(TestCase):

    @data(*da)
    @unpack
    def testAddUser(self,a,b,c,d,e,f,g,h):

        result = bank_addUser(a,b,c,d,e,f,g)

        self.assertEqual(result,h)







