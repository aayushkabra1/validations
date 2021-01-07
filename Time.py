seconds = int(input("Seconds = "))

if seconds < 0:
    print("Invalid")
else:
    years = seconds // 31536000
    days = (seconds % 604800) // 86400
    hours = ((seconds % 604800) % 86400) // 3600
    minutes = (((seconds % 604800) % 86400) % 3600) // 60
    seconds = (((seconds % 604800) % 86400) % 3600) % 60

    print("Year={}, Days={}, Hours={}, Minutes={}, Seconds={}".format(years, days, hours, minutes, seconds))
