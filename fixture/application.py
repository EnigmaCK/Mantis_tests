
from selenium import webdriver
from fixture.session import SessionHelper



class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url == "http://localhost/mantisbt-2.8.0/my_view_page.php"):
            wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        if not (wd.current_url == "http://localhost/mantisbt-2.8.0/my_view_page.php"):
            wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()