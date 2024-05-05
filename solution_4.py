import math

class GeometricObject:

    def __init__(self, x=0.0, y=0.0, color='black', filled=False):

        self.__x = float(x)
        self.__y = float(y)
        self.color = color
        self.filled = filled

    def set_coordinate(self, x, y):

        self.__x = float(x)
        self.__y = float(y)
    
    def set_color(self, color):
        self.color = color

    def set_filled(self, filled):
        self.filled = filled

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_color(self):
        return self.color
    
    def is_filled(self):
        return self.filled
    
    def __str__(self):
        return f'({self.__x}, {self.__y})\ncolor: {self.color}\nfilled: {self.filled}'
    
    def __repr__(self):
        if self.filled:
            is_flld = ''
        else:
            is_flld = ' no'
        return f'({int(self.__x)}, {int(self.__y)}) {self.color}{is_flld} filled'

class Circle(GeometricObject):

    def __init__(self, x=0.0, y=0.0, radius=0.0, color='black', filled=False):

        super().__init__(x, y, color, filled)

        if radius < 0:
            self.__radius = 0.0
        else:
            self.__radius = float(radius)
    
    radius = property()

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            self.__radius = 0.0
        else:
            self.__radius = float(radius)
    
    @radius.getter
    def radius(self):
        return self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    def get_perimetr(self):
        return 2 * math.pi * self.__radius
    
    def get_diametr(self):
        return 2 * self.__radius
    
    def __str__(self):
        return f'radius: {self.__radius}\n{super().__str__()}'
    
    def __repr__(self):
        return f'radius: {int(self.__radius)} {super().__repr__()}'

class Rectangle(GeometricObject):

    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, color='black', filled=False):

        super().__init__(x, y, color, filled)

        if width < 0:
            self.width = 0.0
        else:
            self.width = float(width)

        if height < 0:
            self.height = 0.0
        else:
            self.height = float(height)
    
    def set_width(self, width):
        if width < 0:
            self.width = 0.0
        else:
            self.width = float(width)
    
    def set_height(self, height):
        if height < 0:
            self.height = 0.0
        else:
            self.height = float(height)

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimetr(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f'width: {self.width}\nheight: {self.height}\n{super().__str__()}'

    def __repr__(self):
        return f'width: {int(self.width)} height: {int(self.height)} {super().__repr__()}'
