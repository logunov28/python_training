from model.contact import Contact
from random import *
import random

def test_modify_contact(app, db, json_contacts, check_ui):
    old_contacts = db.get_contact_list()
    contact = json_contacts
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.add(contact)
    random_contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(random_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

