from threading import Thread
from HTMLTestRunner import HTMLTestRunner
import unittest
import os # 系统
class PCmanager(Thread):

    def run(self) -> None:
        # 杀毒的任务程序
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestBank*.py")

        # 执行器
        runner = HTMLTestRunner.HTMLTestRunner(
            title="测试报告",
            description="银行的测试报告",
            verbosity=1,
            stream=open(file="../../任务/银行.html", mode="w+", encoding="utf-8")
        )

        runner.run(tests)
p2 = PCmanager()
p2.start()

