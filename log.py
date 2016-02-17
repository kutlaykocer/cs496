import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)
 
logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

#http://www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging/
