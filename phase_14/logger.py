# logger.py

import logging
import sys
from config import config

def setup_logger():
    # Convert string level from config to logging constants
    level_name = config.LOG_LEVEL.upper()
    log_level = getattr(logging, level_name, logging.INFO)

    # Configure root logger
    logger = logging.getLogger("phase14")
    logger.setLevel(log_level)

    # Avoid duplicate handlers if setup is called multiple times
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)

        # Standard format safe for production (no sensitive payload dumps)
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | [%(name)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)

    return logger

# Singleton logger instance
log = setup_logger()
