import logging
import os 

def my_logger(logger_name:str):
    # create logger
    logpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"logs","jojo.log")
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(filename=logpath, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger