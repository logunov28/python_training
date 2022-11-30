from model.group import Group
from random import *
import random

def test_modify_group_name(app, db, json_groups, check_ui):
    app.open_home_page()
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    app.group.return_to_groups_page()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_modify_group_header(app):
#    app.open_home_page()
#    app.group.open_groups_page()
#    old_groups = app.group.get_group_list()
#    group = Group(header="New header")
#    group.id = old_groups[0].id
#    if app.group.count() == 0:
#        app.group.create(Group(header="test"))
#    app.group.modify_first_group(group)
#    app.group.return_to_groups_page()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

