from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy Marine Sniper Rifle')

    #There is still a text book which invites Mike to add another item.
    #He enters: "2: Kill Tuco Salamanca with the Sniper Rifle."
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Kill Tuco Salamanca with the Sniper Rifle.')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
    #The page updates again, now showing both items on the list.
        self.check_for_row_in_list_table('1: Buy Marine Sniper Rifle')
        self.check_for_row_in_list_table('2: Kill Tuco Salamanca with the Sniper Rifle.')



    #Concerned over losing his progress, Mike sees that the site has
    #generated a custom URL for him and his list. There is some explanation
    #for this fact.
        self.fail('Finish the test!')

    #Whenever Mike visits this site, the to-do list is still the sameself.
    #Satisfied, Mike drinks a Beerself.
if __name__ == '__main__':
    unittest.main(warnings='ignore')
