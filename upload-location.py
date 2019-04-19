

import urllib
import re
from bs4 import BeautifulSoup

def sleeper():
    while True:
		x=14.7288829
		y=120.9610863
		data=urllib.urlopen("thingspeak api key"+str(x)+"&field2"+str(y));
		print data;
       
        time.sleep(3)
        
 
 
try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    


