import tkinter as tk
import random

# Constants
WIDTH = 800
HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 30
GREEN_DURATION = 3000  # milliseconds
YELLOW_DURATION = 1000  # milliseconds
RED_DURATION = 3000  # milliseconds

class TrafficLight:
    def __init__(self, canvas):
        self.canvas = canvas
        self.state = "green"
        self.light = self.canvas.create_rectangle(700, 200, 740, 320, fill="red")
        self.change_light()

    def change_light(self):
        if self.state == "green":
            self.canvas.itemconfig(self.light, fill="green")
            self.state = "yellow"
            self.canvas.after(GREEN_DURATION, self.change_light)
        elif self.state == "yellow":
            self.canvas.itemconfig(self.light, fill="yellow")
            self.state = "red"
            self.canvas.after(YELLOW_DURATION, self.change_light)
        else:  # yellow
            self.canvas.itemconfig(self.light, fill="red")
            self.state = "green"
            self.canvas.after(RED_DURATION, self.change_light)

class Car:
    def __init__(self, canvas, traffic_light):
        self.canvas = canvas
        self.traffic_light = traffic_light
        self.car = self.canvas.create_rectangle(0, random.randint(50, HEIGHT - 50), CAR_WIDTH, random.randint(50, HEIGHT - 50) + CAR_HEIGHT, fill="blue")
        self.speed = 5

    def move(self):
        if self.traffic_light.state == "yellow":
            self.canvas.move(self.car, self.speed, 0)  # Move normally
        elif self.traffic_light.state == "red":
            self.canvas.move(self.car, self.speed / 2, 0)  # Slow down
        elif self.traffic_light.state == "green":
            # Stop the car by not moving
            pass

class TrafficSimulation:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
        self.canvas.pack()
        self.traffic_light = TrafficLight(self.canvas)
        self.cars = [Car(self.canvas, self.traffic_light) for _ in range(5)]
        self.update()

    def update(self):
        for car in self.cars:
            car.move()
        self.canvas.after(100, self.update)  # Update every 100 ms

# Create the main window
root = tk.Tk()
root.title("Traffic Light Simulation")
simulation = TrafficSimulation(root)
root.mainloop()