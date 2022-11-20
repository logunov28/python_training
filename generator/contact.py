import random, string, os.path, jsonpickle, getopt, sys
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    day = str(random.randint(1, 28))
    return day


def random_month():
    month = random.choice(["January", "February", "March", "April", "May", "June", "July", "August",
                           "September", "October", "November", "December"])
    return month


def random_year():
    year = str(random.randint(1, 9999))
    return year


test_data = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                     home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="", homepage="",
                     birthday="0", month_of_birth="-", year_of_birth="", anniversary_day="0", anniversary_month="-",
                     anniversary_year="", address2="", phone2="", notes="")] + [Contact(firstname=random_string('firstname', 10), middlename=random_string('middlename', 10),
                     lastname=random_string('lastname', 10), nickname=random_string('nickname', 10), title=random_string('title', 10),
                     company=random_string('company', 10), address=random_string('address', 20), home_phone=random_string('home_phone', 12),
                     mobile_phone=random_string('mobile_phone', 12), work_phone=random_string('work_phone', 12), fax=random_string('fax', 10),
                     email=random_string('email', 10), email2=random_string('email2', 10), email3=random_string('email3', 10),
                     homepage=random_string('homepage', 10), birthday=random_day(), month_of_birth=random_month(), year_of_birth=random_year(),
                     anniversary_day=random_day(), anniversary_month=random_month(), anniversary_year=random_year(), address2=random_string('address2', 10),
                     phone2=random_string('phone2', 12), notes=random_string('notes', 20)) for i in range(n)]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
