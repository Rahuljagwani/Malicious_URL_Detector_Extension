import re
import pandas as pd
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from tld import get_tld
from joblib import dump

data = pd.read_csv('/home/rahul/RTUAmlServer/urldata.csv')
data['url'] = data['url'].replace('www.', '', regex=True)
data['url_len'] = data['url'].apply(lambda x: len(str(x)))


def process_tld(url):
    try:
        res = get_tld(url, as_object=True,
                      fail_silently=False, fix_protocol=True)
        pri_domain = res.parsed_url.netloc
    except:  # noqa
        pri_domain = None
    return pri_domain


data['domain'] = data['url'].apply(lambda i: process_tld(i))

feature = ['@', '?', '-', '=', '.', '#', '%', '+', '$', '!', '*', ',', '//']
for a in feature:
    data[a] = data['url'].apply(lambda i: i.count(a))


def httpSecure(url):
    htp = urlparse(url).scheme
    match = str(htp)
    if match == 'https':
        # print match.group()
        return 1
    else:
        # print 'No matching pattern found'
        return 0


data['https'] = data['url'].apply(lambda i: httpSecure(i))


def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits


data['digits'] = data['url'].apply(lambda i: digit_count(i))


def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters


data['letters'] = data['url'].apply(lambda i: letter_count(i))


def Shortining_Service(url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'  # noqa
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'  # noqa
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'  # noqa
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'  # noqa
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'  # noqa
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'  # noqa
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'  # noqa
                      'tr\.im|link\.zip\.net',  # noqa
                      url)
    if match:
        return 1
    else:
        return 0


data['Shortining_Service'] = data['url'].apply(lambda x: Shortining_Service(x))


def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'  # noqa
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'  # noqa
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4 with port
        # IPv4 in hexadecimal
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)'  # noqa
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|'
        '([0-9]+(?:\.[0-9]+){3}:[0-9]+)|'  # noqa
        '((?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)(?:\/\d{1,2})?)', url)  # Ipv6  # noqa
    if match:
        return 1
    else:
        return 0


data['having_ip_address'] = data['url'].apply(lambda i: having_ip_address(i))

data['having_ip_address'].value_counts()

data.head()

X = data.drop(['url', 'domain', 'label', 'Unnamed: 0',
              'result'], axis=1)  # ,'type_code'
y = data['result']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2)

model = RandomForestClassifier()

ip = "https://www.youtube.com/"
ip = ip.replace('www.', '')
iplen = len(ip)
process_tld(ip)
feature = ['@', '?', '-', '=', '.', '#', '%', '+', '$', '!', '*', ',', '//']
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0
a9 = 0
a10 = 0
a11 = 0
a12 = 0
a13 = 0
for a in ip:
    if a == '@':
        a1 += 1
    if a == '?':
        a2 += 1
    if a == '-':
        a3 += 1
    if a == '=':
        a4 += 1
    if a == '.':
        a5 += 1
    if a == '#':
        a6 += 1
    if a == '%':
        a7 += 1
    if a == '+':
        a8 += 1
    if a == '$':
        a9 += 1
    if a == '!':
        a10 += 1
    if a == '*':
        a11 += 1
    if a == ',':
        a12 += 1
    if a == '//':
        a13 += 1
http_s = httpSecure(ip)
dc = digit_count(ip)
lc = letter_count(ip)
ss = Shortining_Service(ip)
is_ip = having_ip_address(ip)
input = [[iplen, a1, a2, a3, a4, a5, a6, a7, a8, a9,
          a10, a11, a12, a13, http_s, dc, lc, ss, is_ip]]
model.fit(X_train.values, y_train.values)
model.predict(input)
dump(model, 'model1.joblib')
