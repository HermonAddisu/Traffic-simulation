import tkinter as tk
import random

class TrafficLightSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Traffic Light Simulation")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack()

        self.cars = []
        self.light_color = "red"
        self.create_traffic_light()
        self.reset_simulation()

    def create_traffic_light(self):
        self.canvas.create_rectangle(50, 50, 100, 150, fill="black")
        self.red_light = self.canvas.create_oval(60, 60, 90, 90, fill="red")
        self.yellow_light = self.canvas.create_oval(60, 100, 90, 130, fill="grey")
        self.green_light = self.canvas.create_oval(60, 140, 90, 170, fill="grey")

    def create_cars(self):
        for _ in range(10):
            x = random.randint(-30, 600)
            lane = random.choice([1, 2, 3])
            y = 300 - (lane - 1) * 40
            color = random.choice(["blue", "green", "red", "yellow"])
            car = self.canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)
            self.cars.append(car)

    def update_traffic_light(self):
        if self.light_color == "red":
            self.light_color = "green"
            self.canvas.itemconfig(self.red_light, fill="grey")
            self.canvas.itemconfig(self.green_light, fill="green")
        elif self.light_color == "green":
            self.light_color = "yellow"
            self.canvas.itemconfig(self.green_light, fill="grey")
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
        else:
            self.light_color = "red"
            self.canvas.itemconfig(self.yellow_light, fill="grey")
            self.canvas.itemconfig(self.red_light, fill="red")

        self.master.after(2000, self.update_traffic_light)

    def move_cars(self):
        for car in self.cars:
            if self.light_color == "green":
                self.canvas.move(car, 5, 0)
            elif self.light_color == "yellow":
                self.canvas.move(car, 2, 0)

            if self.canvas.coords(car)[0] > 600:
                self.reset_car(car)

        self.master.after(100, self.move_cars)

    def reset_car(self, car):
        x = -30
        lane = random.choice([1, 2, 3])
        y = 300 - (lane - 1) * 40
        self.canvas.coords(car, x, y, x + 30, y + 30)

    def reset_simulation(self):
        self.canvas.delete("all")
        self.cars.clear()
        self.light_color = "red"
        self.create_traffic_light()
        self.create_cars()
        self.update_traffic_light()
        self.move_cars()

if __name__ == "__main__":
    root = tk.Tk()
    simulation = TrafficLightSimulation(root)
    root.mainloop()