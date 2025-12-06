import tkinter as tk
import random

WIDTH, HEIGHT = 300, 500
CAR_WIDTH, CAR_HEIGHT = 40, 40
OBST_WIDTH, OBST_HEIGHT = 40, 40
LINE_1_X, LINE_2_X = -100, 100
START_OBST_Y = 200
CAR_START_Y = -100

class CarGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
        self.canvas.pack()

        self.line = 1
        self.carx = LINE_1_X
        self.cary = CAR_START_Y

        self.obst1x = LINE_1_X
        self.obsty = START_OBST_Y

        # Coordinates adjusted for canvas center; convert Turtle coords to Canvas coords
        self.offset_x = WIDTH // 2
        self.offset_y = HEIGHT // 2

        self.car_id = None
        self.obs_id = None

        self.running = True

        self.root.bind("<a>", self.left)
        self.root.bind("<d>", self.right)
        self.root.bind("<space>", self.auto_switch_keyboard)
        self.canvas.bind("<Button-1>", self.auto_switch_click)

        self.update_game()

    def convert_coords(self, x, y):
        # Convert from Turtle's coordinate system to Tkinter canvas coordinates (origin top-left)
        return x + self.offset_x, self.offset_y - y

    def draw_car(self):
        # Remove previous car
        if self.car_id:
            self.canvas.delete(self.car_id)

        if self.line == 1:
            self.carx = LINE_1_X
        else:
            self.carx = LINE_2_X

        x, y = self.convert_coords(self.carx, self.cary)

        # Draw the car shape similarly to your turtle drawing
        # Use polygon to simulate the filled shape
        points = [
            (x, y),  # bottom left
            (x, y - 40),  # up 40
            (x + 14, y - 40 - 14),  # up-right 20 at 45 degrees (approx)
            (x + 34, y - 40 - 14),  # right 20
            (x + 48, y - 40),  # down-right 20 at 45 degrees
            (x + 48, y),  # down 40
            (x, y)
        ]

        # Flatten points for create_polygon
        flat_points = []
        for px, py in points:
            flat_points.extend([px, py])

        self.car_id = self.canvas.create_polygon(flat_points, fill='black')

    def draw_obstacle(self):
        # Remove previous obstacle
        if self.obs_id:
            self.canvas.delete(self.obs_id)

        x, y = self.convert_coords(self.obst1x + 40, self.obsty)

        # Draw the square obstacle aligned to the car lanes
        self.obs_id = self.canvas.create_rectangle(
            x, y,
            x - OBST_WIDTH, y - OBST_HEIGHT,
            fill='black'
        )

    def update_positions(self):
        # Move the obstacle down
        self.mobsty = self.obsty - 20
        self.obsty = self.mobsty

        if self.obsty <= -120:
            self.obsty = START_OBST_Y
            randint = random.randint(1, 2)
            if randint == 1:
                self.obst1x = LINE_1_X
            else:
                self.obst1x = LINE_2_X

    def check_collision(self):
        # Check if obstacle collides with car
        current_carx = LINE_1_X if self.line == 1 else LINE_2_X
        # Obstacle y overlaps with car y range?
        if self.obst1x == current_carx and self.cary <= self.obsty <= self.cary + CAR_HEIGHT:
            self.running = False

    def update_game(self):
        if not self.running:
            self.root.destroy()
            return

        self.draw_car()
        self.draw_obstacle()
        self.update_positions()
        self.check_collision()

        # Schedule next frame in 200ms
        self.root.after(200, self.update_game)

    def left(self, event=None):
        if self.line == 2:
            self.line = 1
            self.draw_car()

    def right(self, event=None):
        if self.line == 1:
            self.line = 2
            self.draw_car()

    def auto_switch_click(self, event=None):
        if self.line == 1:
            self.line = 2
        else:
            self.line = 1
        self.draw_car()

    def auto_switch_keyboard(self, event=None):
        if self.line == 1:
            self.line = 2
        else:
            self.line = 1
        self.draw_car()

if __name__ == "__main__":
    root = tk.Tk()
    game = CarGame(root)
    root.mainloop()
