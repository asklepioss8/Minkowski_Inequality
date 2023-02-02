from randomizer import Randomizer


class Minkowski(Randomizer):

    def __init__(self, arr_len, power, count):
        super().__init__(arr_len)
        self.vec1 = []
        self.vec2 = []
        self.power = power
        self.count = count

    def Inequality_sim(self):

        reg1, reg2, reg3 = 0, 0, 0

        if len(self.vec1) == len(self.vec2):
            for i in range(len(self.vec1)):
                reg1 += (self.vec1[i] + self.vec2[i]) ** self.power
                reg2 += (self.vec1[i]) ** self.power
                reg3 += (self.vec2[i]) ** self.power

        else:
            print("Lenght of arrays are not equal")

        return reg1 ** (1 / self.power), (reg2 ** (1 / self.power)) + (reg3 ** (1 / self.power))
















