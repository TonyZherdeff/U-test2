class Number:
    def __init__(self, num: int):
        self.num = num

    def read_num(self):
        return self.num

    def write_num(self, new_num):
        self.num = new_num
        return new_num

    def oct_num(self):
        return oct(self.num)[2:]

    def hex_num(self):
        return hex(self.num)[2:]

    def bin_num(self):
        return bin(self.num)[2:]
