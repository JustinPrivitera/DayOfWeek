from StringToken import stringToken
import datetime

def dayConverter(day):
	if day == 0:
		return "Monday"
	if day == 1:
		return "Tuesday"
	if day == 2:
		return "Wednesday"
	if day == 3:
		return "Thursday"
	if day == 4:
		return "Friday"
	if day == 5:
		return "Saturday"
	if day == 6:
		return "Sunday"
	if day == -1:
		return "Arguments entered were not recognized as a valid date."

def dayOfWeek(date):
	if testValidity(date) == True:
		now = datetime.datetime.now()
		day = datetime.datetime.today().weekday()
		date = stringToken(date, "/")
		if len(date[2]) == 4:
			date[2] = date[2][2:]
		for i in range(0, len(date)):
			date[i] = int(date[i])
		count = countDays([int(now.month), int(now.day), int(now.year)], date)
		return (count + day) % 7
	else:
		return -1

def countDays(date1, date2):
	count = 0
	for i in range(date1[2], date2[2]):
		count += 365
		if i % 4 == 0:
			count += 1
	for i in range(date1[0], date2[0]):
		if i == 9 or i == 4 or i == 6 or i == 11:
			count += 30
		elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
			count += 31
		else:
			count += 28
	for i in range(date1[1], date2[1]):
		count += 1
	return count

def testValidity(date): # could easily be more robust
	date = stringToken(date, "/")
	if len(date) != 3:
		return False
	if len(date[0]) != 2:
		return False
	if len(date[1]) != 2:
		return False
	if len(date[2]) != 2 and len(date[2]) != 4:
		return False
	for i in range(0, 3):
		for j in range(0, len(date[i])):
			if date[i][j] not in "1234567890":
				return False
	if int(date[0]) == 0 or int(date[0]) > 12:
		return False
	if int(date[1]) == 0 or int(date[1]) > 31:
		return False
	if int(date[2]) < int(datetime.datetime.now().year):
		return False
	return True
