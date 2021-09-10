import pywhatkit as kit

msg = "Hello this message is from Python"

###### e.g 8:02 ######
# num= str(9)
# numz = num.zfill(2)

# personal message
kit.sendwhatmsg("phone_num", msg, 21,10)

#group message
kit.sendwhatmsg_to_group("group_id", msg, 21,10)