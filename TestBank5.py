from unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_transformMoney
#(outputaccount, inputaccount, outputpassword, outputmoney):
#取钱

da = [
    ["ge86y4fU","mog25aTx","123456",3,0],
    ["234r6653","242566","499333",0,1],
    ["234re6t3","242466","499123",0,1],
    ["mog25aTx", "12378456", "499123", 0,2]
]

@ddt
class TestBank5(TestCase):

    @data(*da)
    @unpack
    def testTransformMoney(self,a,b,c,d,e):

        result = bank_transformMoney(a,b,c,d)

        self.assertEqual(result,e)