from unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_selectUser
#查询
#account, password
da = [
    ["ge86y4fU","123456",None],
    ["23456653","134456",None],
    ["mog25aTx","123956",None]
]

@ddt
class TestBank2(TestCase):

    @data(*da)
    @unpack
    def testSelectUser(self,a,b,c):

        result = bank_selectUser(a,b)

        self.assertEqual(result,c)