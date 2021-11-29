from datetime import datetime
import pytz

midwest_tz = pytz.timezone('America/Vancouver')
india_tz = pytz.timezone('Asia/Karachi')


dt = datetime(2016, 7, 27, 12, 13,45)
print(midwest_tz.localize(dt))
print(midwest_tz.localize(dt))