# Tkinter notes
# Updated Jun 7 2018



########################################################################
# Essentials
########################################################################

# Import tkinter
from tkinter import *

# Make blank window
my_window = Tk()
# my_window is the <window_handle>
# Standard convention: root = Tk()

# Update window
<window_handle>.mainloop()

# Make a frame (invisible container which divides window)
my_frame = Frame(<window_handle>, width=<widthval>, height=<heightval>)
# my_frame is the <frame_handle>
# Ommitting row=<rowval> or col=<colval> sets it to the default value (size of <window_handle>)
# <window_handle> will be resized if <widthval> or <heightval> exceed the current value(s)
# Note that you can also put a <frame_handle> in place of the <window_handle>
# FRAMES MUST BE PLACED WITH EITHER .pack() OR .grid() TO RENDER!



########################################################################
# Widgets
########################################################################

# ----- Creation ----- #
# WIDGETS MUST BE PLACED WITH EITHER .pack() OR .grid() TO RENDER!

# Make a text label
my_label = Label(<frame_handle>,text="message goes here", <text_options>)
# my_label is the <widget_handle>
# Note that you can also put a <window_handle> in place of the <frame_handle>

# Make an image label
my_img = PhotoImage(file="<filename>")
my_img_label = Label(<frame_handle>, image=my_img)
my_img_label.photo = my_img
# my_img_label is the <widget_handle>

# Make a dynamic text label
my_text = StringVar()
Label(<frame_handle>, textvariable=my_text)
my_text.set("New text")

# Make a button
my_button = Button(<frame_handle>, text="button text goes here", <text_options>, <function_options>)
# my_button is the <widget_handle>
# Note that you can also put a <window_handle> in place of the <frame_handle>

# Make a text input box
my_input_box = Entry(<frame_handle>)
# my_input_box is the <widget_handle>
# Note that you can also put a <window_handle> in place of the <frame_handle>

# Make a checkbox
my_checkbox = Checkbutton(<frame_handle>, text="this will appear to right", <text_options>)
# my_checkbox is the <widget_handle>
# Note that you can also put a <window_handle> in place of the <frame_handle>
# STRONGLY RECOMMENDED to combine with my_checkbox.grid(columnspan=2) if using .grid()


# ----- Layout with .pack() ----- #

# Pin widget to default location (top)
<widget_handle>.pack()
# If this is the only .pack() statement, will pack window tight around widget

# Pin widget to specific side of window/frame
<widget_handle>.pack(side=<SIDE>)
# Parameters for <SIDE> include TOP, BOTTOM, LEFT, RIGHT

# Make widget span length of window/frame/space
<widget_handle>.pack(fill=<DIM>)
# Parameters for <DIM> include X, Y, BOTH


# ----- Layout with .grid() ----- #

# Position an item in the grid
<widget_handle>.grid(row=<rowval>, column=<colval>)
# Values for <rowval> and <colval> begin at 0
# Ommitting row=<rowval> or col=<colval> sets it to the default value (0)

# Make a widget span multiple rows/columns
<widget_handle>.grid(rowspan=<rowspanval>, columnspan=<colspanval>)
# Values for <rowspanval> and <colspanval> begin at 1
# Ommitting row=<rowval> or col=<colval> sets it to the default value (1)


# ----- Text Formatting ----- #

# Pin text to specific side of widget
<exmaple_widget> = Widget(<widget_options>, sticky=<DIR>)
# Parameters for <DIR> include N, E, S, W

# Change font of text
<example_widget> = Widget(<widget_options>, font=("<font_name>",16))
# Parameters for <font_name> include Courier, Helvetica, ...


# -----  Coloring ----- #

# Color text
<exmaple_widget> = Widget(<widget_options>, fg = "<color>")
# Parameters for <color> include red, blue, green, purple, ...

# Color widget
<exmaple_widget> = Widget(<widget_options>, bg = "<color>")
# Parameters for <color> include red, blue, green, purple, ...



########################################################################
# Functions
########################################################################


# ------ Binding (no events) ------ #

# Define a function with no event dependency
def my_function():
    <function_body>
# <my_function> is the <function_handle>

# Bind a function to widget directly
<example_widget> = Widget(<widget_options>, <text_options>, command=<function_handle>)
# The function defined by <function_handle> will execute when the widget's event occurs


# ------ Binding (events) ------ #

# Define a function with event dependency
def my_function(<event_handle>):
    <function_body>
# <my_function> is the <function_handle>

# Bind a function to widget via event
<widget_handle>.bind("<event>", <function_handle>)
# Parameters for <event> include:
#   < > MUST BE INCLUDED!
#   <Button-1> - Left mouse click
#   <Button-2> - Middle mouse click (scroll wheel)
#   <Button-3> - Right mouse click
# Note that you can also put a <frame_handle> in place of the <widget_handle>
