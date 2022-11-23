import random
from model.group import Group


def test_delete_some_group(app, db):
    app.open_home_page()
    app.group.open_groups_page()
    old_groups = db.get_group_list()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
