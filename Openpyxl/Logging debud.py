import logging
logging.basicConfig(filename="D://Docments/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG
                    )
logging.debug("this msg debug")
logging.info("this msg to info")
logging.warning("warning to you")
logging.error("warned as error")
logging.critical("critical file")
