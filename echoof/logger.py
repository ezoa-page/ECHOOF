"""
This software is proprietary and may not be used, copied, modified, or distributed without the express permission of the copyright holder.
"""

import logging

# Create and configure logger
logger = logging.getLogger(__name__)

# Create console handler
ch = logging.StreamHandler()

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(ch)

# Logging level will be configured dynamically in the CLI
logger.setLevel(logging.WARNING)  # Default level set to WARNING to minimize output
