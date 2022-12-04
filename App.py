from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab
from k_nearest_neighbor import *


# App run handwritten recognition task
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.x = self.y = 0

        # Creating elements
        self.canvas = tk.Canvas(self, width=200, height=200, bg="white", cursor="cross")
        self.label = tk.Label(self, text="Draw..", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text="Recognise", command=self.classify_handwriting)
        self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)
        self.inputtext = Text(self, height=1, width=2, bg="light yellow")
        self.button_mistake = tk.Button(self, text="Wrong", command=self.adaptive_mechanism)

        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=0, column=1, pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)
        self.inputtext.grid(row=1, column=3, pady=2)
        self.button_mistake.grid(row=1, column=2, pady=2)

        # self.canvas.bind("<Motion>", self.start_pos)
        self.canvas.bind("<B1-Motion>", self.draw_lines)

    # This function is created to learn from mistake. Manually learn when press button "wrong"
    def adaptive_mechanism(self):
        # Get input from the text box (The correct input for the mistake one inputted by user)
        INPUT = self.inputtext.get("1.0", "end-1c")
        self.inputtext.delete('1.0', END)

        if INPUT.isnumeric():
            if 0 <= int(INPUT) <= 9:
                HWND = self.canvas.winfo_id()  # get the handle of the canvas
                rect = win32gui.GetWindowRect(HWND)  # get the coordinate of the canvas
                a, b, c, d = rect
                rect = (a + 4, b + 4, c - 4, d - 4)
                img = ImageGrab.grab(rect)
                vector = get_vector(img)

                # Just deal with dirty input
                if len(set(vector)) != 1:
                    print(INPUT)
                    print(get_vector(img))
                    # Add mistake one into memory
                    data.append(vector)
                    label.append(int(INPUT))

    def clear_all(self):
        self.canvas.delete("all")

    def classify_handwriting(self):
        HWND = self.canvas.winfo_id()  # get the handle of the canvas
        rect = win32gui.GetWindowRect(HWND)  # get the coordinate of the canvas
        a, b, c, d = rect
        rect = (a + 4, b + 4, c - 4, d - 4)
        im = ImageGrab.grab(rect)

        digit, acc = predict_digit(im)
        # self.label.configure(text=str(digit) + ', ' + str(int(acc * 1)))
        self.label.configure(text=str(digit))

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r = 8
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill='black')


# Load training data
load_data("mnist.txt")
load_data("experience.txt")
last_index = load_data("advanced_experience.txt")
app = App()
mainloop()
# Write some "experience" to specific file
write_data("experience.txt", last_index)
