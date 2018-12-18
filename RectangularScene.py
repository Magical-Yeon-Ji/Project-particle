from Particle import Particle
import numpy as np
import math
import random


class RectangularScene:
    def __init__(self, X, Y, n, time_step, r, total_time):
        self.__X = X
        self.__Y = Y
        self.__n = n
        self.__r = r
        self.__time_step = time_step
        self.__total_time = total_time
        self.__particles = []
        self.__current_time = 0
        for i in range(n):
            position = np.random.random((1, 2))
            self.__particles.append(Particle(position[0][0] * X,
                                             position[0][1] * Y,
                                             r,
                                             random.uniform(0, min(X, Y)),
                                             random.uniform(0, 2) * math.pi))

    def move(self):
        for particle in self.__particles:
            x, y = particle.get_x(), particle.get_y()
            r = particle.get_r()
            v = particle.get_v()
            alfa = particle.get_alfa()
             x_next = x + v * math.cos(alfa) * self.__time_step
             y_next = y + v * math.sin(alfa) * self.__time_step
             if x_next + r > self.__X or x_next + r < 0:

            #particle.set_x(x - v * math.cos(alfa) * self.__time_step)
            #particle.set_y(y + v * math.sin(alfa) * self.__time_step)
            #if y_next + r > self.__Y or y_next + r < 0:
            #particle.set_x(x + v*math.cos(alfa) * self.__time_step)
            #particle.set_y(y - v * math.sin(alfa) * self.__time_step)
            # столкновение шариков i and j  ( для взаимодействия дать координаты каждой из частичек и разные начальные скорости, как ? )
            #particle1 = Particle(self, x1, y2, r, v, alfa)
            #particle2 = Particle(self, x1, y2, r, v, alfa)
            #def distance_between_centers(particle1,particle2):
            #if muth.sqrt((x2_next - x1_next)**2 + (y2_next - y1_next)**2) < r**2:
            #
            #
            #

    def run(self):
        while self.__current_time <= self.__total_time:
            self.move()
            self.__current_time = self.__current_time + self.__time_step

    def get_particles(self):
        return self.__particles
