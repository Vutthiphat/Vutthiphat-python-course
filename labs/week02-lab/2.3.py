#shopping Calculator Template
print("2. Time Converter:")
print(" - Ask user for seconds")
print(" - Convert to hours, minutes, and remaining seconds")
print(" - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

# input
seconds = int(input("Enter seconds: "))

# process
hours = seconds // 3600
seconds_remain = seconds % 3600

minutes = seconds_remain // 60
seconds_remain = seconds_remain % 60

# output
print(f"{seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds_remain} second(s)")