#    Wesician --> Yousician Scripts (File: src/main.py)
#    Copyright (C) 2023  Damien Boisvert (AlphaGameDeveloper)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tkinter as tk
import tkinter.messagebox
import sys
import json
import os


def createConfig() -> None:
	tf = ("Times", "18")
	s = tk.Tk()
	s.title("Wesician Configuration")
	tk.Label(s, text="Wesician Configuration", font=tf).pack(side=tk.TOP)
	s.mainloop()

def main() -> int:
	if os.path.isfile("wesician.config.json") == False:
		createConfig()
	s = tk.Tk()
	s.title("Wesician")
	s.mainloop()
	return 0

if __name__ == "__main__":
	sys.exit(main())
else:
	print("wesician: main.py MUST BE AN ENTRYPOINT,")
	print("wesician: but it is not directly executed.")
	sys.exit(1)
