import generic
import json

class YousicianJSONFileHandler(generic.YousicianGenericFileHandler):
    def load(self):
        """Load the Yousician Cache JSON file.  The problem is that the file contains HTTP headers at the top, so my
        best idea is to try loading each line, until hitting the minimized JSON portion of the file."""
        lines = self.file.readlines()
        jsonStringFound = False

        for line in lines:
            try:
                self.data = json.loads(line)
                jsonStringFound = True
                break
            except json.decoder.JSONDecodeError:
                pass
        if jsonStringFound == False:
            raise json.decoder.JSONDecodeError("JSON decoding failed on all lines of the file!")