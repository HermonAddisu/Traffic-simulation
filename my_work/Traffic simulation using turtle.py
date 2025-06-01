import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.title("Traffic Simulation")
screen.bgcolor("lightblue")

# Constants
NUM_VEHICLES = 15
ROUNDABOUT_RADIUS = 150
GREEN_LIGHT_DURATION = 5
YELLOW_LIGHT_DURATION = 1
RED_LIGHT_DURATION = 5

# Traffic light class
class TrafficLight:
    def __init__(self, position):
        self.light = turtle.Turtle()
        self.light.penup()
        self.light.goto(position)
        self.state = "red"
        self.light.shape("circle")
        self.light.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.change_light()

    def change_light(self):
        if self.state == "red":
            self.light.color("red")
            self.state = "green"
            screen.ontimer(self.change_light, GREEN_LIGHT_DURATION * 1000)
        elif self.state == "green":
            self.light.color("green")
            self.state = "yellow"
            screen.ontimer(self.change_light, YELLOW_LIGHT_DURATION * 1000)
        else:
            self.light.color("yellow")
            self.state = "red"
            screen.ontimer(self.change_light, RED_LIGHT_DURATION * 1000)

# Vehicle class
class Vehicle:
    def __init__(self):
        self.car = turtle.Turtle()
        self.car.shape("square")
        self.car.penup()
        self.car.color(random.choice(["red", "blue", "yellow", "green", "orange"]))
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.angle = random.randint(0, 360)  # Random starting angle
        self.speed = random.uniform(2, 4)  # Increased speed for better flow
        self.car.setheading(self.angle)

        # Set initial position
        self.update_position()

    def update_position(self):
        x = ROUNDABOUT_RADIUS * math.cos(math.radians(self.angle))
        y = ROUNDABOUT_RADIUS * math.sin(math.radians(self.angle))
        self.car.goto(x, y)

    def move(self):
        if simulation.traffic_light.state == "green":
            self.angle += self.speed  # Change angle for circular movement
            if self.angle >= 360:
                self.angle -= 360  # Keep angle within 0-360 degrees
        elif simulation.traffic_light.state == "yellow":
            self.angle += self.speed * 0.5  # Slow down during yellow
        # No movement during red
        self.update_position()

# Simulation class
class TrafficSimulation:
    def __init__(self):
        self.vehicles = []
        self.traffic_light = TrafficLight((0, 200))
        self.running = True

    def create_vehicles(self):
        for _ in range(NUM_VEHICLES):
            vehicle = Vehicle()
            self.vehicles.append(vehicle)

    def check_collisions(self):
        for i in range(len(self.vehicles)):
            for j in range(i + 1, len(self.vehicles)):
                if self.vehicles[i].car.distance(self.vehicles[j].car) < 20:
                    self.vehicles[i].car.color("black")
                    self.vehicles[j].car.color("black")

    def update(self):
        if self.running:
            self.check_collisions()
            for vehicle in self.vehicles:
                vehicle.move()
            screen.ontimer(self.update, 100)  # Update more frequently

    def start(self):
        self.create_vehicles()
        self.update()

# User controls
def toggle_simulation():
    simulation.running = not simulation.running

# Draw roundabout
def draw_roundabout():
    roundabout = turtle.Turtle()
    roundabout.penup()
    roundabout.goto(0, -ROUNDABOUT_RADIUS)
    roundabout.pendown()
    roundabout.color("black")
    roundabout.circle(ROUNDABOUT_RADIUS)
    roundabout.hideturtle()

# Initialize simulation
draw_roundabout()
simulation = TrafficSimulation()
simulation.traffic_light.change_light()  # Start the traffic light cycle
simulation.start()

# Keyboard controls
screen.listen()
screen.onkey(toggle_simulation, "space")  # Press space to start/stop

# Start simulation loop
turtle.done()