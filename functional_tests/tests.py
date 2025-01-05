from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
         # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get(self.live_server_url)
        # เธอเห็น Title และ Header ที่เกี่ยวกับ To-Do
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # เธอเพิ่มรายการ "Buy peacock feathers"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # หน้าเว็บแสดงรายการที่เพิ่มเข้าไป
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])

        # เธอเพิ่มรายการ "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # หน้าเว็บอัปเดตแสดงทั้งสองรายการ
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        self.assertIn("2: Use peacock feathers to make a fly", [row.text for row in rows])
