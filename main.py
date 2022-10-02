import math
import tkinter as tk
from tkinter import filedialog, ttk
import matplotlib

# noinspection PyProtectedMember
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

from dehyroxy_func import C
from plot_data import radial_profile, temporal_profile

matplotlib.use("TkAgg")

# padding
pdx = 5
pdy = 5

# root window


root = tk.Tk()
root.geometry('600x600')
root.title('Dehydroxylation Calculator')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=0, fill='both', expand=True)


##################
# CALCULATOR FRAME
##################


def solve(r, t, a, conc, D, label):
    r = float(r)/1000
    t = float(t)
    a = float(a)/1000
    conc = float(conc)
    D = float(D)*(1e-4)

    label.config(text=str(C(r, t, a, conc, D)))


calc_frame = ttk.Frame(notebook, width=400, height=200)
calc_frame.pack(fill='both', expand=True)
calc_frame.columnconfigure(0, weight=1)
calc_frame.columnconfigure(1, weight=4)

# Diffusion coefficient entry

dif_label_c = tk.Label(calc_frame, text="Diffusion Coefficient(cm2/s)")
dif_label_c.grid(column=0, row=0)

D_c = tk.StringVar()
D_c.set('1e-7')
dif_entry_c = tk.Entry(calc_frame, textvariable=D_c)
dif_entry_c.grid(column=1, row=0, sticky='EW', pady=pdy, padx=pdx)

# Radius entry

radius_label_c = tk.Label(calc_frame, text="Radius(mm)")
radius_label_c.grid(column=0, row=1)

a_c = tk.StringVar()
a_c.set('50')
radius_entry_c = tk.Entry(calc_frame, textvariable=a_c)
radius_entry_c.grid(column=1, row=1, sticky='EW', pady=pdy, padx=pdx)

# initial concentration entry

init_conc_label_c = tk.Label(calc_frame, text="Initial Concentration(unit)")
init_conc_label_c.grid(column=0, row=2)

conc_c = tk.StringVar()
conc_c.set('100')
conc_entry_c = tk.Entry(calc_frame, textvariable=conc_c)
conc_entry_c.grid(column=1, row=2, sticky='EW', pady=pdy, padx=pdx)

# Time entry

time_label_c = tk.Label(calc_frame, text="Time(s)")
time_label_c.grid(column=0, row=3)

t_c = tk.StringVar()
t_c.set('3600')
time_entry_c = tk.Entry(calc_frame, textvariable=t_c)
time_entry_c.grid(column=1, row=3, sticky='EW', pady=pdy, padx=pdx)

# radial distance entry

r_label_c = tk.Label(calc_frame, text="Radial Dist.")
r_label_c.grid(column=0, row=4)

r_c = tk.StringVar()
r_c.set('45')
r_entry_c = tk.Entry(calc_frame, textvariable=r_c)
r_entry_c.grid(column=1, row=4, sticky='EW', pady=pdy, padx=pdx)

# result label
result_label = tk.Label(calc_frame, text="Concentration = ")
result_label.grid(column=0, row=5, sticky='EW')

result_label_c = tk.Label(calc_frame, text="")
result_label_c.grid(column=1, row=5, columnspan=2, sticky='W')

# calculate button
calc_c = tk.Button(calc_frame, text="Calculate",
                   command=lambda: solve(r_c.get(), t_c.get(), a_c.get(), conc_c.get(), D_c.get(), result_label_c))
calc_c.grid(column=0, columnspan=2, row=6)


###################
# RADIAL PLOT FRAME
###################

# DATA VARIABLE
x_r = None
y_r = None


def plot_radial(figure, figure_canvas_r, t, a, conc, D, n_point_r):
    t = float(t)
    a = float(a)/1000
    conc = float(conc)
    D = float(D)*(1e-4)
    figure.clf()
    axes = figure.add_subplot()
    axes.set_xlim([0, 1.1*a*1000])
    axes.set_ylim([0, 1.1*conc])
    axes.title.set_text(f'Concentration along radius at t = {int(t)} seconds')
    axes.set(xlabel='Radial Distance(mm)', ylabel='Concentration')
    global x_r
    global y_r

    x_r = np.linspace(0, a*1000, num=int(n_point_r))
    y_r = radial_profile(t, a, D, conc, int(n_point_r))

    axes.plot(x_r, y_r)
    figure_canvas_r.draw()


def save_data_r():
    global x_r
    global y_r
    files = [('CSV file', '*.csv'),
             ('All Files', '*.*')]
    f = filedialog.asksaveasfile(initialfile='data.csv', filetypes=files, defaultextension='.csv', mode='w')
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    y = np.array(y_r)
    xy_data = np.array([x_r, y])
    xy_data = xy_data.transpose()
    np.savetxt(f, xy_data, delimiter=',')
    f.close()  # `()` was missing.


radial_plot_frame = ttk.Frame(notebook, width=root.winfo_width(), height=root.winfo_height())
radial_plot_frame.pack(fill='both', expand=True)

radial_plot_frame.rowconfigure(0, weight=6)
radial_plot_frame.rowconfigure(1, weight=1)
radial_plot_frame.rowconfigure(2, weight=1)
radial_plot_frame.rowconfigure(3, weight=1)

radial_plot_frame.columnconfigure(0, weight=1)
radial_plot_frame.columnconfigure(1, weight=2)
radial_plot_frame.columnconfigure(2, weight=1)
radial_plot_frame.columnconfigure(3, weight=2)

# frame for plot
radial_plot = ttk.Frame(radial_plot_frame, width=radial_plot_frame.winfo_width(), height=radial_plot_frame.winfo_height())

# Figure
figure_r = Figure(figsize=(8, 4.5), dpi=100)

# create FigureCanvasTkAgg object
figure_canvas_r = FigureCanvasTkAgg(figure_r, radial_plot)

# create the toolbar
NavigationToolbar2Tk(figure_canvas_r, radial_plot)

# create axes
# axes = figure_r.add_subplot()

figure_canvas_r.get_tk_widget().pack(fill='both', expand=True)

# packing radial_plot frame
radial_plot['borderwidth'] = 1
radial_plot['relief'] = 'solid'
radial_plot.grid(row=0, column=0, columnspan=6, sticky="NSEW", padx=pdx)


# Diffusion coefficient entry

dif_label_r = tk.Label(radial_plot_frame, text="Diffusion Coefficient(cm2/s)")
dif_label_r.grid(column=0, row=1, padx=pdx, pady=pdy, sticky='E')

D_r = tk.StringVar()
D_r.set('1e-9')
dif_entry_r = tk.Entry(radial_plot_frame, textvariable=D_r)
dif_entry_r.grid(column=1, row=1, sticky='W', padx=pdx, pady=pdy)

# Radius entry

dif_label_r = tk.Label(radial_plot_frame, text="Radius(mm)")
dif_label_r.grid(column=2, row=1, padx=pdx, pady=pdy, sticky='E')

a_r = tk.StringVar()
a_r.set('50')
radius_entry_r = tk.Entry(radial_plot_frame, textvariable=a_r)
radius_entry_r.grid(column=3, row=1, sticky='W', padx=pdx, pady=pdy)

# initial concentration entry

init_conc_label_r = tk.Label(radial_plot_frame, text="Initial Concentration")
init_conc_label_r.grid(column=0, row=2, sticky='E', padx=pdx, pady=pdy)

conc_r = tk.StringVar()
conc_r.set('100')
conc_entry_r = tk.Entry(radial_plot_frame, textvariable=conc_r)
conc_entry_r.grid(column=1, row=2, sticky='W', pady=pdy, padx=pdx)

# Time entry

time_label_r = tk.Label(radial_plot_frame, text="Time")
time_label_r.grid(column=2, row=2, padx=pdx, pady=pdy, sticky='E')

t_r = tk.StringVar()
t_r.set('3600')
time_entry_r = tk.Entry(radial_plot_frame, textvariable=t_r)
time_entry_r.grid(column=3, row=2, sticky='W', pady=pdy, padx=pdx)

# No. of points entry
n_point_label_r = tk.Label(radial_plot_frame, text="No. of points")
n_point_label_r.grid(column=0, row=3, padx=pdx, pady=pdy, sticky='E')

n_point_r = tk.StringVar()
n_point_r.set('100')
n_point_entry_r = tk.Entry(radial_plot_frame, textvariable=n_point_r)
n_point_entry_r.grid(column=1, row=3, sticky='W', pady=pdy, padx=pdx)

# calculate button
calc_r = tk.Button(radial_plot_frame, text="Plot",
                   command=lambda: plot_radial(figure_r, figure_canvas_r, t_r.get(),
                                               a_r.get(), conc_r.get(), D_r.get(), n_point_r.get()))
calc_r.grid(column=1, row=4, sticky='EW', padx=pdx, pady=pdy)

# save data button
save_r = tk.Button(radial_plot_frame, text="Save Data", command=lambda: save_data_r())
save_r.grid(column=2, row=4, sticky='EW', padx=pdx, pady=pdy)

#######################
# TEMPORAL PLOT FRAME #
#######################

x_t = None
y_t = None


def plot_temporal(figure, figure_canvas, r, a, T, dT, conc, D):
    r = float(r)/1000 # mm to meter conversion
    a = float(a)/1000 # mm to meter conversion
    conc = float(conc)
    D = float(D)*(1e-4) # cm2/s to m2/s conversion
    T = int(T)
    dT = int(dT)
    figure.clf()
    axes = figure.add_subplot()
    axes.set_xlim([0, 1.1*T])
    axes.set_ylim([0, 1.1*conc])
    axes.title.set_text(f'Concentration w.r.t time at r = {r*1000}mm')
    axes.set(xlabel='Time(s)', ylabel='Concentration')

    global x_t
    global y_t

    x_t = np.linspace(0, T, num=math.ceil(T/dT))
    y_t = temporal_profile(r, a, T, dT, D, conc)

    axes.plot(x_t, y_t)
    figure_canvas.draw()


def save_data_t():
    global x_t
    global y_t
    files = [('CSV file', '*.csv'),
             ('All Files', '*.*')]
    f = filedialog.asksaveasfile(initialfile='data.csv', filetypes=files, defaultextension='.csv', mode='w')
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    y = np.array(y_t)
    xy_data = np.array([x_t, y])
    xy_data = xy_data.transpose()
    np.savetxt(f, xy_data, delimiter=',')
    f.close()  # `()` was missing.


temporal_plot_frame = ttk.Frame(notebook, width=root.winfo_width(), height=root.winfo_height())
temporal_plot_frame.pack(fill='both', expand=True)

temporal_plot_frame.rowconfigure(0, weight=6)
temporal_plot_frame.rowconfigure(1, weight=1)
temporal_plot_frame.rowconfigure(2, weight=1)
temporal_plot_frame.rowconfigure(3, weight=1)

temporal_plot_frame.columnconfigure(0, weight=1)
temporal_plot_frame.columnconfigure(1, weight=2)
temporal_plot_frame.columnconfigure(2, weight=1)
temporal_plot_frame.columnconfigure(3, weight=2)

# frame for plot
temporal_plot = ttk.Frame(temporal_plot_frame, width=temporal_plot_frame.winfo_width(), height=temporal_plot_frame.winfo_height())

# Figure
figure_t = Figure(figsize=(8, 4.5), dpi=100)

# create FigureCanvasTkAgg object
figure_canvas_t = FigureCanvasTkAgg(figure_t, temporal_plot)

# create the toolbar
NavigationToolbar2Tk(figure_canvas_t, temporal_plot)

# create axes
# axes = figure_t.add_subplot()

figure_canvas_t.get_tk_widget().pack(fill='both', expand=True)

# packing temporal_plot frame
temporal_plot.grid(row=0, column=0, columnspan=6, sticky="NSEW", padx=pdx)
temporal_plot['borderwidth'] = 1
temporal_plot['relief'] = 'solid'

# Diffusion coefficient entry

dif_label_t = tk.Label(temporal_plot_frame, text="Diffusion Coefficient(cm2/s)")
dif_label_t.grid(column=0, row=1, padx=pdx, pady=pdy, sticky='E')

D_t = tk.StringVar()
D_t.set("1e-7")
dif_entry_t = tk.Entry(temporal_plot_frame, textvariable=D_t)
dif_entry_t.grid(column=1, row=1, sticky='W', padx=pdx, pady=pdy)

# initial concentration entry

init_conc_label_t = tk.Label(temporal_plot_frame, text="Initial Concentration(unit)")
init_conc_label_t.grid(column=2, row=1, sticky='E', padx=pdx, pady=pdy)

conc_t = tk.StringVar()
conc_t.set("10")
conc_entry_t = tk.Entry(temporal_plot_frame, textvariable=conc_t)
conc_entry_t.grid(column=3, row=1, sticky='W', pady=pdy, padx=pdx)

# Radius entry

dif_label_t = tk.Label(temporal_plot_frame, text="Radius(mm)")
dif_label_t.grid(column=0, row=2, padx=pdx, pady=pdy, sticky='E')

a_t = tk.StringVar()
a_t.set("10")
radius_entry_t = tk.Entry(temporal_plot_frame, textvariable=a_t)
radius_entry_t.grid(column=1, row=2, sticky='W', padx=pdx, pady=pdy)


# Total Time entry

total_time_label_t = tk.Label(temporal_plot_frame, text="Total Time(s)")
total_time_label_t.grid(column=2, row=2, padx=pdx, pady=pdy, sticky='E')

t_total_t = tk.StringVar()
t_total_t.set("3600")
total_time_entry_t = tk.Entry(temporal_plot_frame, textvariable=t_total_t)
total_time_entry_t.grid(column=3, row=2, sticky='W', pady=pdy, padx=pdx)

# Radial distance entry

radial_distance_label_t = tk.Label(temporal_plot_frame, text="Radial Distance(mm)")
radial_distance_label_t.grid(column=0, row=3, padx=pdx, pady=pdy, sticky='E')

r_t = tk.StringVar()
r_t.set("9")
radial_distance_entry_t = tk.Entry(temporal_plot_frame, textvariable=r_t)
radial_distance_entry_t.grid(column=1, row=3, sticky='W', padx=pdx, pady=pdy)

# Time interval entry

time_interval_label_t = tk.Label(temporal_plot_frame, text="Time interval(>= 1s)")
time_interval_label_t.grid(column=2, row=3, padx=pdx, pady=pdy, sticky='E')

time_interval_t = tk.StringVar()
time_interval_t.set("300")
time_interval_entry_t = tk.Entry(temporal_plot_frame, textvariable=time_interval_t)
time_interval_entry_t.grid(column=3, row=3, sticky='W', pady=pdy, padx=pdx)


# calculate button
calc_t = tk.Button(
    temporal_plot_frame, text="Plot",
    command=lambda: plot_temporal(
        figure_t, figure_canvas_t, r_t.get(), a_t.get(),
        t_total_t.get(), time_interval_t.get(), conc_t.get(), D_t.get()))

calc_t.grid(column=1, columnspan=1, sticky='EW', padx=pdx, pady=pdy, row=4)

# save data button
save_t = tk.Button(temporal_plot_frame, text="Save Data", command=lambda: save_data_t())
save_t.grid(column=2, columnspan=1, sticky='EW', padx=pdx, pady=pdy, row=4)

# add frames to notebook
notebook.add(calc_frame, text="Calculator")
notebook.add(radial_plot_frame, text='Radial Plot')
notebook.add(temporal_plot_frame, text='Temporal Plot')




root.mainloop()