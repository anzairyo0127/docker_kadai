import os
import logging
import time

# Logging Format Initting
formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.Formatter.converter = time.gmtime
logging.basicConfig(level=logging.DEBUG, format=formatter)

# Get value from environment variable
login_name = os.getenv('LOGIN_NAME', 'default')
password = os.getenv('PASSWORD', 'default')

# Print login information
logging.info(f'LoginName="{login_name}" ; Password="{password}"')
logging.info('Cheking Username & Password .....')

# Stop one second
time.sleep(1)

# ひっどいログイン処理
if (login_name == 'honda') & (password == 'vFr8+rr'):
    logging.info('OK! Login Succeeded!')
else:
    logging.error('ERROR! Failed to login.')
