import tkinter as tk
from tkinter import ttk

from dehyroxy_func import C


def calc_gui(Notebook, width, height):

        def solve(r, t, a, conc, D, label):
            r = float(r)
            t = float(t)
            a = float(a)
            conc = float(conc)
            D = float(D)

            label.config(text=str(C(r, t, a, conc, D)))

        calc_frame = ttk.Frame(Notebook, width=width, height=height)
        calc_frame.pack()
        calc_frame.columnconfigure(0, weight=1)
        calc_frame.columnconfigure(1, weight=4)

        # Diffusion coefficient entry

        dif_label = tk.Label(calc_frame, text="Diffusion Coefficient")
        dif_label.grid(column=0, row=0)

        D = tk.StringVar()
        dif_entry = tk.Entry(calc_frame, textvariable=D)
        dif_entry.grid(column=1, row=0, sticky='EW', pady=10, padx=10)

        # Radius entry

        dif_label = tk.Label(calc_frame, text="Radius")
        dif_label.grid(column=0, row=1)

        a = tk.StringVar()
        radius_entry = tk.Entry(calc_frame, textvariable=a)
        radius_entry.grid(column=1, row=1, sticky='EW', pady=10, padx=10)

        # initial concentration entry

        init_conc_label = tk.Label(calc_frame, text="Initial Concentration")
        init_conc_label.grid(column=0, row=2)

        conc = tk.StringVar()
        conc_entry = tk.Entry(calc_frame, textvariable=conc)
        conc_entry.grid(column=1, row=2, sticky='EW', pady=10, padx=10)

        # Time entry

        time_label = tk.Label(calc_frame, text="Time")
        time_label.grid(column=0, row=3)

        t = tk.StringVar()
        time_entry = tk.Entry(calc_frame, textvariable=t)
        time_entry.grid(column=1, row=3, sticky='EW', pady=10, padx=10)

        # radial distance entry

        r_label = tk.Label(calc_frame, text="Radial Dist.")
        r_label.grid(column=0, row=4)

        r = tk.StringVar()
        r_entry = tk.Entry(calc_frame, textvariable=r)
        r_entry.grid(column=1, row=4, sticky='EW', pady=10, padx=10)

        # result label
        result_label = tk.Label(calc_frame, text="")
        result_label.grid(column=0, row=6, columnspan=2)

        # calculate button
        calc = tk.Button(calc_frame, text="Calculate", command=lambda: solve(r.get(), t.get(), a.get(), conc.get(), D.get(), result_label))
        calc.grid(column=0, columnspan=2, row=5)
