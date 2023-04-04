
minutes = 3456789

# calculate the number of years and days
minutes_in_year = 365 * 24 * 60
minutes_in_day = 24 * 60

years = minutes // minutes_in_year
days = (minutes % minutes_in_year) // minutes_in_day

print(minutes,"minutes is approximately", years," years and", days," days")
