###################
# RADIAL PLOT FRAME
###################

import tkinter as tk
from tkinter import filedialog, ttk
import matplotlib

# noinspection PyProtectedMember
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


from plot_data import radial_profile

matplotlib.use("TkAgg")

# DATA VARIABLE
x_r = None
y_r = None


def plot_radial(figure, figure_canvas_r, t_str, a, conc, D, n_point_r):
    t = t_str.split(',')
    t = [float(x) for x in t]
    a = float(a)/1000
    n_point_r=int(n_point_r)
    conc = float(conc)
    D = float(D)*(1e-4)
    figure.clf()
    axes = figure.add_subplot()
    axes.set_xlim([0, 1.1 * a * 1000])
    axes.set_ylim([0, 1.1 * conc])
    axes.title.set_text(f'Concentration along radius at \nt = {str(t)} seconds')
    axes.set(xlabel='Radial Distance(mm)', ylabel='Concentration')
    for time in t:
        time = float(time)
        global x_r
        global y_r
        x_r = np.linspace(0, a*1000, num=n_point_r)
        y_r = radial_profile(time, a, D, conc, n_point_r)
        y_r = np.array(y_r).reshape(100)
        axes.plot(x_r, y_r)
    figure.legend()
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


def radial_plot_tab(notebook, pdx, pdy):
    radial_plot_frame = ttk.Frame(notebook, width=notebook.winfo_width(), height=notebook.winfo_height())
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
    D_r.set('3.71e-5')
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
    t_r.set('36000')
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

    return radial_plot_frame