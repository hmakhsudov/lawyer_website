from django import template

register = template.Library()

@register.filter
def duration_format(value):
    hours = int(value)
    minutes = int((value - hours) * 60)
    if hours > 0 and minutes > 0:
        return f"{hours} часов {minutes} минут"
    elif hours > 0:
        return f"{hours} часов"
    elif minutes > 0:
        return f"{minutes} минут"
    else:
        return ""



MONTH_NAMES = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря',
}

register = template.Library()

@register.filter(name='rus_date')
def rus_date(date):
    day = date.strftime('%d')
    month = date.month
    return f"{day} {MONTH_NAMES[month]}"

@register.filter(name='display_time')
def display_time(value):
    return value.strftime('%H:%M')  # Format the time as HH:MM