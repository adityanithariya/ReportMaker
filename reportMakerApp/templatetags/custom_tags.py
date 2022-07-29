from django.template import Library
register = Library()

def get_time(value):
    return value.strftime("%I:%M%p").lower()

def split(value, arg):
    return str(value).split(arg)

register.filter("get_time", get_time)
register.filter("split", split)