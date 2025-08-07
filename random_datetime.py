import random
import datetime

lucky_number = random.randint(1, 100)
current_time = datetime.datetime.now()

print(f"Your lucky number is: {lucky_number}")
print(f"Current date and time: {current_time}")