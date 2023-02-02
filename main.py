from engine import Minkowski
from matplotlib import pyplot as plt



class Main(Minkowski):
    x = []
    y1 = []
    y2 = []

    def double_grapher(self, x, y1, y2):
        plt.plot(x, y1, "r")
        plt.plot(x, y2, "b")

        plt.show()

    def main_loop(self):
        self.vec1 = self.rand_arr()
        self.vec2 = self.rand_arr()

        for i in range(self.count):
            reg = self.Inequality_sim()
            Main.x.append(i)
            Main.y1.append(reg[0])
            Main.y2.append(reg[1])
            self.power += 0.1
        self.double_grapher(Main.x, Main.y1, Main.y2)


test1 = Main(100, 3, 1000)
print(test1.main_loop())
