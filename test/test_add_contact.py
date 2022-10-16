from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_add_new_page()
    app.contact.add(Contact(firstname="Kurt", middlename="Donald", lastname="Kobain", nickname="idk", title="idk",
                            company="Nirvana", address="Aberdeen USA", home_phone="+1999999", mobile_phone="None", work_phone="None", fax="None",
                            email="kobain@bk.biz", email2="kobain@bk.org", email3="kobain@bk.com", homepage="nirvana.com",
                            birthday="4", month_of_birth="March", year_of_birth="1967", anniversary_day="10", anniversary_month="October", anniversary_year="2022", address2="New York",
                            phone2="25", notes="still alive"))
    app.session.logout()
