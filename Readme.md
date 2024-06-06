# Easy Logging Package

Easy Logging is a Python package that simplifies the process of setting up logging in your Python applications. With Easy Logging, you can easily configure logging to suit your needs, without having to write a lot of boilerplate code.

## Installation

You can install Easy Logging using pip:

```bash
pip install easy-logging
```

# Usage
Here's an example of how you can use Easy Logging to configure logging in your Python application:

```python
# main.py
import logging
from easy_logging import Logging

# Configure logging
logging = Logging(enable_json_mode=True)

# Get the logger for the current module
logger = logging.getLogger(__name__)

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
``` 

In this example, we import the Logging class from the easy_logging package and use it to configure logging. We can pass an optional enable_json_mode argument to the Logging class to enable JSON formatting for the log messages. We then use the getLogger method to get a logger object that we can use to log messages.

# Configuration
Easy Logging uses a YAML configuration file to configure logging. By default, the configuration file is located in the same directory as the easy_logging package. You can customize the configuration by creating a log-config.yml file in the same directory as your Python script and modifying the configuration as needed.

# Contributing
Contributions to Easy Logging are welcome! If you find a bug or have a feature request, please open an issue on the GitHub repository. If you'd like to contribute code, please fork the repository and submit a pull request.

# License
Easy Logging is licensed under the MIT License. See the LICENSE file for details.


You can copy and paste this source code into a file named `README.md` in the root directory of your project.
how to add code in readme.md

To add code to a README.md file, you can use Markdown syntax to format the code as a code block. Here's an example of how to add a code block to a README.md file: