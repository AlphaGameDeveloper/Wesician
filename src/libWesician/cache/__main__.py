#    LibWesician --> Yousician Cache File Library (File: cache/__main__.py)
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


import filetypes
import filetypes.generic
import os

def tryGetCacheType(filename):
    file = open(filename, "r")
    obj = filetypes.generic.YousicianGenericFileHandler(file)
    print(obj.getFromHTTPData("content-type"))

for a in os.listdir("C:/Users/damie/AppData/LocalLow/Yousician/Yousician/HTTPCache"):
    try:
        tryGetCacheType("C:/Users/damie/AppData/LocalLow/Yousician/Yousician/HTTPCache/%s" % a)
    except UnicodeDecodeError:
        pass