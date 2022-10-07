import math
import tkinter as tk
from tkinter import filedialog, ttk
import matplotlib

# noinspection PyProtectedMember
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


from plot_data import pc_simulation_profile

matplotlib.use("TkAgg")


x_s = None
y_s = None


def plot_simulation(figure, figure_canvas, c_sat, D, a, tin, tout, n_point_r, n=100):
    a = float(a)/1000 # mm to meter conversion
    D = float(D)*(1e-4) # cm2/s to m2/s conversion
    tin = int(tin)
    tout = int(tout)
    c_sat = float(c_sat)
    n_point_r = int(n_point_r)
    figure.clf()
    axes = figure.add_subplot()
    axes.set_xlim([0, 1.1*a*1000])
    axes.set_ylim([0, 1.1*c_sat])
    axes.title.set_text(f'Concentration w.r.t radius after hydroxylation for {tin} seconds \n and dehydroxylation for {tout} seconds')
    axes.set(xlabel='Radius(mm)', ylabel='Concentration')

    global x_s
    global y_s

    x_s = np.linspace(0, 1000*a, num=n_point_r)
    y_s = simulation_profile(c_sat, D, a, tin, tout, n_point_r)

    axes.plot(x_s, y_s)
    figure_canvas.draw()


def save_data_s():
    global x_s
    global y_s
    files = [('CSV file', '*.csv'),
             ('All Files', '*.*')]
    f = filedialog.asksaveasfile(initialfile='data.csv', filetypes=files, defaultextension='.csv', mode='w')
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    y = np.array(y_s)
    xy_data = np.array([x_s, y])
    xy_data = xy_data.transpose()
    np.savetxt(f, xy_data, delimiter=',')
    f.close()  # `()` was missing.


def cc_simulation_tab(notebook, pdx, pdy):
    simulation_plot_frame = ttk.Frame(notebook, width=notebook.winfo_width(), height=notebook.winfo_height())
    simulation_plot_frame.pack(fill='both', expand=True)

    simulation_plot_frame.rowconfigure(0, weight=6)
    simulation_plot_frame.rowconfigure(1, weight=1)
    simulation_plot_frame.rowconfigure(2, weight=1)
    simulation_plot_frame.rowconfigure(3, weight=1)

    simulation_plot_frame.columnconfigure(0, weight=1)
    simulation_plot_frame.columnconfigure(1, weight=2)
    simulation_plot_frame.columnconfigure(2, weight=1)
    simulation_plot_frame.columnconfigure(3, weight=2)

    # frame for plot
    simulation_plot = ttk.Frame(simulation_plot_frame, width=simulation_plot_frame.winfo_width(),
                                height=simulation_plot_frame.winfo_height())

    # Figure
    figure_s = Figure(figsize=(8, 4.5), dpi=100)

    # create FigureCanvasTkAgg object
    figure_canvas_s = FigureCanvasTkAgg(figure_s, simulation_plot)

    # create the toolbar
    NavigationToolbar2Tk(figure_canvas_s, simulation_plot)

    # create axes
    # axes = figure_t.add_subplot()

    figure_canvas_s.get_tk_widget().pack(fill='both', expand=True)

    # packing simulation_plot frame
    simulation_plot.grid(row=0, column=0, columnspan=6, sticky="NSEW", padx=pdx)
    simulation_plot['borderwidth'] = 1
    simulation_plot['relief'] = 'solid'

    # Diffusion coefficient entry

    dif_label_s = tk.Label(simulation_plot_frame, text="Diffusion Coefficient(cm2/s)")
    dif_label_s.grid(column=0, row=1, padx=pdx, pady=pdy, sticky='E')

    D_s = tk.StringVar()
    D_s.set("1e-7")
    dif_entry_s = tk.Entry(simulation_plot_frame, textvariable=D_s)
    dif_entry_s.grid(column=1, row=1, sticky='W', padx=pdx, pady=pdy)

    # saturation concentration entry

    sat_conc_label_s = tk.Label(simulation_plot_frame, text="Saturation Concentration(unit)")
    sat_conc_label_s.grid(column=2, row=1, sticky='E', padx=pdx, pady=pdy)

    sat_conc_s = tk.StringVar()
    sat_conc_s.set("10")
    sat_conc_entry_s = tk.Entry(simulation_plot_frame, textvariable=sat_conc_s)
    sat_conc_entry_s.grid(column=3, row=1, sticky='W', pady=pdy, padx=pdx)

    # Radius entry

    radius_label_s = tk.Label(simulation_plot_frame, text="Radius(mm)")
    radius_label_s.grid(column=0, row=2, padx=pdx, pady=pdy, sticky='E')

    a_s = tk.StringVar()
    a_s.set("10")
    radius_entry_s = tk.Entry(simulation_plot_frame, textvariable=a_s)
    radius_entry_s.grid(column=1, row=2, sticky='W', padx=pdx, pady=pdy)


    # Time in entry

    tin_label_s = tk.Label(simulation_plot_frame, text="Hydroxylation time(s)")
    tin_label_s.grid(column=2, row=2, padx=pdx, pady=pdy, sticky='E')

    tin_s = tk.StringVar()
    tin_s.set("3600")
    tin_entry_s = tk.Entry(simulation_plot_frame, textvariable=tin_s)
    tin_entry_s.grid(column=3, row=2, sticky='W', pady=pdy, padx=pdx)

    # Time out entry

    tout_label_s = tk.Label(simulation_plot_frame, text="Dehydroxylation time(s)")
    tout_label_s.grid(column=0, row=3, padx=pdx, pady=pdy, sticky='E')

    tout_s = tk.StringVar()
    tout_s.set("9")
    tout_entry_s = tk.Entry(simulation_plot_frame, textvariable=tout_s)
    tout_entry_s.grid(column=1, row=3, sticky='W', padx=pdx, pady=pdy)

    # No. of points entry
    n_point_label_s = tk.Label(simulation_plot_frame, text="No. of points")
    n_point_label_s.grid(column=2, row=3, padx=pdx, pady=pdy, sticky='E')

    n_point_s = tk.StringVar()
    n_point_s.set('100')
    n_point_entry_s = tk.Entry(simulation_plot_frame, textvariable=n_point_s)
    n_point_entry_s.grid(column=3, row=3, sticky='W', pady=pdy, padx=pdx)


    # calculate button
    calc_s = tk.Button(
        simulation_plot_frame, text="Plot",
        command=lambda: plot_simulation(
            figure_s, figure_canvas_s, sat_conc_s.get(), D_s.get(), a_s.get(), tin_s.get(), tout_s.get(), n_point_s.get()))

    calc_s.grid(column=1, columnspan=1, sticky='EW', padx=pdx, pady=pdy, row=4)

    # save data button
    save_s = tk.Button(simulation_plot_frame, text="Save Data", command=lambda: save_data_s())
    save_s.grid(column=2, columnspan=1, sticky='EW', padx=pdx, pady=pdy, row=4)
    return simulation_plot_frame