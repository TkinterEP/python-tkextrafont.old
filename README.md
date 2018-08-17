# TkExtrafont
Python wrapper around the `extrafont` Tcl library

## Usage
This wrapper uses the binary distributions of `extrafont` and loads them 
into a the `Tcl/Tk`-interpreter of a `Tkinter.Tk` instance during 
runtime. After doing so, a few additional functions are available on the
`Tk` instance, most notably `load_font`.

```python
import tkinter as tk
from tkextrafont import load_extrafont

window = tk.Tk()
load_extrafont(window)
window.load_font("path_to_font_file.ttf")
```

After loading, the fonts can be used within the Tk instance for themed
widgets. After the program exits, the fonts are no longer available.
The fonts are only available in the Tk-instance `extrafont` was loaded
into an all its children.

## License
    python-extrafont: A Python wrapper to load extrafont
    Copyright (c) 2018 RedFantom
    Copyright (c) 2017-2018 Aldo Buratti (extrafont)
    Copyright (c) 2018 Akuli (extrafont.chdir)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
