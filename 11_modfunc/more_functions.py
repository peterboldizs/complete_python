import math
import tkinter


def parabola(x):
    y = x * x
    return y


def parabola2(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius, g, h):
    for x in range(g, g + radius):
        y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_orig = page.winfo_width() / 2
    y_orig = page.winfo_height() / 2
    page.configure(scrollregion=(-x_orig, -y_orig, x_orig, y_orig))
    page.create_line(-x_orig, 0, x_orig, 0, fill="black")
    page.create_line(0, y_orig, 0, -y_orig, fill="black")
    print("locals", locals())


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")


for i in range(-10, 10):
    j = parabola(i)
    print("{} -> {}".format(i, j))

main_window = tkinter.Tk()
main_window.title("Parabola")
main_window.geometry("640x480")

canvas = tkinter.Canvas(main_window, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axes(canvas)
print(repr(canvas))

parabola2(canvas, 100)
parabola2(canvas, 200)
circle(canvas, 100, 100, 100)

main_window.mainloop()
