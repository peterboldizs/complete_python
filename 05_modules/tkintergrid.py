import tkinter

# this is the same as tkinterdemo but uses grid instead of pack

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()
main_window = tkinter.Tk()
main_window.title("Hello TK")
main_window.geometry('640x480-8-200')

label = tkinter.Label(main_window, text="This is my second GUI")
label.grid(row=0, column=0)

left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=3)
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)
canvas.grid(row=1, column=0)

right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(right_frame, text="First")
button2 = tkinter.Button(right_frame, text="Second")
button3 = tkinter.Button(right_frame, text="Third")
button1.grid(row=0, column=0)
button3.grid(row=1, column=0)
button2.grid(row=2, column=0)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)

left_frame.config(relief='sunken', borderwidth=1)
right_frame.config(relief='sunken', borderwidth=1)
left_frame.grid(sticky='ns')
right_frame.grid(sticky='new')
right_frame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')
main_window.mainloop()
