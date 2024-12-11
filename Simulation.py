from Sun import Sun
from Planet import Planet
from Solar_System import SolarSystem
import turtle
"""class Simulation:
    def __init__(self,a_solar_system, the_sun, planets):
        self.a_solar_system = a_solar_system
        self.the_sun = the_sun
        self.planets = planets
"""


class Simulation:
    def __init__(self, solar_system: 'SolarSystem', width: int, height: int, num_periods: int):
        self.solar_system = solar_system
        self._width = width
        self._height = height
        self._num_periods = num_periods
        # graphics stuff for space
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=self._width,height=self._height)
        self.t.clear()

    def run(self):
        print(f"Starting simulation for {self._num_periods} periods...\n")
        for period in range(1, self._num_periods + 1):
            print(f"--- Period {period} ---")

            # Move all planets according to their velocities
            self.solar_system.move_planets()

            # Display the current state of the solar system
            self.solar_system.show_planets()
        self.screen.exitonclick()

if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 10000000, 5800)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 1, 25, 5.0, 200.0, color="green")#
    solar_system.add_planet(earth)

    mars = Planet("MARS", .1, 62, 10.0, 125.0,color="red") #
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()
