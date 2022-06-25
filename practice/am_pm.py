


from cgi import print_arguments


def converter(s):
    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]
    phase = s[8:]
    if phase == "AM" and hour =="12" and minute== '00' and second == '00':
        return "00:00:00"
    
    delta = 0
    if phase == 'PM':
        delta = 12
    hour_int = 0
    if hour[0]=='0':
        hour_int = int(hour[1]) + delta
    else:
        if hour == '12':
            delta = 0
        if phase == 'AM':
            hour = '00'
        hour_int = int(hour) + delta
    if hour_int < 10:
        hour_str = '0'+str(hour_int)
    else:
        hour_str = str(hour_int)
    return hour_str+":"+str(minute)+":"+str(second)




"""
07:05:45PM == 19:05:45
07:05:45AM == 07:05:45
12:05:00AM == 00:05:00
12:05:00PM == 12:05:00
"""
if __name__ =="__main__":
    print(converter("07:05:45PM"))