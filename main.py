import tkinter as tk
from tkinter import ttk

from calculator_tab import calculator_tab
from radial_plot_tab import radial_plot_tab
from temporal_plot_tab import temporal_plot_tab
from cc_simulation_tab import cc_simulation_tab

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

calc_frame = calculator_tab(notebook, pdx, pdy)

###################
# RADIAL PLOT FRAME
###################

radial_plot_frame = radial_plot_tab(notebook, pdx, pdy)

#####################
# TEMPORAL PLOT FRAME
#####################

temporal_plot_frame = temporal_plot_tab(notebook, pdx, pdy)

##############################
# C-C SIMULATION FRAME
##############################

cc_simulation_plot_frame = cc_simulation_tab(notebook, pdx, pdy)


######################
# P-C SIMULATION FRAME
######################

pc_simulation_plot_frame = pc_simulation_tab(notebook, pdx, pdy)

#################
# ABOUT SECTION #
#################

about_frame = ttk.Frame(notebook, width=root.winfo_width(), height=root.winfo_height())
about_frame.pack(fill='both', expand=True)

# Heading label
heading_label = ttk.Label(about_frame, text="About", font=('Helvetica', 14))
heading_label.pack()


# add frames to notebook
notebook.add(calc_frame, text="Calculator")
notebook.add(radial_plot_frame, text='Radial Plot')
notebook.add(temporal_plot_frame, text='Temporal Plot')
notebook.add(cc_simulation_plot_frame, text="CC Simulation")
notebook.add(pc_simulation_plot_frame, text='PC Simulation')
notebook.add(about_frame, text='About')


root.mainloop()