import json
import calendar
import random
from datetime import date, timedelta

import faker
import numpy as np
from pandas import DataFrame
from delorean import parse
import pandas as pd

#pd.set_option('display.mpl_style', 'default')

fake = faker.Faker()

usernames = set()
usr_num = 10

while len(usernames) < usr_num:
    usernames.add(fake.user_name())

def get_random_name_and_gender():
    skew = 0.6
    male = random.random() > skew
    if male:
        return fake.name_male(), 'M'
    else:
        return fake.name_female(), 'F'


def get_users(usernames):
    users = []
    for username in usernames:
        name, gender = get_random_name_and_gender()
        user = {
            'username': username,
            'name': name,
            'gender': gender,
            'email': fake.email(),
            'age': fake.random_int(min=18, max=90),
            'address': fake.address(),
        }
        users.append(json.dumps(user))
    return users


def get_type():
    types = ['AKR', 'BZY', 'CEM', 'BFG']
    return random.choice(types)


def get_start_end_dates():
    duration = random.randint(1, 2 * 365)
    offset = random.randint(-365, 365)
    start = date.today() - timedelta(days=offset)
    end = start + timedelta(days=duration)

    def _format_date(date_):
        return date_.strftime('%Y%m%d')

    return _format_date(start), _format_date(end)


def get_age():
    age = random.randint(20, 45)
    age -= age % 5
    diff = random.randint(5, 25)
    diff -= diff % 5
    return '{}-{}'.format(age, age + diff)


def get_gender():
    return random.choice(('M', 'F', 'B'))


def get_currency():
    return random.choice(('GBP', 'EUR', 'USD'))


def get_campaign_name():
    sep = '_'
    type_ = get_type()
    start_end = sep.join(get_start_end_dates())
    age = get_age()
    gender = get_gender()
    currency = get_currency()
    return sep.join((type_, start_end, age, gender, currency))


def get_campaign_data():
    name = get_campaign_name()
    budget = random.randint(10 ** 3, 10 ** 6)
    spent = random.randint(10 **2, budget)
    clicks = int(random.triangular(10 **2,  10 **5, 0.2 * 10 **5))
    impressions = random.gauss(0.5 * 10 **6, 2)
    return {
        'cmp_name': name,
        'cmp_budget': budget,
        'cmp_spent': spent,
        'cmp_clicks': clicks,
        'cmp_impr': impressions
    }


def get_data(users):
    data = []
    for user in users:
        campaigns = [get_campaign_data() for _ in range(random.randint(2,8))]
        data.append({'user': user, 'campaigns': campaigns})
    return data


def unpack_user_json(user):
    usr = json.loads(user.strip())
    return [
        usr['username'],
        usr['email'],
        usr['name'],
        usr['age'],
        usr['gender'],
        usr['address'],
    ]


def calc_extra_cols(df):
    df['CTR'] = df['campaigns']['cmp_clicks'] / df['campaigns']['cmp_impr']
    df['CPC'] = df['campaigns']['cmp_spent'] / df['campaigns']['cmp_clicks']
    df['CPI'] = df['campaigns']['cmp_spent'] / df['campaigns']['cmp_impr']



#print(users[:3])
#users[:3]
users = get_users(usernames)
rough_data = get_data(users)
print("--- rough data")
print(rough_data[:3])

print("--- data frame")
df = DataFrame(rough_data)
print(df[:3])

user_data = df['user'].apply(unpack_user_json)
user_cols = ['username', 'email', 'name', 'age', 'gender', 'address']
user_df = DataFrame(user_data.tolist(), columns=user_cols, index=df.index)
print(df.head())
print(df.count())

print("--- user data frame")
print(user_df)



