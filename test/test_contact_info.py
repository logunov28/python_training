from model.contact import Contact
import re

def test_info_on_home_page(app, db):
    db_contacts = db.get_contact_list()
    for i in db_contacts:
        i.all_emails_from_home_page = merge_emails_like_on_home_page(i)
        i.all_phones_from_home_page = merge_phones_like_on_home_page(i)
    db_contacts = sorted(db_contacts, key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(db_contacts) == len(contacts_from_home_page)
    assert db_contacts == contacts_from_home_page
    for i in range(len(db_contacts)):
        print(str(i))
        print(db_contacts[i])
        print(contacts_from_home_page[i])

    for i in range(len(db_contacts)):
        assert db_contacts[i].id == contacts_from_home_page[i].id
        assert db_contacts[i].firstname == contacts_from_home_page[i].firstname
        assert db_contacts[i].lastname == contacts_from_home_page[i].lastname
        assert db_contacts[i].address == contacts_from_home_page[i].address
        assert db_contacts[i].all_phones_from_home_page == contacts_from_home_page[i].all_phones_from_home_page
        assert db_contacts[i].all_emails_from_home_page == contacts_from_home_page[i].all_emails_from_home_page


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
