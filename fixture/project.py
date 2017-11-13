
from model.project import Project
from sys import maxsize


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()

    def open_manage_progects_tab(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def open_projects_page(self, config):
        wd = self.app.wd
        if not (wd.current_url == config['web']['baseURL'] + "/manage_proj_page.php"):
            self.app.open_home_page(self.app.config)
            self.open_manage_page()
            self.open_manage_progects_tab()

    def change_field_values(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_values("name", project.name)
        self.change_field_values("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page(self.app.config)
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='manage_proj_edit_page.php?project_id=%s']" % id).click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page(self.app.config)
        self.project_list = []
        tables = wd.find_elements_by_css_selector("tbody")
        row_list = tables[2].find_elements_by_css_selector("tr.row-1")
        for el in tables[2].find_elements_by_css_selector("tr.row-2"):
            row_list.append(el)
        for element in row_list:
            cells = element.find_elements_by_css_selector("td")
            id = cells[0].find_element_by_css_selector("a").get_attribute("href")[70:maxsize]
            name = cells[0].text
            description = cells[4].text
            self.project_list.append(Project(id=id, name=name, description=description))
        return list(self.project_list)

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_projects_page(self.app.config)
        self.select_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()



