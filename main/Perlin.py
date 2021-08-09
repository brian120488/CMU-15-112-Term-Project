import random

# https://en.wikipedia.org/wiki/Perlin_noise and Kian's Spicy Recitatioin
class Perlin(object):
    grid = [None] * 100
    gradients = [random.random() * 2 - 1 for _ in range(len(grid))]
    amplitude = 1
    frequency = 1
    
    def perlin(self, x):
        left = self.gradients[int(x)]
        right = self.gradients[int(x) + 1]
        offset = x - int(x)

        # dot products
        dpLeft = left * offset
        dpRight = right * (1 - offset)

        return self.interpolate(offset, dpLeft, dpRight)

    def interpolate(self, x, a0, a1):
        return a0 + self.smoothstep(x) * (a1 - a0)

    def smoothstep(self, x):
        return 6 * x ** 5 - 15 * x ** 4 + 10 * x ** 3