import calendar
import datetime
from datetime import timedelta







def is_weekends():
    if datetime.datetime.today().weekday() == 6 or datetime.datetime.today().weekday() == 5:
        return True
    else:
        return False



def is_couple_of_lessons():
    x = datetime.datetime.now().strftime("%Y-%m-%d")
    para_1_start = datetime.datetime.strptime(f'{x}/9-30', "%Y-%m-%d/%H-%M")
    para_1_end = datetime.datetime.strptime(f'{x}/11-05', "%Y-%m-%d/%H-%M")
    para_2_start = datetime.datetime.strptime(f'{x}/11-20', "%Y-%m-%d/%H-%M")
    para_2_end = datetime.datetime.strptime(f'{x}/12-55', "%Y-%m-%d/%H-%M")
    para_3_start = datetime.datetime.strptime(f'{x}/13-10', "%Y-%m-%d/%H-%M")
    para_3_end = datetime.datetime.strptime(f'{x}/14-45', "%Y-%m-%d/%H-%M")
    para_4_start = datetime.datetime.strptime(f'{x}/15-25', "%Y-%m-%d/%H-%M")
    para_4_end = datetime.datetime.strptime(f'{x}/17-00', "%Y-%m-%d/%H-%M")
    para_5_start = datetime.datetime.strptime(f'{x}/17-15', "%Y-%m-%d/%H-%M")
    para_5_end = datetime.datetime.strptime(f'{x}/18-50', "%Y-%m-%d/%H-%M")
    odd_even = is_odd()
    week = datetime.datetime.today().weekday()
    now = datetime.datetime.now() + timedelta(hours=3)
    weekends = is_weekends()
    if odd_even == True:
        if week == 0:
            if now > para_1_start and now < para_1_end:
                minutes_diff = int((para_1_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 1 пара.До конца осталось {minutes_diff}"
            elif now > para_2_start and now < para_2_end:
                minutes_diff = int((para_2_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 2 пара.До конца осталось {minutes_diff}"
            elif now > para_3_start and now < para_3_end:
                minutes_diff = int((para_3_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 3 пара.До конца осталось {minutes_diff}"
            elif now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff}"
            elif now > para_5_start and now < para_5_end:
                minutes_diff = int((para_5_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 5 пара.До конца осталось {minutes_diff}"
            else:
                return "Сейчас нет пары"
        elif week == 1:
            if now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff} "
            elif now > para_5_start and now < para_5_end:
                minutes_diff = int((para_5_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 5 пара.До конца осталось {minutes_diff}"
            else:
                return "Сейчас нет пары"
        elif week == 2:
            if now > para_2_start and now < para_2_end:
                minutes_diff = int((para_2_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 2 пара.До конца осталось {minutes_diff}"
            elif now > para_3_start and now < para_3_end:
                minutes_diff = int((para_3_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 3 пара.До конца осталось {minutes_diff}"
            elif now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff} "
            else:
                return "Сейчас нет пары"
        elif week == 3:
            if now > para_2_start and now < para_2_end:
                   minutes_diff = int((para_2_end - now).total_seconds() // 60)
                   if minutes_diff > 60:
                       minutes_diff = f"1 час {minutes_diff - 60} минут"
                   else:
                       minutes_diff = f"{minutes_diff} минут"
                   return f"Сейчас идет 2 пара.До конца осталось {minutes_diff}"
            elif now > para_3_start and now < para_3_end:
                minutes_diff = int((para_3_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 3 пара.До конца осталось {minutes_diff}"
            elif now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff}"
            elif now > para_5_start and now < para_5_end:
                minutes_diff = int((para_5_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 5 пара.До конца осталось {minutes_diff}"
            else:
                return "Сейчас нет пары"
        elif week == 4:
          if now > para_3_start and now < para_3_end:
              minutes_diff = int((para_3_end - now).total_seconds() // 60)
              if minutes_diff > 60:
                  minutes_diff = f"1 час {minutes_diff - 60} минут"
              else:
                  minutes_diff = f"{minutes_diff} минут"
              return f"Сейчас идет 3 пара.До конца осталось {minutes_diff}"
          elif now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff}"
          else:
              return "Сейчас нет пары"

    elif odd_even == False:
        if week == 0:
            if now > para_1_start and now < para_1_end:
                minutes_diff = int((para_1_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 1 пара.До конца осталось {minutes_diff}"
            elif now > para_2_start and now < para_2_end:
                minutes_diff = int((para_2_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 2 пара.До конца осталось {minutes_diff}"
            elif now > para_3_start and now < para_3_end:
                minutes_diff = int((para_3_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 3 пара.До конца осталось {minutes_diff}"
            elif now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff}"
            elif now > para_5_start and now < para_5_end:
                minutes_diff = int((para_5_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 5 пара.До конца осталось {minutes_diff}"
            else:
                return "Сейчас нет пары"
        elif week == 1:
            if now > para_1_start and now < para_1_end:
                minutes_diff = int((para_1_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 1 пара.До конца осталось {minutes_diff}"
            elif now > para_2_start and now < para_2_end:
                minutes_diff = int((para_2_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 2 пара.До конца осталось {minutes_diff}"
            elif now > para_3_start and now < para_3_end:
                minutes_diff = int((para_3_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 3 пара.До конца осталось {minutes_diff}"
            elif now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff}"
            elif now > para_5_start and now < para_5_end:
                minutes_diff = int((para_5_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 5 пара.До конца осталось {minutes_diff}"
            else:
                return "Сейчас нет пары"
        elif week == 2:
            if now > para_3_start and now < para_3_end:
                minutes_diff = int((para_3_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 3 пара.До конца осталось {minutes_diff} минут"
            elif now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff}"
            else:
                return "Сейчас нет пары"
        elif week == 3:
            if now > para_2_start and now < para_2_end:
                minutes_diff = int((para_2_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 2 пара.До конца осталось {minutes_diff}"
            elif now > para_3_start and now < para_3_end:
                minutes_diff = int((para_3_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 3 пара.До конца осталось {minutes_diff}"
            elif now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff}"
            elif now > para_5_start and now < para_5_end:
                minutes_diff = int((para_5_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 5 пара.До конца осталось {minutes_diff}"
            else:
                return "Сейчас нет пары"
        elif week == 4:
            if now > para_3_start and now < para_3_end:
                minutes_diff = int((para_3_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 3 пара.До конца осталось {minutes_diff}"
            elif now > para_4_start and now < para_4_end:
                minutes_diff = int((para_4_end - now).total_seconds() // 60)
                if minutes_diff > 60:
                    minutes_diff = f"1 час {minutes_diff - 60} минут"
                else:
                    minutes_diff = f"{minutes_diff} минут"
                return f"Сейчас идет 4 пара.До конца осталось {minutes_diff}"
            else:
                return "Сейчас нет пары"


def today_is():
    result = ""
    odd_even = is_odd()
    weekday = datetime.datetime.today().weekday()
    if odd_even == True:
        result += "0"
        if weekday == 0:
            result += str(weekday)
        elif weekday == 1:
            result +=str(weekday)
        elif weekday == 2:
            result +=str(weekday)
        elif weekday == 3:
            result +=str(weekday)
        elif weekday == 4:
            result +=str(weekday)
        elif weekday == 5:
            result = "66"
        elif weekday == 6:
            result = "66"
    elif odd_even == False:
        result += "1"
        if weekday == 0:
            result += str(weekday)
        elif weekday == 1:
            result +=str(weekday)
        elif weekday == 2:
            result +=str(weekday)
        elif weekday == 3:
            result +=str(weekday)
        elif weekday == 4:
            result +=str(weekday)
        elif weekday == 5:
            result = "66"
        elif weekday == 6:
            result = "66"
    return result

def tommorow_is():
    result = ""
    odd_even = is_odd()
    weekday = datetime.datetime.today().weekday()
    if odd_even == True:
        if weekday == 6 :
            result = "10"
        else:
            result += "0"
        if weekday == 0:
            result += str(weekday+1)
        elif weekday == 1:
            result +=str(weekday+1)
        elif weekday == 2:
            result +=str(weekday+1)
        elif weekday == 3:
            result +=str(weekday+1)
        elif weekday == 4:
            result = "66"
        elif weekday == 5:
            result = "66"
    elif odd_even == False:
        if weekday == 6:
            result = "00"
        else:
            result += "1"
        if weekday == 0:
            result += str(weekday + 1)
        elif weekday == 1:
            result += str(weekday + 1)
        elif weekday == 2:
            result += str(weekday + 1)
        elif weekday == 3:
            result += str(weekday + 1)
        elif weekday == 4:
            result = "66"
        elif weekday == 5:
            result = "66"
    return result






def is_odd():
    now = datetime.datetime.now()
    sep = datetime.datetime(now.year if now.month >= 9 else now.year - 1, 9, 1)

    d1 = sep - timedelta(days=sep.weekday())
    d2 = now - timedelta(days=now.weekday())

    parity = ((d2 - d1).days // 7) % 2
    if parity:
        return False
    else:
        return True



























