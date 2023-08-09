import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from tkinter import ttk
import webbrowser
import threading
import requests
import time
import math
import sys

class linkScreen:
    def __init__(self, link: str, title="Link", description="", download=False):
        # dummy download progress bar object
        self.dbar = None
        self.dloc = None
        # -----
        self.link = link
        self.download = download
        #----------
        self.screen = tk.Tk()
        self.screen.title(title)
        #s.geometry('320x100')
        tk.Label(self.screen, text=description, font=("Times", "14")).pack(side=tk.TOP)
        link = tk.Entry(self.screen)
        link.insert(0, self.link)
        link.config(state=tk.DISABLED)
        link.pack(side=tk.TOP)
        tk.Button(self.screen, text="Open in browser", command=self._open).pack(side=(tk.LEFT if download == True else tk.TOP))
        if download == True:
            tk.Button(self.screen, text="Download file", command=self._download).pack(side=tk.RIGHT)
        tk.Button(self.screen, text="Cancel", command=self.screen.destroy).pack(side=tk.BOTTOM)
        self.screen.mainloop()

    def _open(self):
        """Opens the link in a web browser, and then closes self.screen."""
        webbrowser.open(self.link)
        self.screen.destroy()

    def _download(self):
        """Downloads the file, with a fancy-schmancy gui"""
        try:
            print("download called")
            if self.download == False:
                tkinter.messagebox.showerror("Error", "download is not allowed but linkScreen.download() was called!")
                return
            self.dloc = tkinter.filedialog.asksaveasfilename(title="Where to save this file?")
            self.dscreen = tk.Tk()
            self.dscreen.attributes('-topmost', True)
            tk.Label(self.dscreen, font=("Times", "16"), text="Download Progress").pack(side=tk.TOP)
            self.dbar = ttk.Progressbar(self.dscreen, orient=tk.HORIZONTAL, length=300, mode="determinate")
            self.dbar.pack(side=tk.TOP)
            self.percent = tk.StringVar()
            dPercent = tk.Label(self.dscreen, textvariable=self.percent, font=("Times", "14", "italic")).pack(side=tk.TOP)
            dthread = threading.Thread(target=self._dlthread)
            dthread.start()

            self.dscreen.mainloop()
        except Exception as e:
            raise e
    def _dlthread(self):
        sTime = time.perf_counter()
        print("thread invoked")
        url = self.link
        
        try:
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            
            with open(self.dloc, 'wb') as file, response.raw as response_stream:
                for chunk in response_stream:
                    percent = (file.tell() / total_size) * 100
                    if chunk:
                        print(chunk)
                        file.write(chunk)
                        percent = (file.tell() / total_size) * 100
                        self.dbar["value"] = percent
                        self.percent.set("Percent complete: {0}%".format(round(percent, 2)))
                        #self._update_progress_bar(file.tell(), total_size)
                        self.dscreen.update()

            self.dbar["value"] = 100
            eTime = time.perf_counter()
            t = eTime - sTime
            minutes = t // 60
            seconds = math.remainder(t, 60)
            tkinter.messagebox.showinfo("Download", "Download complete!\n\nDownload took {0} minutes and {1} seconds.".format(minutes, seconds))
            self.dscreen.destroy()
            exit(0)

        except Exception as e:
            tkinter.messagebox.showerror("Error", e)
            self.screen.destroy()
            self.dscreen.destroy()
            raise e
            sys.exit(1)
    def _update_progress_bar(self, current_size, total_size):
        progress = (current_size / total_size) * 100
        self.dbar["value"] = progress
#        self.dscreen.update()


