from logger import DEBUG

"""readconfig.py: This script reads and parses values from the configuration file"""


class ConfigFile:
    def __init__(self, file):
        self.file = file
        self.param_map = dict()

    def loadconfig(self):
        DEBUG('Loading configurations from: [{}]'.format(self.file))
        list = []
        with open(self.file) as line:
            for l in line:
                if l.startswith(' ') or l.startswith('#'):
                    continue
                list.append(l.strip().replace(" ", ""))

        self.param_map = dict(s.split('=') for s in list)

        return self.param_map

    def getvalue(self, param):
        return self.param_map.get(param)
