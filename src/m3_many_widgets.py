import tkinter as tk

###############################################################################
window = tk.Tk()
window.title("Practice Widgets")

frame1 = tk.Frame(window)
frame1.pack(side=tk.LEFT, padx=10, pady=10)

label1 = tk.Label(frame1, text="Frame 1 Label")
label1.pack()

button1 = tk.Button(frame1, text="Frame 1 Button")
button1.pack()

entry1 = tk.Entry(frame1, width=30)
entry1.pack()

frame2 = tk.Frame(window)
frame2.pack(side=tk.RIGHT, padx=10, pady=10)

label2 = tk.Label(frame2, text="Frame 2 Label")
label2.pack()

text2 = tk.Text(frame2, width=30, height=5)
text2.pack()

window.mainloop()