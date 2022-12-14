from model.contact import Contact
from model.group import Group
import random



def test_del_contact_from_group(app, orm):
    groups = orm.get_group_list()
    if len(groups) == 0:
        app.group.return_to_groups_page()
        app.group.create(Group(name="test"))
        groups = orm.get_group_list()
    random_group = random.choice(groups)
    contacts = orm.get_contact_list()
    if len(contacts) == 0:
        app.contact.add(Contact(firstname="Kurt", middlename="Donald", lastname="Kobain", nickname="idk", title="idk",
                                company="Nirvana", address="Aberdeen USA", home_phone="+1999999", mobile_phone="None",
                                work_phone="None", fax="None",
                                email="kobain@bk.biz", email2="kobain@bk.org", email3="kobain@bk.com",
                                homepage="nirvana.com",
                                birthday="4", month_of_birth="March", year_of_birth="1967", anniversary_day="10",
                                anniversary_month="October", anniversary_year="2022", address2="New York",
                                phone2="25", notes="still alive"))
        contacts = orm.get_contact_list()
    old_contacts = orm.get_contacts_in_group(random_group)
    if len(old_contacts) == 0:
        random_contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_group_by_id(random_contact.id, random_group.id)
    else:
        random_contact = random.choice(contacts)
    old_contacts = orm.get_contacts_in_group(random_group)
    app.contact.delete_contact_from_group(random_contact.id, random_group.id)
    new_contacts = orm.get_contacts_in_group(random_group)
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
