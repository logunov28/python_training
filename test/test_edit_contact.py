from model.contact import Contact
from random import randrange

def test_edit_contact(app, json_contacts):
    old_contacts = app.contact.get_contact_list()
    contact = json_contacts
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.add(contact)
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

