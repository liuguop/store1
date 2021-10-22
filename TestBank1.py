from unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_saveMoney
#存钱
#account,money
da = [
    ["ge86y4fU",-12,True],
    ["23456653",499,False],
    ["DR7G3wdF",-12,False]
]

@ddt
class TestBank1(TestCase):

    @data(*da)
    @unpack
    def testSaveMoney(self,a,b,c):

        result = bank_saveMoney(a,b)

        self.assertEqual(result,c)