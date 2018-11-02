from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise # -*- coding: utf-8 -*-
                time.sleep(0.5)
    def test_can_start_a_list_for_one_user(self):
        #Mike, as a 60-year-old man, has memory problems.
        #So, he goes to a website to help him remember things.
        time.sleep(10)
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Buy Marine Sniper Rifle')

    #There is still a text book which invites Mike to add another item.
    #He enters: "2: Kill Tuco Salamanca with the Sniper Rifle."
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Kill Tuco Salamanca with the Sniper Rifle.')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
    #The page updates again, now showing both items on the list.
        #self.wait_for_row_in_list_table('1: Buy Marine Sniper Rifle')
        self.wait_for_row_in_list_table('2: Kill Tuco Salamanca with the Sniper Rifle.')
        self.wait_for_row_in_list_table('1: Buy Marine Sniper Rifle')
        
    def test_multiple_users_can_start_lists_at_different_urls(self):
        #Mike makes a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Marine Sniper Rifle')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Marine Sniper Rifle')
    #Concerned over losing his progress, Mike sees that the site has
        mike_list_url = self.browser.current_url
        self.assertRegex(mike_list_url, '/lists/.+')

    #Now, a second user, Franciss, comes along to the siteself.
    ##e use a new browser session to make sure that no information
    ## of Mike's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Francis visits the home page. There is no sign of Edith's lists
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy Marine Sniper Rifle', page_text)
        self.assertNotIn('Kill Tuco Salamanca with the Sniper Rifle', page_text)

        #Francis starts a new list by entering a new item. He is less interesting than Mike
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        #Francis gets his OWN url
        francis_list_url = self.browser.current_url
        self.assertRegex(francis-list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #Again, NO trace of Mike's list. He'd get mad!
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

    #generated a custom URL for him and his list. There is some explanation
    #for this fact

        self.fail('Finish the test!')

    #Whenever Mike visits this site, the to-do list is still the sameself.
    #Satisfied, Mike drinks a Beerself.
