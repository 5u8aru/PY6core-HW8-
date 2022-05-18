"""
Д/З Було виконано відповідно до умови в Schoology, а саме: "Функция выводит пользователей для дней рождения
на следующей неделе", тобто виводить дні народження від понеділка наступної неділі + попередні вихідні. СЬОГОДНІШНІЙ
(18.05.2022) запуск функції надрукує тих, в кого д/н в період з (21.05.2022) по (27.05.2022). Також на руках версія
коду, яка надрукує список іменинників саме з запуску функції (18.05.2022) по (25.05.2022). Надсилаю код відповідно
умові в Schoology.
"""
from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {
        "name": "Yurij", "birthday": "2003-11-29"
    },
    {
        "name": "Aider", "birthday": "2012-05-19"
    },
    {
        "name": "Bill", "birthday": "2010-05-21"
    },
    {
        "name": "Jill", "birthday": "1997-05-23"
    },
    {
        "name": "Kim", "birthday": "1986-07-14"
    },
    {
        "name": "Steve", "birthday": "2008-05-27"
    },
    {
        "name": "John", "birthday": "1972-05-28"
    },
]

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def day_of_birth(date: str) -> str:
    current_datetime = datetime.now()
    d, m, y = date.split('-')
    date = datetime(year=current_datetime.year, month=int(m), day=int(y))
    d_name = days_name.get(date.weekday())
    return d_name


def congratulate(users: list) -> None:
    current_datetime = datetime.now()
    first_fr = datetime.now()
    one_week_interval = timedelta(days=6)
    one_day_interval = timedelta(days=1)
    any_days_interval = timedelta(days=5 - first_fr.weekday())
    if first_fr.weekday() == 5:
        second_fr = first_fr + one_week_interval
    elif first_fr.weekday() > 5:
        first_fr = first_fr - one_day_interval
        second_fr = first_fr + one_week_interval
    else:
        first_fr = first_fr + any_days_interval
        second_fr = first_fr + one_week_interval
    day_name = []
    for el in range(len(users)):
        date = users[el]["birthday"]
        d, m, y = date.split('-')
        date_n = datetime(year=current_datetime.year, month=int(m), day=int(y))
        if first_fr.date() <= date_n.date() <= second_fr.date():
            day = day_of_birth(date)
            day_name.append((day, users[el]["name"]))
    day_name_d = defaultdict(list)
    for k, v in day_name:
        if k == 'Saturday' or k == 'Sunday':
            day_name_d["Monday"].append(v)
        else:
            day_name_d[k].append(v)
    for k, v in day_name_d.items():
        print(k + ': ' + ','.join(v))


congratulate(users)
