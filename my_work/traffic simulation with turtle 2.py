import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Traffic Light Simulation")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)


# Create a traffic light
class TrafficLight:
    def __init__(self):
        self.red_light = turtle.Turtle()
        self.yellow_light = turtle.Turtle()
        self.green_light = turtle.Turtle()
        self.setup_lights()
        self.current_light = "red"

    def setup_lights(self):
        # Set up red light
        self.red_light.penup()
        self.red_light.goto(50, 170)
        self.red_light.color("red")
        self.red_light.shape("circle")

        # Set up yellow light
        self.yellow_light.penup()
        self.yellow_light.goto(50, 150)
        self.yellow_light.color("yellow")
        self.yellow_light.shape("circle")

        # Set up green light
        self.green_light.penup()
        self.green_light.goto(50, 130)
        self.green_light.color("green")
        self.green_light.shape("circle")

        self.red_light.showturtle()
        self.yellow_light.hideturtle()
        self.green_light.hideturtle()

    def change_light(self):
        if self.current_light == "red":
            self.red_light.hideturtle()
            self.green_light.showturtle()
            self.current_light = "green"
            screen.ontimer(self.change_light, 3000)  # Green for 3 seconds
        elif self.current_light == "green":
            self.green_light.hideturtle()
            self.yellow_light.showturtle()
            self.current_light = "yellow"
            screen.ontimer(self.change_light, 1000)  # Yellow for 1 second
        elif self.current_light == "yellow":
            self.yellow_light.hideturtle()
            self.red_light.showturtle()
            self.current_light = "red"
            screen.ontimer(self.change_light, 3000)  # Red for 3 seconds


# Create a car class
class Car:
    def __init__(self, color, speed):
        self.car = turtle.Turtle()
        self.car.shape("square")
        self.car.color(color)
        self.car.penup()
        self.car.goto(-400, random.randint(-100, 100))
        self.speed = speed

    def move(self, traffic_light):
        if traffic_light.current_light == "green":
            self.car.forward(self.speed)
        elif traffic_light.current_light == "yellow":
            self.car.forward(self.speed / 2)  # Slow down
        else:
            self.car.setx(self.car.xcor())  # Stop


# Create cars
cars = [Car(random.choice(["red", "blue", "green", "yellow", "orange"]), random.randint(5, 20)) for _ in range(5)]

# Create traffic lights
traffic_light = TrafficLight()


# Main loop
def run_simulation():
    for car in cars:
        car.move(traffic_light)
    screen.ontimer(run_simulation, 100)  # Repeat every 100ms


# Start the traffic light and simulation
traffic_light.change_light()
run_simulation()

# Main event loop
turtle.mainloop()
# Main event loop
turtle.mainloop()