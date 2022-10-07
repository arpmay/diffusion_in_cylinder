##################
# CALCULATOR FRAME
##################

from dehyroxy_func import C
import tkinter as tk
from tkinter import ttk


def solve(r, t, a, conc, D, label):
    r = float(r)/1000
    t = float(t)
    a = float(a)/1000
    conc = float(conc)
    D = float(D)*(1e-4)

    label.config(text=str(C(r, t, a, conc, D)))


def calculator_tab(notebook, pdx, pdy):
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

    return calc_frame