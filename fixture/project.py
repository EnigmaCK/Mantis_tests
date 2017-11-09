
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

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/mantisbt-2.8.0/manage_proj_page.php"):
            self.app.open_home_page()
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
        self.open_projects_page()
        wd.find_element_by_xpath("//div[@class='row']//button[.='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//form[@id='manage-project-create-form']/div/div[3]/input").click()
        wd.find_element_by_link_text("Proceed").click()

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='manage_proj_edit_page.php?project_id=%s']" % id).click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        self.project_list = []
        tables = wd.find_elements_by_css_selector("tbody")
        for element in tables[0].find_elements_by_css_selector("tr"):
            cells = element.find_elements_by_css_selector("td")
            id = cells[0].find_element_by_css_selector("a").get_attribute("href")[69:maxsize]
            name = cells[0].text
            description = cells[4].text
            self.project_list.append(Project(id=id, name=name, description=description))
        return list(self.project_list)

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()



