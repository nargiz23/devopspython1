
# A DevOps engineer needs to monitor the remaining time for a 
# long-running task on a server. They have the total time the task
#  takes in hours, minutes, and seconds, and they know the time that
#   has already passed. They want to calculate the remaining time for
#    the task to complete.

# Step 1: Define the problem inputs.

# Total time for the task (hours, minutes, seconds)
# Time passed (hours, minutes, seconds)
#FIRST WAY
total_hours = 5
total_minutes = 25
total_seconds = 15 # 0.25 min

passed_hours = 2
passed_minutes = 45
passed_seconds = 30

total_time = (total_hours * 60 * 60) + (total_minutes * 60) + total_seconds
passed_time = (passed_hours * 60 * 60) + (passed_minutes * 60) + passed_seconds
remaining_time = total_time - passed_time
remaining_hours = remaining_time // (60 * 60)
remaining_minutes = (remaining_time // 60) % 60
remaining_seconds = remaining_time % 60
print("The remaining time is:", remaining_hours, "hours,", remaining_minutes, "minutes, and", remaining_seconds, "seconds.")
  
  #Second way to solution
#3600 is seconds in an hour
total_time_in_sec= total_hours * 3600 +total_minutes * 60 + total_seconds;

passed_time_in_sec=passed_hours *3600+passed_minutes *60 + passed_seconds;
#this will gives us the remaining time in seconds
remaining_total_seconds=total_time_in_sec-passed_time_in_sec

#our goal is to convert remaining seconds in minustes hours and sec
#Question:how many hours we have in the remianing seconds

remaining_hours=remaining_total_seconds // 3600
remaining_minutes= (remaining_total_seconds %3600)//60
remaining_seconds=remaining_total_seconds %60
print(remaining_hours)
print(remaining_minutes)
print(remaining_seconds)






