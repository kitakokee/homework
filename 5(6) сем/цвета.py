import tkinter as tk

def hex_to_rgb(hex_color):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return r, g, b

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def complementary_color(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    comp_color = rgb_to_hex(255 - r, 255 - g, 255 - b)
    return comp_color

class ColorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Цвет и комплементарный цвет")

        self.canvas = tk.Canvas(root, width=300, height=200)
        self.canvas.pack()

        self.color_entry = tk.Entry(root, bg="#ffffff", width=10)
        self.color_entry.insert(0, '#ff0000')  
        self.color_entry.pack()

        self.update_button = tk.Button(root, text="Другой цвет", command=self.display_colors)
        self.update_button.pack()

        self.display_colors()


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorApp(root)
    root.mainloop()