from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, json_contacts, orm):
    groups = orm.get_group_list()
    if len(groups) == 0:
        app.group.return_to_groups_page()
        app.group.create(Group(name="new_group"))
        groups = orm.get_group_list()
    random_group = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(random_group)
    if len(contacts) == 0:
        app.contact.open_add_new_page()
        app.contact.add(json_contacts)
        contacts = orm.get_contacts_not_in_group(random_group)
    random_contact = random.choice(contacts)
    old_contacts = orm.get_contacts_in_group(random_group)
    app.contact.add_contact_to_group_by_id(random_contact.id, random_group.id)
    new_contacts = orm.get_contacts_in_group(random_group)
    old_contacts.append(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
