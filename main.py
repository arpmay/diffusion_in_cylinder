import tkinter as tk
from tkinter import ttk
import matplotlib

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from numpy import linspace
from dehyroxy_func import C
from plot_data import radial_profile, temporal_profile

matplotlib.use("TkAgg")

# padding
pdx = 10
pdy = 10

# root window


root = tk.Tk()
root.geometry('600x600')
root.title('Diffusion Sim')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=0, fill='both', expand=True)

# create frames
temporal_plot_frame = ttk.Frame(notebook, width=400, height=200)
simulation_frame = ttk.Frame(notebook, width=400, height=200)

temporal_plot_frame.pack(fill='both', expand=True)
simulation_frame.pack(fill='both', expand=True)

##################
# CALCULATOR FRAME
##################


def solve(r, t, a, conc, D, label):
    r = float(r)
    t = float(t)
    a = float(a)
    conc = float(conc)
    D = float(D)

    label.config(text=str(C(r, t, a, conc, D)))


calc_frame = ttk.Frame(notebook, width=400, height=200)
calc_frame.pack(fill='both', expand=True)
calc_frame.columnconfigure(0, weight=1)
calc_frame.columnconfigure(1, weight=4)

# Diffusion coefficient entry

dif_label_c = tk.Label(calc_frame, text="Diffusion Coefficient")
dif_label_c.grid(column=0, row=0)

D_c = tk.StringVar()
dif_entry_c = tk.Entry(calc_frame, textvariable=D_c)
dif_entry_c.grid(column=1, row=0, sticky='EW', pady=pdy, padx=pdx)

# Radius entry

radius_label_c = tk.Label(calc_frame, text="Radius")
radius_label_c.grid(column=0, row=1)

a_c = tk.StringVar()
radius_entry_c = tk.Entry(calc_frame, textvariable=a_c)
radius_entry_c.grid(column=1, row=1, sticky='EW', pady=pdy, padx=pdx)

# initial concentration entry

init_conc_label_c = tk.Label(calc_frame, text="Initial Concentration")
init_conc_label_c.grid(column=0, row=2)

conc_c = tk.StringVar()
conc_entry_c = tk.Entry(calc_frame, textvariable=conc_c)
conc_entry_c.grid(column=1, row=2, sticky='EW', pady=pdy, padx=pdx)

# Time entry

time_label_c = tk.Label(calc_frame, text="Time")
time_label_c.grid(column=0, row=3)

t_c = tk.StringVar()
time_entry_c = tk.Entry(calc_frame, textvariable=t_c)
time_entry_c.grid(column=1, row=3, sticky='EW', pady=pdy, padx=pdx)

# radial distance entry

r_label_c = tk.Label(calc_frame, text="Radial Dist.")
r_label_c.grid(column=0, row=4)

r_c = tk.StringVar()
r_entry_c = tk.Entry(calc_frame, textvariable=r_c)
r_entry_c.grid(column=1, row=4, sticky='EW', pady=pdy, padx=pdx)

# result label
result_label_c = tk.Label(calc_frame, text="")
result_label_c.grid(column=0, row=6, columnspan=2)

# calculate button
calc_c = tk.Button(calc_frame, text="Calculate",
                   command=lambda: solve(r_c.get(), t_c.get(), a_c.get(), conc_c.get(), D_c.get(), result_label_c))
calc_c.grid(column=0, columnspan=2, row=5)


###################
# RADIAL PLOT FRAME
###################


def plot_radial(figure, figure_canvas_r, t, a, conc, D):
    t = float(t)
    a = float(a)/1000
    conc = float(conc)
    D = float(D)
    figure.clf()
    axes = figure.add_subplot()
    axes.set_xlim([0, 1.1*a*1000])
    axes.set_ylim([0, 1.1*conc])
    axes.title.set_text(f'Concentration along radius at t = {int(t)} seconds')
    axes.set(xlabel='Radial Distance(mm)', ylabel='Concentration')
    axes.plot(linspace(0, a*1000, num=250), radial_profile(t, a, D, conc))
    figure_canvas_r.draw()


radial_plot_frame = ttk.Frame(notebook, width=root.winfo_width(), height=root.winfo_height())
radial_plot_frame.pack(fill='both', expand=True)

radial_plot_frame.rowconfigure(0, weight=10)
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
radial_plot.grid(row=0, column=0, columnspan=6, sticky="NSEW", padx=10)


# Diffusion coefficient entry

dif_label_r = tk.Label(radial_plot_frame, text="Diffusion Coefficient(m2/s)")
dif_label_r.grid(column=0, row=1, padx=pdx, pady=pdy, sticky='E')

D_r = tk.StringVar()
dif_entry_r = tk.Entry(radial_plot_frame, textvariable=D_r)
dif_entry_r.grid(column=1, row=1, sticky='W', padx=pdx, pady=pdy)

# Radius entry

dif_label_r = tk.Label(radial_plot_frame, text="Radius(mm)")
dif_label_r.grid(column=2, row=1, padx=pdx, pady=pdy, sticky='E')

a_r = tk.StringVar()
radius_entry_r = tk.Entry(radial_plot_frame, textvariable=a_r)
radius_entry_r.grid(column=3, row=1, sticky='W', padx=pdx, pady=pdy)

# initial concentration entry

init_conc_label_r = tk.Label(radial_plot_frame, text="Initial Concentration")
init_conc_label_r.grid(column=0, row=2, sticky='E', padx=pdx, pady=pdy)

conc_r = tk.StringVar()
conc_entry_r = tk.Entry(radial_plot_frame, textvariable=conc_r)
conc_entry_r.grid(column=1, row=2, sticky='W', pady=pdy, padx=pdx)

# Time entry

time_label_r = tk.Label(radial_plot_frame, text="Time")
time_label_r.grid(column=2, row=2, padx=pdx, pady=pdy, sticky='E')

t_r = tk.StringVar()
time_entry_r = tk.Entry(radial_plot_frame, textvariable=t_r)
time_entry_r.grid(column=3, row=2, sticky='W', pady=pdy, padx=pdx)


# calculate button
calc_r = tk.Button(radial_plot_frame, text="Calculate", command=lambda: plot_radial(figure_r, figure_canvas_r, t_r.get(), a_r.get(), conc_r.get(), D_r.get()))
calc_r.grid(column=0, columnspan=6, row=3)

"""
#######################
# TEMPORAL PLOT FRAME #
#######################
def plot_temporal(figure, figure_canvas_t, r, a, conc, D):
    r = float(r)
    a = float(a)
    conc = float(conc)
    D = float(D)
    axes = figure.add_subplot()
    axes.set_xlim([0, 1.1*250])
    axes.set_ylim([0, 1.1*conc])
    axes.title.set_text(f'Concentration along radius at t = {t} seconds')
    axes.set(xlabel='Radial Distance', ylabel='Concentration')
    axes.plot(radial_profile(t, a, D, conc))
    figure_canvas_t.draw()


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
radial_plot = ttk.Frame(radial_plot_frame)

# Figure
figure_r = Figure(figsize=(6, 4), dpi=100)

# create FigureCanvasTkAgg object
figure_canvas_r = FigureCanvasTkAgg(figure_r, radial_plot)

# create the toolbar
NavigationToolbar2Tk(figure_canvas_r, radial_plot)

# create axes
# axes = figure_r.add_subplot()

figure_canvas_r.get_tk_widget().pack(fill='both', expand=True)

# packing radial_plot frame
radial_plot.grid(row=0, column=0, columnspan=6, sticky="EW")


# Diffusion coefficient entry

dif_label_r = tk.Label(radial_plot_frame, text="Diffusion Coefficient")
dif_label_r.grid(column=0, row=1, padx=pdx, pady=pdy, sticky='E')

D_r = tk.StringVar()
dif_entry_r = tk.Entry(radial_plot_frame, textvariable=D_r)
dif_entry_r.grid(column=1, row=1, sticky='W', padx=pdx, pady=pdy)

# Radius entry

dif_label_r = tk.Label(radial_plot_frame, text="Radius")
dif_label_r.grid(column=2, row=1, padx=pdx, pady=pdy, sticky='E')

a_r = tk.StringVar()
radius_entry_r = tk.Entry(radial_plot_frame, textvariable=a_r)
radius_entry_r.grid(column=3, row=1, sticky='W', padx=pdx, pady=pdy)

# initial concentration entry

init_conc_label_r = tk.Label(radial_plot_frame, text="Initial Concentration")
init_conc_label_r.grid(column=0, row=2, sticky='E', padx=pdx, pady=pdy)

conc_r = tk.StringVar()
conc_entry_r = tk.Entry(radial_plot_frame, textvariable=conc_r)
conc_entry_r.grid(column=1, row=2, sticky='W', pady=pdy, padx=pdx)

# Time entry

time_label_r = tk.Label(radial_plot_frame, text="Time")
time_label_r.grid(column=2, row=2, padx=pdx, pady=pdy, sticky='E')

t_r = tk.StringVar()
time_entry_r = tk.Entry(radial_plot_frame, textvariable=t_r)
time_entry_r.grid(column=3, row=2, sticky='W', pady=pdy, padx=pdx)


# calculate button
calc_r = tk.Button(radial_plot_frame, text="Calculate", command=lambda: plot_radial(figure_r, figure_canvas_r, t_r.get(), a_r.get(), conc_r.get(), D_r.get()))
calc_r.grid(column=0, columnspan=6, row=3)
"""


# add frames to notebook
notebook.add(calc_frame, text="Calculator")
notebook.add(radial_plot_frame, text='Radial Plot')
notebook.add(temporal_plot_frame, text='Temporal Plot')
notebook.add(simulation_frame, text='Simulation')




root.mainloop()