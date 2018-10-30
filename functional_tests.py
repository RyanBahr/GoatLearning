from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    #def tearDown(self):
    #    self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        #Mike, as a 60-year-old man, has memory problems.
        #So, he goes to a website to help him remember things.
        self.browser.get('http://localhost:8000')

        #After seeing "To-Do" in the page header
        self.assertIn('To-Do', self.browser.title)
        #self.fail('Finish the test!')
        #He is invited to enter a to-do item straight away

        #He Types "Buy Marine Sniper Rifle into a text-box.
        #When he hits enter, the page updates, and now the page lists:
    #"1: Buy Marine Sniper Rifle"

    #There is still a text book which invites Mike to add another itemself.
    #He enters: "Kill Tuco Salamanca with the Sniper Rifle."

    #The page updates again, now showing both items on the listself.

    #Concerned over losing his progress, Mike sees that the site has
    #generated a custom URL for him and his list. There is some explanation
    #for this factself.

    #Whenever Mike visits this site, the to-do list is still the sameself.
    #Satisfied, Mike drinks a Beerself.
if __name__ == '__main__':
    unittest.main(warnings='ignore')
