from twython import Twython
from datetime import date
#from auth import (
#    consumer_key,
#    consumer_secret,
#    access_token,
#    access_token_secret
#)
originDate = date(2023, 2, 22).strftime("%d")
currentDate = date.today().strftime("%d")
daysElapsed = int(currentDate) - int(originDate)
#twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
message = "Day " + str(daysElapsed) + " tweeting @MountainDew until they make a Voltage diet/zero drink #MountainDew #voltage #mtnDewZeroVoltage"
print(message)
#twitter.update_status(status=message)
