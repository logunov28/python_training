from model.contact import Contact
from random import *

def test_edit_contact(app, db, json_contacts, check_ui):
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    #contact = json_contacts
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.add(contact)
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

