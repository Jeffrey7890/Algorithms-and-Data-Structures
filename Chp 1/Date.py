# Implements a proleptic Gregorian calendar date as a Julian day number

class Date:
	# Creates an  object instance for the specified Gregorian date.
	def __init__(self, month, day, year):
		self._julianDay = 0
		assert self._isValidGregorian(month, day, year), "Invalid Gregorian date."

		# The first line of the equation, T =(M-14)/12 has to be changed
		# since Python's implementation of integer division is not the same
		# as the mathematical definition.
		tmp = 0
		if month < 3:
			tmp =-1
		self._julianDay = day - 32075 +\
				 (1461*(year + 4800 + tmp)//4) +\
				 (367*(month-2-tmp*12)//12) -\
				 (3*((year + 4900+tmp)//100)//4)

	# Extracts the appropriate Gregorian date component.
	def month(self):
		return (self._toGregorian())[0] # returning M from (M, d, y)

	def day(self):
		return (self._toGregorian())[1] # returning D from (m, D, y)

	def year(self):
		return (self._toGregorian())[2]  # returning Y from (m, d, Y)

	def monthName(self):
		months = {1:"January", 2:"Febuary",
				  3:"March", 4:"April",
				  5:"May" , 6:"June",
				  7:"July", 8: "August",
				  9:"September", 10:"October",
				  11:"November", 12:"December"
					}
		return months[self._toGregorian()[0]] # returning the name of the month

	# Check if year is leap year.
	def isLeapYear(self,year = None):
		if year == None:	
			year =self. _toGregorian()[2]
		if year%4 == 0:
			if year % 100 == 0:
				if year % 400 == 0:
					return True
				else:
					return False
			else:
				return True
		else:
			return False

	def numDays(self, otherDate):
		return self._julianDay - otherDate._julianDay # returns number of days between the other date.

	def advanceBy(self, days):
		self._julianDay+=days # Advances Days by number of days


	# Returns name of the day
	def dayOfWeekName(self):
		daysName = {0:"Sunday",1:"Monday", 2:"Tuesday",
					3: "Wednesday",4:"Thursday",
					5:"Friday", 6:"Saturday",
					}
		return daysName[self.dayOfWeek()]

	# returns and integer indicating the day of the year.
	def dayOfYear(self):
		pass

	# determines if the date is a weekday.
	def isWeekday(self):
		pass

	# determines if the date is the spring or autumn equinox.
	def isEquinox(self):
		pass

	# determines if the date is the summer or winter solstice.
	def isSolstice(self):
		pass

	def printCalendar(self):
		month = self._toGregorian()[0]
		year = self._toGregorian()[2]
		day = 1
		if month < 3:
			month = month +12
			year = year-1

		dayofWeek = ((13*month +3)//5 + day+\
			year + year//4 - year // 100+year//400)%7
		n = 0
		cnt = 0
		thirty = [8,4,6,11]
		print("\t", self.monthName(),year)
		print("Su\tMo\tTu\tWe\tTh\tFr\tSa")
		for i in range(5):
			for j in range(7):
				if cnt <= dayofWeek:
					print(" ", end="\t")
				else:
					n+=1
					print(n, end = "\t")
				cnt+=1
				if month in thirty and n == 30:
					break 
				elif month == 2:
					if self.isLeapYear(year) == True and n == 29:
						break
					elif self.isLeapYear(year) != True and n == 28:
						break
				elif n == 31:
					break

			print(" ")


	# Returns day of the week as an int between 0 (Mon) and 6 (Sun)
	def dayOfWeek(self):
		month, day,year = self._toGregorian()
		if month < 3:
			month = month +12
			year = year-1

		return ((13*month +3)//5 + day+\
			year + year//4 - year // 100+year//400)%7

	# Returns the date as a string in Gregorian format.
	def __str__(self):
		month, day, year = self._toGregorian()
		return "%02d/%02d/%04d" %(month, day, year)

	# Logically compares the two dates.
	def __eq__(self, otherDate):
		return self._julianDay == otherDate._julianDay

	def __lt__(self, otherDate):
		return self._julianDay < otherDate._julianDay

	def __le__(self,otherDate):
		return self._julianDay <= otherDate._julianDay

	# The remaining methods are to be included at this point.
	# ....
	def _isValidGregorian(self, month, day,year):

		thirty = [8,4,6,11]
		if year > 0:
			if month == 2:
				if self.isLeapYear(year) == False:
					if (0 < day <= 28):
						return True
					else:return False
				else:
					if (0 < day <= 29):
						return True
					else:
						return False

			if month in thirty:
				if(0<day <=30):
					return True
				else:return False

			if (0 < month <= 12) and (0<day<=31):
				return True
		return False


	# Returns the Gregorian date as a tuple: (month, day, year).
	def _toGregorian(self):
		A = self._julianDay + 68569
		B = 4*A//146097
		A = A-(146097 * B + 3)//4
		year = 4000 *(A+1) // 1461001
		A = A-(1461 *year//4)+ 31
		month = 80 * A//2447
		day = A-(2447 *month //80)
		A = month // 11
		month = month+2-(12*A)
		year = 100*(B-49)+year
		#print("year sdmfsdfasdf" , year)
		return month, day, year


if __name__ == '__main__':
	firstDay = Date(3,8,2022)
	firstDay.printCalendar()
