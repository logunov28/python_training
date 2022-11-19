# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    app.open_home_page()
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.create(group)
    app.group.return_to_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def clear(group):
    for i in group:
        if i.name is not None:
            i.name = ' '.join(i.name.split())
            i.name = i.name.strip()
    return group
