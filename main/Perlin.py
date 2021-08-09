import random

# https://en.wikipedia.org/wiki/Perlin_noise and Kian's Spicy Recitatioin
class Perlin(object):
    grid = [None] * 10
    gradients = [random.random() * 2 - 1 for _ in range(len(grid))]
    amplitude = 1
    frequency = 1
    
    def perlin(self, x):
        left = self.gradients[int(x)]
        right = self.gradients[int(x) + 1]
        offset = x - int(x)

        # dot products
        dpLeft = left * offset
        dpRight = right * offset

        interpolate(offset, dpLeft, dpRight)

    def interpolate(self, x, a0, a1):
        return a0 + smoothstep(x) * (a1 - a0)