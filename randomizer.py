import random


class Randomizer:

    def __init__(self, arr_len):
        self.arr_len = arr_len

    def rand_int(self):
        random.randint(1, 100)

    def rand_arr(self):
        reg4 = []
        for i in range(self.arr_len):
            reg4.append(random.randint(1, 100))
        return reg4