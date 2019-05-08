def doTime() :
	today = datetime.datetime.now()
	hours = today.hour
	minutes = str(today.minute)

	if len(minutes) < 2 :
		minutes = '0' + minutes

	period = 'AM' if hours < 12 else 'PM'
	hours -= 12 if hours > 12 else 0

	hours = str(hours)

	return hours + ':' + minutes + ' ' + period