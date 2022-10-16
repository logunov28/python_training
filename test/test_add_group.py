# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="First_group", header="This is the first group.",
                           footer="I mean this group was created earlier than others."))
    app.group.return_to_groups_page()
    app.session.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.session.logout()

