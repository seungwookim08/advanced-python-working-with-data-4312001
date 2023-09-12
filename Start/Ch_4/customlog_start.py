# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
formatstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %p"

# set the output file and debug level, and
# TODO: use a custom formatting specification
logging.basicConfig(
    level=logging.DEBUG,
    filename="Start\\Ch_4\\output2.log",
    format=formatstr,
    datefmt=datestr,
)

logging.info("This is an info-level log message")
logging.warning("This is a warning-level message")
