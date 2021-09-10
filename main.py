import pywhatkit as kit

phone_num = input("Type a phone number: ")
msg = input("Type a message: ")
print("Enter the time in 24 hour format")
time_hour = input(str("Type a time (hour): "))
time_minute = input(str("Type a time (minute): "))

kit.sendwhatmsg(f"+6{phone_num}", msg, int(time_hour),int(time_minute))