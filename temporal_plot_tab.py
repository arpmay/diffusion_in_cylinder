#####################
# TEMPORAL PLOT FRAME
#####################
import math
import tkinter as tk
from tkinter import filedialog, ttk
import matplotlib

# noinspection PyProtectedMember
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


from plot_data import temporal_profile

matplotlib.use("TkAgg")


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


def temporal_plot_tab(notebook, pdx, pdy):
    temporal_plot_frame = ttk.Frame(notebook, width=notebook.winfo_width(), height=notebook.winfo_height())
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

    return temporal_plot_frame