from fuzzymeta import fuzzymeta


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
        self.hieght, self.width = self.width, self.height

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
