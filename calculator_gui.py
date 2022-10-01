import tkinter as tk
import matplotlib
from dehyroxy_func import C


matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


class App(tk.Tk):

    def __init__(self):

        def solve(r, t, a, conc, D, label):
            r = float(r)
            t = float(t)
            a = float(a)
            conc = float(conc)
            D = float(D)

            label.config(text=str(C(r, t, a, conc, D)))

        super().__init__()

        self.title('Diffusion in a cylinder')

        self.geometry('400x400')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)

        # Diffusion coefficient entry

        dif_label = tk.Label(self, text="Diffusion Coefficient")
        dif_label.grid(column=0, row=0)

        D = tk.StringVar()
        dif_entry = tk.Entry(self, textvariable=D)
        dif_entry.grid(column=1, row=0, sticky='EW', pady=10, padx=10)

        # Radius entry

        dif_label = tk.Label(self, text="Radius")
        dif_label.grid(column=0, row=1)

        a = tk.StringVar()
        radius_entry = tk.Entry(self, textvariable=a)
        radius_entry.grid(column=1, row=1, sticky='EW', pady=10, padx=10)

        # initial concentration entry

        init_conc_label = tk.Label(self, text="Initial Concentration")
        init_conc_label.grid(column=0, row=2)

        conc = tk.StringVar()
        conc_entry = tk.Entry(self, textvariable=conc)
        conc_entry.grid(column=1, row=2, sticky='EW', pady=10, padx=10)

        # Time entry

        time_label = tk.Label(self, text="Time")
        time_label.grid(column=0, row=3)

        t = tk.StringVar()
        time_entry = tk.Entry(self, textvariable=t)
        time_entry.grid(column=1, row=3, sticky='EW', pady=10, padx=10)

        # radial distance entry

        r_label = tk.Label(self, text="Radial Dist.")
        r_label.grid(column=0, row=4)

        r = tk.StringVar()
        r_entry = tk.Entry(self, textvariable=r)
        r_entry.grid(column=1, row=4, sticky='EW', pady=10, padx=10)

        # result label
        result_label = tk.Label(self, text="")
        result_label.grid(column=0, row=6, columnspan=2)

        # calculate button
        calc = tk.Button(self, text="Calculate", command=lambda: solve(r.get(), t.get(), a.get(), conc.get(), D.get(), result_label))
        calc.grid(column=0, columnspan=2, row=5)




if __name__ == '__main__':
    app = App()
    app.mainloop()