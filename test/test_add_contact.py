from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_page()
    contact = Contact(firstname="Kurt", middlename="Donald", lastname="Kobain", nickname="idk", title="idk",
                            company="Nirvana", address="Aberdeen USA", home_phone="+1999999", mobile_phone="None", work_phone="None", fax="None",
                            email="kobain@bk.biz", email2="kobain@bk.org", email3="kobain@bk.com", homepage="nirvana.com",
                            birthday="4", month_of_birth="March", year_of_birth="1967", anniversary_day="10", anniversary_month="October", anniversary_year="2022", address2="New York",
                            phone2="25", notes="still alive")
    app.contact.add(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
