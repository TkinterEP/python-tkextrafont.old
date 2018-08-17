"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2018 RedFantom
"""

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:  # Python 2
    import Tkinter as tk
    import ttk
from tkextrafont import load_extrafont

window = tk.Tk()
load_extrafont(window)
window.load_font("Roboto-Medium.ttf")
assert window.is_font_available("Roboto")
assert "Roboto Medium" in window.loaded_fonts()
assert window.font_info("Roboto-Medium.ttf")[0]["copyright"]
ttk.Label(window, text="Roboto Font", font=("Roboto", 12)).grid()
ttk.Label(window, text="Normal Font", font=("default", 12)).grid()
window.mainloop()
