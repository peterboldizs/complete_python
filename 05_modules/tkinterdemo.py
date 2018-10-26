import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()
main_window = tkinter.Tk()
main_window.title("Hello TK")
main_window.geometry('640x480')

label = tkinter.Label(main_window, text="This is my first GUI")
label.pack(side='top')

left_frame = tkinter.Frame(main_window)
left_frame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=3)
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)
canvas.pack(side='top')

right_frame = tkinter.Frame(main_window)
right_frame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(right_frame, text="First")
button2 = tkinter.Button(right_frame, text="Second")
button3 = tkinter.Button(right_frame, text="Third")
button1.pack(side='top')
button3.pack(side='top')
button2.pack(side='top')

main_window.mainloop()
