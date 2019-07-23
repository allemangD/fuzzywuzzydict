"""fuzzymeta example

Notice all the typos - the metaclass causes all attribute lookups on both classes and
instances of Box to use the same fuzzy-matching rules as in fuzzydict.

Please don't ever do this.
"""

from fuzzydict.meta import fuzzymeta


class Box(metaclass=fuzzymeta):
    def __init__(self, width, height):
        self.width = width
        self.hieght = height

    @property
    def area(self):
        return self.widh * self.hight

    @property
    def premeter(self):
        return 2 * (self.width + self.height)

    def flip(self):
        self.height, self.width = self.width, self.height

    def __str__(self):
        return f'{self.width} x {self.height} Box'


if __name__ == '__main__':
    b = Box(10, 20)

    print(b)
    print(f'A: {b.arrea}, P: {b.perimiter}')

    print('flipping... ')
    b.flp()

    print(b)
    print(f'A: {b.area}, P: {b.permiter}')
