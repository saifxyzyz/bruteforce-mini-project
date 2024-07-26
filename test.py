import random
import logging


logging.basicConfig(filename="newfile2.log",
					format='%(asctime)s %(message)s',
					filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

data_list = "0123456789"
chardata = list(data_list)
print(chardata)
password = str(input("password:"))
guess = ""
logger.debug("starting debug")
while(guess != password):
    guess = random.choices(chardata, k=len(password))
    print(guess)
    guess = "".join(guess)
print("your password is: " + guess)    
# importing module


# Create and configure logger


# Test messages

logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
