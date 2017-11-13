
from model.project import Project
import random


def test_add_project(app, config):
    app.session.ensure_login(username=config['webadmin']['username'], password=config['webadmin']['password'])
    old_projects = app.project.get_project_list()
    project = Project(name="Test12" + str(random.randrange(0, 10000)), description="Description")
    app.project.create(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    for el in old_projects:
        print(el)
    print("____________________________________________________________")
    for el in new_projects:
        print(el)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
