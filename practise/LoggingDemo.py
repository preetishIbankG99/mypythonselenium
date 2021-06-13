import logging
logging.basicConfig(filename="testconfig",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
logging.debug("This is Debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.critical("This is critical message")
logging.error("This is Error message")