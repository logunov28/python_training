from model.group import Group

def test_modify_group_name(app):
    app.open_home_page()
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New name"))
    app.group.return_to_groups_page()

def test_modify_group_header(app):
    app.open_home_page()
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    app.group.modify_first_group(Group(header="New header"))
    app.group.return_to_groups_page()

