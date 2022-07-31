from datetime import datetime
from django.template import Library
register = Library()

def get_time(value):
    month = value.month
    date = value.date()
    dt = datetime.now()
    if dt.month > month:
        if dt.date() > date:
            return value.strftime("%d %b, %y")
        else:
            return value.strftime("%I:%M%p").lower()
    else:
        if dt.date() > date:
            return value.strftime("%d %b, %y")
        else:
            return value.strftime("%I:%M%p").lower()

def get_whole_time(value):
    return value.strftime("%I:%M%p ").lower() + value.strftime("%d %b, %y").lower()

def split(value, arg):
    return str(value).split(arg)

register.filter("get_time", get_time)
register.filter("get_whole_time", get_whole_time)
register.filter("split", split)