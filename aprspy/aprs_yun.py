#!/usr/bin/python

__author__ = "Mattiolo Paolo Valentino"
__copyright__ = "2020 Mattiolo Paolo"
__license__ = "Gnu GPL"
__version__ = "1.0.0"
__maintainer__ = "Mattiolo Paolo"
__email__ = "mattiolo@gmail.com"
__status__ = "Production"

import argparse




import aprslib

MYCALL = 'IN3AQK'
PASSWD = '22694'

def sendPos():
    

    # a valid passcode for the callsign is required in order to send
    AIS = aprslib.IS(MYCALL, passwd=PASSWD, port=14580)
    AIS.connect()
    # send a single status message    
    AIS.sendall("%s>APRX29,TCPIP*,qAC,T2USANW:!4635.00NI01112.00E-Arduino YUN linux http://in3aqk.blogspot.com" % MYCALL )






if __name__ == "__main__":
    sendPos()