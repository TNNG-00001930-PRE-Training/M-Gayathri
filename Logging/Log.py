import logging
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler('revature_training.py')
file_handler.setLevel(logging.ERROR)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.debug('This is a debug message')
logger.info('This is a info message')
logger.warning('This is a warning message')
logger.error('This is a error message')
logger.critical('This is a critical message')

2024-03-21 23:39:09,626 - example_logger - ERROR - This is a error message
2024-03-21 23:39:09,626 - example_logger - CRITICAL - This is a critical message
