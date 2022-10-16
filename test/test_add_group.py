# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="First_group", header="This is the first group.",
                      footer="I mean this group was created earlier than others."))
    app.return_to_groups_page()
    app.session.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group(name="", header="", footer=""))
    app.return_to_groups_page()
    app.session.logout()

