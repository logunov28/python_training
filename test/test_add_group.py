# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups):
    group = json_groups
    app.open_home_page()
    app.group.open_groups_page()
    old_groups = db.get_group_list()
    app.group.create(group)
    app.group.return_to_groups_page()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def clear(group):
    for i in group:
        if i.name is not None:
            i.name = ' '.join(i.name.split())
            i.name = i.name.strip()
    return group
