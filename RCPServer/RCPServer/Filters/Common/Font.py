'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPServer.Filters.Filter import Filter

class Font(Filter):
    '''Class description...'''

    def __init__(self):
        #Call default parent constructor
        Filter.__init__(self)

    def ConstructDefaultParameters(self):
        return {"size":"3", "color":"red"}
        
    def ApplyFilter(self, message, filterParameters):
        result = '<font size="%(size)s" color="%(color)s">'%filterParameters
        result += str(message["Value"])
        result += '</font>'
        message["Value"] = result