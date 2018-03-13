if data=='MID':
flame='M'

start_time=time.time()
data=flamecontrol(data)
bot.sendMessage(chat_id=chat_id, text="Flame- Medium")
if data=='OFF':
	data=flamecontrol(data)
status='OFF'
bot.sendMessage(chat_id=chat_id, text="Stove is turned off")
end_time=time.time()
calculate(start_time,end_time)
if data=='TIMH':
status='ON'
flame='H'
bot.sendMessage(chat_id=chat_id, text="TIME MODE STARTED..")
start_time=time.time()
data=flamecontrol(status)
time_temp=(int(time_control))
print time_temp
for i in range (0,time_temp):
time.sleep(1)
print i
status='OFF'
data=flamecontrol(status)
status='OFF'
end_time=time.time()
calculate(start_time,end_time)
bot.sendMessage(chat_id=chat_id, text="Time over, Stove is turned off")
if data=='TIMM':
status='MID'
flame='M'
bot.sendMessage(chat_id=chat_id, text="TIME MODE STARTED..")
start_time=time.time()
data=flamecontrol(status)
time_temp=(int(time_control))
print time_temp
for i in range (0,time_temp):
time.sleep(1)
print i
status='OFF'

data=flamecontrol(status)
status='OFF'
end_time=time.time()
calculate(start_time,end_time)
bot.sendMessage(chat_id=chat_id, text="Time over, Stove is turned off")