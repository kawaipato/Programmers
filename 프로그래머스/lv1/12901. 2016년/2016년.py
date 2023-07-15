import datetime
def solution(a, b):
    day = datetime.date(2016,a,b)
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return days[day.weekday()]