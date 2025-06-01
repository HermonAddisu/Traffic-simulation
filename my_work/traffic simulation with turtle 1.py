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
        elif self.state == "green":
            self.light.color("green")
            self.state = "yellow"
        else:
            self.light.color("yellow")
            self.state = "red"

# Vehicle class
class Vehicle:
    def __init__(self):
        self.car = turtle.Turtle()
        self.car.shape("square")
        self.car.penup()
        self.car.color(random.choice(["red", "blue", "yellow", "green", "orange"]))
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.angle = random.randint(0, 360)  # Random starting angle
        self.speed = random.uniform(1, 3)  # Random speed
        self.car.setheading(self.angle)

        # Set initial position
        self.update_position()

    def update_position(self):
        x = ROUNDABOUT_RADIUS * math.cos(math.radians(self.angle))
        y = ROUNDABOUT_RADIUS * math.sin(math.radians(self.angle))
        self.car.goto(x, y)

    def move(self):
        self.angle += self.speed  # Change angle for circular movement
        if self.angle >= 360:
            self.angle -= 360  # Keep angle within 0-360 degrees
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
            if self.traffic_light.state == "green":
                for vehicle in self.vehicles:
                    vehicle.move()
            self.traffic_light.change_light()
            screen.ontimer(self.update, 3000)  # Update every 3 seconds

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
simulation.start()

# Keyboard controls
screen.listen()
screen.onkey(toggle_simulation, "space")  # Press space to start/stop

# Start simulation loop
turtle.done()