# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(
    level=logging.DEBUG, filename="Start\\Ch_4\\output.log", filemode="w"
)

# TODO: Try out each of the log levels
logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")

# TODO: Output formatted strings to the log
x = "test"
logging.info(f"Formmated: {x}")
