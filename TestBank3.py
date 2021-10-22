from unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import bank_takeMoney
#account, password, money
#取钱

da = [
    ["ge86y4fU","123456",900,3],
    ["234r6653","242566",499,0],
    ["234r66t3","242466",499,0],
    ["mog25aTx", "123456", 499, 0]
]

@ddt
class TestBank3(TestCase):

    @data(*da)
    @unpack
    def testTakeMoney(self,a,b,c,d):

        result = bank_takeMoney(a,b,c)

        self.assertEqual(result,d)