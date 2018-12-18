class Particle:
    def __init__(self, x, y, r, v, alfa):
        self.__x = x
        self.__y = y
        self.__r = r
        self.__v = v
        self.__alfa = alfa

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_r(self):
        return self.__r

    def get_v(self):
        return self.__v

    def get_alfa(self):
        return self.__alfa

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y
