
__author__ = "Mattiolo Paolo Valentino"
__copyright__ = "2020 Mattiolo Paolo"
__license__ = "Gnu GPL"
__version__ = "1.0.0"
__maintainer__ = "Mattiolo Paolo"
__email__ = "mattiolo@gmail.com"
__status__ = "Production"


import ConfigParser
import os
import aprslib



class AprsToIs:

    MYCALL = None
    PASSWD = None
    aprs_is = None


    def __init__(self):
        self.getConfigs()


    def getConfigs(self):

        config = ConfigParser.ConfigParser()
        config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'conf.ini'))
        self.MYCALL = config.get("default","MYCALL")
        self.PASSWD = config.get("default","PASSWD")

   
    def send(self,dataToSend):

        self.__parseData(dataToSend)
        self.__connect()
        # send a single status message    
        self.aprs_is.sendall("%s>APRX29,TCPIP*,qAC,T2USANW:!4635.00NI01112.00E-Arduino YUN linux http://in3aqk.blogspot.com" % self.MYCALL )


    def __parseData(self,dataTosend):
        return 1



    def __connect(self):
         # a valid passcode for the callsign is required in order to send
        self.aprs_is = aprslib.IS(self.MYCALL, passwd=self.PASSWD, port=14580)
        self.aprs_is.connect()


