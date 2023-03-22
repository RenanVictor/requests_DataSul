import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My Window")

# Create a frame to contain the labels, buttons, and entry fields
frame = tk.Frame(window)
frame.pack()

# Create the labels
label1 = tk.Label(frame, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(frame, text="Label 2")
label2.grid(row=1, column=0)

# Create the entry fields
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1)

# Create the buttons
button1 = tk.Button(frame, text="Button 1")
button1.grid(row=2, column=0)

button2 = tk.Button(frame, text="Button 2")
button2.grid(row=2, column=1)

# Run the window
window.mainloop()
