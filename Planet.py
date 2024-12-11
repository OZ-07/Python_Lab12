import turtle
"""class Planet:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity"""


class Planet:
    def __init__(self, name: str, mass: float, x: float, vel_x: float, vel_y: float,y: float=0.0,
                color="black"): #
        self.name = name
        self.mass = mass
        self.distance = x
        self.x = x
        self.y = y
        self._vel_x = vel_x
        self._vel_y = vel_y
        # this is the graphics stuff
        self.t = turtle.Turtle()
        self.t.shape('circle')
        self.t.color(color)
        # initial positioning of planet
        self.t.penup()
        self.t.goto(self.x,self.y)
        self.t.pendown()

    def get_mass(self) -> float:
        return self.mass

    def get_distance(self) -> float:
        return self.distance

    def set_distance(self,distance):
        self.distance = distance

    def get_x_pos(self) -> float:
        return self.x

    def get_y_pos(self) -> float:
        return self.y

    def get_x_vel(self) -> float:
        """Returns the velocity of the planet in the x-direction."""
        return self._vel_x

    def get_y_vel(self) -> float:
        """Returns the velocity of the planet in the y-direction."""
        return self._vel_y

    def set_x_vel(self, new_x_vel: float):
        self._vel_x = new_x_vel

    def set_y_vel(self, new_y_vel: float):
        self._vel_y = new_y_vel

    def move_to(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
        self.t.goto(new_x,new_y)

    def __str__(self) -> str:
        """Returns a string representation of the planet."""
        return (f"Planet(name={self.name}, mass={self.mass}, distance={self.distance}, "
                f"x={self.x}, y={self.y}, vel_x={self._vel_x}, vel_y={self._vel_y})")
