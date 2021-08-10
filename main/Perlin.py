import random

# https://en.wikipedia.org/wiki/Perlin_noise and Kian's Spicy Recitation
class Perlin(object):
    grid = [None] * 500
    gradients = [random.random() * 2 - 1 for _ in range(len(grid))]

    @staticmethod
    def perlin(x):
        x %= len(Perlin.grid) - 1
        left = Perlin.gradients[int(x)]
        right = Perlin.gradients[int(x) + 1]
        offset = x - int(x)

        # dot products
        dpLeft = left * offset
        dpRight = right * (1 - offset)

        return Perlin.interpolate(offset, dpLeft, dpRight)

    @staticmethod
    def interpolate(x, a0, a1):
        return a0 + Perlin.smoothstep(x) * (a1 - a0)

    @staticmethod
    def smoothstep(x):
        return 6 * x ** 5 - 15 * x ** 4 + 10 * x ** 3