from HTMLTestRunner import HTMLTestRunner
import unittest
import os # 系统

# 加载所有用例
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

# 执行器
runner = HTMLTestRunner.HTMLTestRunner(
    title= "计算器的测试报告",
    description="加法和减法的测试报告",
    verbosity=1,
    stream = open(file="计算器.html",mode="w+",encoding="utf-8")
)

runner.run(tests)












