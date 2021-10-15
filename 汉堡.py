from threading import Thread
import time
bread = 0 #面包
money = 10000
class MakeBread(Thread):
    def run(self) -> None:
        global bread
        while True:
            if bread <500:
                time.sleep(0.5)
                bread += 1
                print("做了",bread,"个面包")
            elif bread>=500:
                time.sleep(3)


class TakeBread(Thread):
    username = ""
    count = 0
    def run(self) -> None:
        global bread,money
        while True:
            if bread>0:
                bread -= 1
                self.count +=1
                money -= 5
                print(self.username, "抢了", self.count, "花了", 5 * self.count)
                if money <= 0:
                    print("没钱了")
                    break
            elif bread<=0:
                time.sleep(1)

c1 = MakeBread()
c2 = MakeBread()
c3 = MakeBread()

g1 = TakeBread()
g2 = TakeBread()
g3 = TakeBread()
g4 = TakeBread()
g5 = TakeBread()
g6 = TakeBread()

g1.username = "张三"
g2.username = "李四"
g3.username = "王‍"
g4.username = "刘‍"
g5.username = "张"
g6.username = "关"

c1.start()
c2.start()
c3.start()
g1.start()
g2.start()
g3.start()
g4.start()
g5.start()
g6.start()
