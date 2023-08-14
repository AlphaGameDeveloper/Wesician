class YousicianGenericFileHandler(object):
    def __init__(self, file):
        self.file = file
        self.data = None
        self.http = None
        self.getHTTPData()

    def getHTTPData(self):
        lines = self.file.readlines()
        self.httpHeaders = []
        index = 0
        for l in lines:
            if index == 0:
                #if "{0}{1}{2}{3}".format(l[0],l[1],l[2],l[3]) == "HTTP":
                self.httpHeaders.append(["http-response", l])
                index += 1
            if l == "" or l == "\n":
                break
            
            sp = l.split(":")
            
            _sp = sp[:]
            del _sp[0]
            t = ""
            for f in sp:
                t = t + ":"
            self.httpHeaders.append([sp[0], t])

    def getFromHTTPData(self, key):
        found = False
        for a in self.httpHeaders:
            #print("new a ({0})".format(a[0]))
            if a[0] == key:
                
                found = True
                return a[1]
        if found == False:
            raise KeyError("Could not find key '%s' in headers" % key)


    