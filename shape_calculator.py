class Rectangle:

    def __init__(self, width, height):
        if (type(width) == Square) or (type(width) == Rectangle):
            self.width = width.width
        else:
            self.width: int = width
        if (type(height) == Square) or (type(height) == Rectangle):
            self.height = height.height
        else:
            self.height: int = height

    def __str__(self):
        return f"{type(self).__name__}(width={self.width}, height={self.height})"

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        result = []
        lines = ""
        separator_by = "\n"

        for i in range(self.width):
            lines += "*"

        for i in range(self.height):
            result.append(lines)

        print(" a ver como se veeeeeeee")
        print(separator_by.join(result))
        return separator_by.join(result) + "\n"

    def get_amount_inside(self, side: int):
        return int(self.get_area() / Square(side).get_area())



class Square(Rectangle):

    def __init__(self, length: int):
        width = length
        height = length
        super().__init__(width, height)

    def set_side(self, side: int):
        self.width = side
        self.height = side

    def __str__(self):
        return f"{type(self).__name__}(side={self.width})"
