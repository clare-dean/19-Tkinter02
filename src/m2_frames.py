import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (2 pts)
#
#   Now, create a frame called frm_a and add a label called lbl_a to it that
#   contains the text "Frame A".
#
#   Make sure you call the pack() method on your widgets.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 3. (2 pts)
#
#   Now, create a frame called frm_b and add a label called lbl_b to it that
#   contains the text "Frame B".
#
#   Make sure you call the pack() method on your widgets.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 4. (1 pt)
#
#   Now, edit your frames to have different background colors. You can choose
#   the colors, but they must both be different.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 5. (1 pt)
#
#   Now, edit frm_b to have one of the reliefs that we looked at in our code
#   along.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("My Window")

frm_a = tk.Frame(window, bg="white")
frm_a.pack()
lbl_a = tk.Label(frm_a, text="Frame A")
lbl_a.pack()

frm_b = tk.Frame(window, bg="blue", relief=tk.SUNKEN)
frm_b.pack()  
lbl_b = tk.Label(frm_b, text="Frame B")
lbl_b.pack()

window.mainloop()


