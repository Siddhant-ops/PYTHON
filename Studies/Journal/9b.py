class Program(object):
    def __init__(self):
        self.__version = 12.4

    def getVersion(self):
        print(self.__version)

    def setVersion(self, version):
        self.__version = version


obj = Program()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print(obj.__version)  # this is return an error stating AttributeError: 'Program' object has no attribute '__version'
