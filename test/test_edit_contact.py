from model.contact import Contact


def test_edit_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Kurt", middlename="Donald", lastname="Kobain", nickname="idk", title="idk",
                            company="Nirvana", address="Aberdeen USA", home_phone="+1999999", mobile_phone="None", work_phone="None", fax="None",
                            email="kobain@bk.biz", email2="kobain@bk.org", email3="kobain@bk.com", homepage="nirvana.com",
                            birthday="4", month_of_birth="March", year_of_birth="1967", anniversary_day="10", anniversary_month="October", anniversary_year="2022", address2="New York",
                            phone2="25", notes="still alive"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivanov", middlename="Ivan", lastname="Ivanych", nickname="Vano", title="III",
                            company="Teplopribor", address="Novohopersk, Voronezh region, Russia", home_phone="2-16-34", mobile_phone="+79523635511", work_phone="02", fax="broken",
                            email="vano@mail.ru", email2="vano@ya.ru", email3="none", homepage="ivanivanov.ru",
                            birthday="14", month_of_birth="May", year_of_birth="1989", anniversary_day="1", anniversary_month="July", anniversary_year="2023", address2="Moscow, Red Square",
                            phone2="3-37-69", notes="A good engineer")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
