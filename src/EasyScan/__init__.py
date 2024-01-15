# Import necessary modules
import os
import sys
import logging

# Configure logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Specify the log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    # Set up logging handlers (to both a file and the console)
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger with the name "EasyScanLogger"
logger = logging.getLogger("EasyScanLogger")
