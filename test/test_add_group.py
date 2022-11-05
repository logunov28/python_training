# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name="First_group", header="This is the first group.",
                           footer="I mean this group was created earlier than others.")
    app.group.create(group)
    app.group.return_to_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_empty_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    app.group.return_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

