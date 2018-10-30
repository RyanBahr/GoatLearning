from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        #Mike, as a 60-year-old man, has memory problems.
        #So, he goes to a website to help him remember things.
        self.browser.get('http://localhost:8000')

        #After seeing "To-Do" in the page header
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #He Types "Buy Marine Sniper Rifle into a text-box.
        inputbox.send_keys('Buy Marine Sniper Rifle')
        #When he hits enter, the page updates, and now the page lists:
        #"1: Buy Marine Sniper Rifle"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy Marine Sniper Rifle' for row in rows),
            "New to-do item did not appear in table"
        )
    #There is still a text book which invites Mike to add another itemself.
    #He enters: "Kill Tuco Salamanca with the Sniper Rifle."
        self.fail('Finish the test!')
    #The page updates again, now showing both items on the listself.

    #Concerned over losing his progress, Mike sees that the site has
    #generated a custom URL for him and his list. There is some explanation
    #for this factself.

    #Whenever Mike visits this site, the to-do list is still the sameself.
    #Satisfied, Mike drinks a Beerself.
if __name__ == '__main__':
    unittest.main(warnings='ignore')
