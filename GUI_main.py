#!/usr/bin/env python

from tkinter import *
import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import time


########################################################################
# ----- Author Info ----- #

__author__ = "Julian Lambert"
__copyright__ = "'Copyright' 2018, LASP"
#__license__ = "MIT"
__version__ = "0.0.3"
__maintainer__ = "Julian Lambert"
__email__ = "julian.lambert@colorado.edu"
__status__ = "Development"


########################################################################
# ----- Setup ----- #

# Define resolution of Raspi
master_width = 800
master_height = 480

# Create root window
root = Tk()
root.title('Square Tank GUI')
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(master_width, master_height))

# Define geometry for frame partitions
num_frame_rows = 3
num_frame_cols = 2
frame_width = master_width/num_frame_cols
frame_height = master_height/num_frame_rows

# Define formatting for frame partitions
frame_bw = 5                    # border width
frame_color = 'lightsteelblue'  # background color

# Define frames
settings_frame = Frame(root, width=frame_width, height=frame_height, bg=frame_color, bd=frame_bw, relief=GROOVE)
sensor_1_frame = Frame(root, width=frame_width, height=frame_height, bg=frame_color, bd=frame_bw, relief=RAISED)
sensor_2_frame = Frame(root, width=frame_width, height=frame_height, bg=frame_color, bd=frame_bw, relief=RAISED)
sensor_3_frame = Frame(root, width=frame_width, height=frame_height, bg=frame_color, bd=frame_bw, relief=RAISED)
sensor_4_frame = Frame(root, width=frame_width, height=frame_height, bg=frame_color, bd=frame_bw, relief=RAISED)
sensor_5_fra,me = Frame(root, width=frame_width, height=frame_height, bg=frame_color, bd=frame_bw, relief=RAISED)



########################################################################
# ----- Frame formatting ----- #

field_color = 'aliceblue'   # textbox color

# Format settings/datetime frame
settings_frame.grid_propagate(False)
curr_date = StringVar()
curr_time = StringVar()
settings_label = Label(settings_frame, text="Settings", font=("Courier", 40), bg=frame_color, relief=RAISED)
date_label = Label(settings_frame, textvariable=curr_date, font=("Courier", 15), bg=frame_color)
time_label = Label(settings_frame, textvariable=curr_time, font=("Courier", 15), bg=frame_color)
# Center date/time labels
settings_label.grid(row=2, column=1, sticky=NSEW)
date_label.grid(row=0, column=0, sticky=NSEW)
time_label.grid(row=0, column=2, sticky=NSEW)
settings_frame.grid_rowconfigure(1, weight=1)
settings_frame.grid_rowconfigure(3, weight=1)
settings_frame.grid_columnconfigure(0, weight=1)
settings_frame.grid_columnconfigure(2, weight=1)

# Define sensor frame fields
# Sensor 1
sensor_1_frame.grid_propagate(False)
title_1_text = "Cryo Gauge"
title_1 = Label(sensor_1_frame, text=title_1_text, font=("Courier", 15), relief=RIDGE, bg=field_color)
graph_1 = Label(sensor_1_frame, text="<beautiful_graph.png>", font=("Courier", 13), relief=RIDGE)
info_1 = Label(sensor_1_frame, text="0 torr", font=("Courier", 40), relief=RIDGE, bg=field_color)
info_1.grid(rowspan=5)
status_1 = Label(sensor_1_frame, text="Status: READY", font=("Courier",12), relief=RIDGE, bg='lightgreen')
# Alignment
title_1.grid(row=1, column=1, sticky=NSEW)
graph_1.grid(row=3, column=1, sticky=NSEW)
info_1.grid(row=1, column=3, sticky=NSEW)
status_1.grid(row=5, column=1, sticky=NSEW)
sensor_1_frame.grid_rowconfigure(0, weight=1)
sensor_1_frame.grid_rowconfigure(2, weight=1)
sensor_1_frame.grid_rowconfigure(3, weight=3)
sensor_1_frame.grid_rowconfigure(4, weight=1)
sensor_1_frame.grid_rowconfigure(6, weight=1)
sensor_1_frame.grid_columnconfigure(0, weight=1)
sensor_1_frame.grid_columnconfigure(2, weight=3)
sensor_1_frame.grid_columnconfigure(4, weight=3)

# Sensor 2
sensor_2_frame.grid_propagate(False)
title_2_text = "Rough Line Gauge"
title_2 = Label(sensor_2_frame, text=title_2_text, font=("Courier", 15), relief=RIDGE, bg=field_color)
graph_2 = Label(sensor_2_frame, text="<beautiful_graph.png>", font=("Courier", 13), relief=RIDGE)
info_2 = Label(sensor_2_frame, text="0 torr", font=("Courier", 40), relief=RIDGE, bg=field_color)
info_2.grid(rowspan=5)
status_2 = Label(sensor_2_frame, text="Status: CLOSED", font=("Courier",12), relief=RIDGE, bg='red')
# Alignment
title_2.grid(row=1, column=1, sticky=NSEW)
graph_2.grid(row=3, column=1, sticky=NSEW)
info_2.grid(row=1, column=3, sticky=NSEW)
status_2.grid(row=5, column=1, sticky=NSEW)
sensor_2_frame.grid_rowconfigure(0, weight=1)
sensor_2_frame.grid_rowconfigure(2, weight=1)
sensor_2_frame.grid_rowconfigure(3, weight=3)
sensor_2_frame.grid_rowconfigure(4, weight=1)
sensor_2_frame.grid_rowconfigure(6, weight=1)
sensor_2_frame.grid_columnconfigure(0, weight=1)
sensor_2_frame.grid_columnconfigure(2, weight=3)
sensor_2_frame.grid_columnconfigure(4, weight=3)

# Sensor 3
sensor_3_frame.grid_propagate(False)
title_3_text = "Tank Gauge"
title_3 = Label(sensor_3_frame, text=title_3_text, font=("Courier", 15), relief=RIDGE, bg=field_color)
graph_3 = Label(sensor_3_frame, text="<beautiful_graph.png>", font=("Courier", 13), relief=RIDGE)
info_3 = Label(sensor_3_frame, text="0 torr", font=("Courier", 40), relief=RIDGE, bg=field_color)
info_3.grid(rowspan=5)
status_3 = Label(sensor_3_frame, text="Status: CLOSED", font=("Courier",12), relief=RIDGE, bg='red')
# Alignment
title_3.grid(row=1, column=1, sticky=NSEW)
graph_3.grid(row=3, column=1, sticky=NSEW)
info_3.grid(row=1, column=3, sticky=NSEW)
status_3.grid(row=5, column=1, sticky=NSEW)
sensor_3_frame.grid_rowconfigure(0, weight=1)
sensor_3_frame.grid_rowconfigure(2, weight=1)
sensor_3_frame.grid_rowconfigure(3, weight=3)
sensor_3_frame.grid_rowconfigure(4, weight=1)
sensor_3_frame.grid_rowconfigure(6, weight=1)
sensor_3_frame.grid_columnconfigure(0, weight=1)
sensor_3_frame.grid_columnconfigure(2, weight=3)
sensor_3_frame.grid_columnconfigure(4, weight=3)

# Sensor 4
sensor_4_frame.grid_propagate(False)
title_4_text = "Aux Gauge 1"
title_4 = Label(sensor_4_frame, text=title_4_text, font=("Courier", 15), relief=RIDGE, bg=field_color)
graph_4 = Label(sensor_4_frame, text="<beautiful_graph.png>", font=("Courier", 13), relief=RIDGE)
info_4 = Label(sensor_4_frame, text="0 torr", font=("Courier", 40), relief=RIDGE, bg=field_color)
info_4.grid(rowspan=5)
status_4 = Label(sensor_4_frame, text="Status: READY", font=("Courier",12), relief=RIDGE, bg='lightgreen')
# Alignment
title_4.grid(row=1, column=1, sticky=NSEW)
graph_4.grid(row=3, column=1, sticky=NSEW)
info_4.grid(row=1, column=3, sticky=NSEW)
status_4.grid(row=5, column=1, sticky=NSEW)
sensor_4_frame.grid_rowconfigure(0, weight=1)
sensor_4_frame.grid_rowconfigure(2, weight=1)
sensor_4_frame.grid_rowconfigure(3, weight=3)
sensor_4_frame.grid_rowconfigure(4, weight=1)
sensor_4_frame.grid_rowconfigure(6, weight=1)
sensor_4_frame.grid_columnconfigure(0, weight=1)
sensor_4_frame.grid_columnconfigure(2, weight=3)
sensor_4_frame.grid_columnconfigure(4, weight=3)

# Sensor 5
sensor_5_frame.grid_propagate(False)
title_5_text = "Aux Gauge 2"
title_5 = Label(sensor_5_frame, text=title_5_text, font=("Courier", 15), relief=RIDGE, bg=field_color)
graph_5 = Label(sensor_5_frame, text="<beautiful_graph.png>", font=("Courier", 13), relief=RIDGE)
info_5 = Label(sensor_5_frame, text="0 torr", font=("Courier", 40), relief=RIDGE, bg=field_color)
info_5.grid(rowspan=5)
status_5 = Label(sensor_5_frame, text="Status: READY", font=("Courier", 12), relief=RIDGE, bg='lightgreen')
# Alignment
title_5.grid(row=1, column=1, sticky=NSEW)
graph_5.grid(row=3, column=1, sticky=NSEW)
info_5.grid(row=1, column=3, sticky=NSEW)
status_5.grid(row=5, column=1, sticky=NSEW)
sensor_5_frame.grid_rowconfigure(0, weight=1)
sensor_5_frame.grid_rowconfigure(2, weight=1)
sensor_5_frame.grid_rowconfigure(3, weight=3)
sensor_5_frame.grid_rowconfigure(4, weight=1)
sensor_5_frame.grid_rowconfigure(6, weight=1)
sensor_5_frame.grid_columnconfigure(0, weight=1)
sensor_5_frame.grid_columnconfigure(2, weight=3)
sensor_5_frame.grid_columnconfigure(4, weight=3)

# Format frame positions
sensor_1_frame.grid(row=0, column=0)
sensor_2_frame.grid(row=0, column=1)
sensor_3_frame.grid(row=1, column=0)
sensor_4_frame.grid(row=1, column=1)
sensor_5_frame.grid(row=2, column=0)
settings_frame.grid(row=2, column=1)




########################################################################
# ----- Updating and Events ----- #

# Define function for tagging multiple widgets to group elements on a button
def retag(tag, *args):
    for widget in args:
        widget.bindtags((tag,) + widget.bindtags())

# Tag widgets in sensor frames
retag("sensor_1", sensor_1_frame, title_1, graph_1, info_1, status_1)
retag("sensor_2", sensor_2_frame, title_2, graph_2, info_2, status_2)
retag("sensor_3", sensor_3_frame, title_3, graph_3, info_3, status_3)
retag("sensor_4", sensor_4_frame, title_4, graph_4, info_4, status_4)
retag("sensor_5", sensor_5_frame, title_5, graph_5, info_5, status_5)

# Define event for getting date and time (this will happen automatically with root.after())
def get_datetime():
    curr_date.set(time.strftime("%Y-%m-%d"))
    curr_time.set(time.strftime("%H:%M:%S"))
    root.after(refresh_rate, get_datetime)

# Define event functions (for viewing in-depth info about gauges)
def get_info_1(inquire_1):
    sensor_1_frame.config(relief=SUNKEN)
def cancel_get_info_1(cancel_1):
    sensor_1_frame.config(relief=RAISED)
inquire_1 = sensor_1_frame.bind_class("sensor_1", "<Button-1>", get_info_1)
cancel_1 = sensor_1_frame.bind_class("sensor_1", "<ButtonRelease-1>", cancel_get_info_1)

def get_info_2(inquire_2):
    sensor_2_frame.config(relief=SUNKEN)
def cancel_get_info_2(cancel_2):
    sensor_2_frame.config(relief=RAISED)
inquire_2 = sensor_2_frame.bind_class("sensor_2", "<Button-1>", get_info_2)
cancel_2 = sensor_2_frame.bind_class("sensor_2", "<ButtonRelease-1>", cancel_get_info_2)

def get_info_3(inquire_3):
    sensor_3_frame.config(relief=SUNKEN)
def cancel_get_info_3(cancel_3):
    sensor_3_frame.config(relief=RAISED)
inquire_3 = sensor_3_frame.bind_class("sensor_3", "<Button-1>", get_info_3)
cancel_3 = sensor_3_frame.bind_class("sensor_3", "<ButtonRelease-1>", cancel_get_info_3)

def get_info_4(inquire_4):
    sensor_4_frame.config(relief=SUNKEN)
def cancel_get_info_4(cancel_4):
    sensor_4_frame.config(relief=RAISED)
inquire_4 = sensor_4_frame.bind_class("sensor_4", "<Button-1>", get_info_4)
cancel_4 = sensor_4_frame.bind_class("sensor_4", "<ButtonRelease-1>", cancel_get_info_4)

def get_info_5(inquire_5):
    sensor_5_frame.config(relief=SUNKEN)
def cancel_get_info_5(cancel_5):
    sensor_5_frame.config(relief=RAISED)
inquire_5 = sensor_5_frame.bind_class("sensor_5", "<Button-1>", get_info_5)
cancel_5 = sensor_5_frame.bind_class("sensor_5", "<ButtonRelease-1>", cancel_get_info_5)

# Define event functions (for viewing in-depth info about gauges)
def change_settings(settings_inquire):
    settings_label.config(relief=SUNKEN)
def cancel_change_settings(cancel_settings):
    settings_label.config(relief=RAISED)
settings_inquire = settings_label.bind("<Button-1>", change_settings)
cancel_settings = settings_label.bind("<ButtonRelease-1>", cancel_change_settings)

# Update window
refresh_rate = 1000 # ms until next refresh (for clock)
root.after(refresh_rate, get_datetime)
root.mainloop()

"""
# Testing matplotlib stuff
class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page Test", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", controller.show_frame(StartPage))

        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side-tk.TOP, fill=tk.BOTH, expand=TRUE)
        
        
    ani = animation.FuncAnimation(f, animate, interval=1000)

"""

""" testing Github repo """