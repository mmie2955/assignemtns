import datetime
def days_in_months(year, month):
    '''
    inputs:
    :param year: integer between minimum year and maximum year
    :param month: integer between 1 and 12
    :return: number of days
    '''

    if month==12:
        return 31
    else:
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year, month+1,1)
        difference = date2 - date1
        return(difference.days)
def is_valid_date(year, month, day):
    if datetime.MINYEAR<=year<=datetime.MAXYEAR and 1<=month<=12 and 1<=day<=31:
        return True
    else:
        print("The data you introduced is not correct")
        # date1 is the day the user was born, and day2 is the current date
def days_between(year1, month1, day1, year2, month2, day2):
    date1=datetime.date(year1,month1,day1)
    date2=datetime.date(year2,month2,day2)
    if is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2) and (date1<date2):
        difference=date2-date1
        return difference.days
    else:
        return 0
def age_in_days(year, month, day):
    '''
    inputs: birthday year, month and day
    '''
def todays_date(year, month, day):
    todays_date=datetime.date()
    print("Today's date:", todays_date)


    if is_valid_date(year, month, day) :
        return days_between(age_in_days(year, month, day), todays_date(year, month,day))
    else:
        return 0

