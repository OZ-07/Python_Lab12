import turtle
"""class Sun:
    def __init__(self,name, mass, position):
        self.name = name
        self.mass = mass
        self.position = position"""
class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: float=0.0, y: float=0.0):
        """Initializes the Sun object with the given attributes."""
        self._name = name  # Private attribute for encapsulation
        self._radius = radius
        self._mass = mass
        self._temp = temp
        self.x = x
        self.y = y
        #graphics stuff starts here
        self.t = turtle.Turtle()
        self.t.shape('circle')
        self.t.color('yellow')
        self.t.pen()
        self.t.goto(self.x,self.y)
        self.t.pendown()

    def get_mass(self) -> float:
        return self._mass

    def get_x_pos(self) -> float:
        return self.x

    def get_y_pos(self) -> float:
        return self.y

    def __str__(self) -> str:
        """Returns a string representation of the Sun object."""
        return (f"Sun(name={self._name}, radius={self._radius} km, mass={self._mass} kg, "
                f"temperature={self._temp} K, position=({self._x}, {self._y}))")
