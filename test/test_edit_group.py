from model.group import Group

def test_edit_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit_first_group(Group(name="Edited_group", header="This is the edited group.",
                           footer="I mean this group was edited by you."))
    app.group.return_to_groups_page()
    app.session.logout()
