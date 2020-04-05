from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_cat_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mentions to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

if __name__ == "__main__":
    unittest.main(warnings="ignore")