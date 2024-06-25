from datetime import datetime
import pytz

# Step 1: Define the PST timezone
pst_timezone = pytz.timezone('US/Pacific')

# Step 2: Get the current time in UTC
utc_now = datetime.now(pytz.utc)

# Step 3: Convert the current UTC time to PST
pst_now = utc_now.astimezone(pst_timezone)

# Step 4: Extract the date part and format it as YYYY-MM-DD
pst_date_str = pst_now.strftime('%Y-%m-%d')

# Print the result
print("Current date in PST (YYYY-MM-DD):", pst_date_str)