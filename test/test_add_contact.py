from model.contact import Contact
import string, random, pytest, datetime

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
                     birthday="", month_of_birth="", year_of_birth="", anniversary_day="", anniversary_month="-",
                     anniversary_year="", address2="", phone2="", notes="")] + [Contact(firstname=random_string('firstname', 10), middlename=random_string('middlename', 10),
                     lastname=random_string('lastname', 10), nickname=random_string('nickname', 10), title=random_string('title', 10),
                     company=random_string('company', 10), address=random_string('address', 20), home_phone=random_string('home_phone', 12),
                     mobile_phone=random_string('mobile_phone', 12), work_phone=random_string('work_phone', 12), fax=random_string('fax', 10),
                     email=random_string('email', 10), email2=random_string('email2', 10), email3=random_string('email3', 10),
                     homepage=random_string('homepage', 10), birthday=random_day(), month_of_birth=random_month(), year_of_birth=random_year(),
                     anniversary_day=random_day(), anniversary_month=random_month(), anniversary_year=random_year(), address2=random_string('address2', 10),
                     phone2=random_string('phone2', 12), notes=random_string('notes', 20))]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_page()
    app.contact.add(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
