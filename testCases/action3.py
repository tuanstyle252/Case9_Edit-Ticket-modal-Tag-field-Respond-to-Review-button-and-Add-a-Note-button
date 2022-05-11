from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.loginPage import Loginpage
import time
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class Testaction:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassWord()

    def test_action1_1_1(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("13553")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        self.driver.switch_to.frame((self.driver.find_element(By.CLASS_NAME, "embed-responsive-item")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[1]/a"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li/input"))).click()
        lists = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='chosen-drop']/ul/li")))
        for list in lists:
            if list.text == "Annie test 2 updated":
                list.click()
                break

        #check tag
        argb = self.driver.find_element(By.XPATH, "//li[@class='search-choice']").value_of_css_property("background-color")
        check_hex = Color.from_string(argb).hex
        assert check_hex, '#00B0F2'

        # click x remove
        tag = self.driver.find_element(By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li[1]")
        if tag.is_displayed():
            self.driver.find_element(By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li[1]/a").click()
            assert True
        else:
            raise ValueError("tag is still show")

        #check search field and save buton are shown
        search_field = self.driver.find_element(By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li")
        if search_field.is_displayed():
            assert True
        else:
            raise ValueError("the search_field not show")

        save = self.driver.find_element(By.XPATH, "//*[@type='submit']")
        if save.is_displayed():
            assert True
        else:
            raise ValueError("the save_field not show")

        self.driver.quit()
    def test_action1_1_2(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("13553")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        self.driver.switch_to.frame((self.driver.find_element(By.CLASS_NAME, "embed-responsive-item")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[1]/a"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li/input"))).click()
        lists = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='chosen-drop']/ul/li")))
        list_ = ['0202_W test new tag 2 update', '0302 Annie Tags Test Updated', 'abc', 'Annie test 2 updated', 'Bathroom', 'BL_test Ticket GR 1/17', 'Carpet', 'D0202_Test Gr Updated', 'D0314_New Tag BL update', 'D0328_New Tag Updated', 'D0511_R_ New Tag Updated', 'Lobby', 'New Tag 1', 'Pool', 'S Test Tag on Group 0214 Updated', 'S Test Tag on Group 0214_Test 2 updated', 'Tag3', 'Test 4 updated 01/19', 'WT01 Updated']
        ar = []
        for list in lists:
            ar.append(list.text)

        assert list_ == ar
        self.driver.close()

    def test_action1_1_3(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("13553")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        self.driver.switch_to.frame((self.driver.find_element(By.CLASS_NAME, "embed-responsive-item")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[1]/a"))).click()
        time.sleep(3)
        input = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li/input")))
        actions = ActionChains(self.driver)
        actions.move_to_element(input).click(input).send_keys("dadsadadasdasdas").perform()
        time.sleep(2)
        list = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='chosen-drop']/ul/li")))
        assert list.text == "No results match dadsadadasdasdas"

        self.driver.close()

    def test_action1_1_4(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        # login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("13553")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,
                                        "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        self.driver.switch_to.frame((self.driver.find_element(By.CLASS_NAME, "embed-responsive-item")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[1]/a"))).click()
        # check matching list(not done)
        time.sleep(1)

        input = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li/input")))
        actions = ActionChains(self.driver)
        actions.move_to_element(input).click(input).send_keys("test").perform()
        list_tag = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='chosen-drop']/ul/li")))
        list = ['0202_W test new tag 2 update', '0302 Annie Tags Test Updated', 'Annie test 2 updated', 'S Test Tag on Group 0214 Updated', 'S Test Tag on Group 0214_Test 2 updated', 'Test 4 updated 01/19']
        ar = []
        for i in list_tag:
            ar.append(i.text)

        assert ar == list
        self.driver.close()
    def test_action1_1_5(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("13553")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        self.driver.switch_to.frame((self.driver.find_element(By.CLASS_NAME, "embed-responsive-item")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[1]/a"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li/input"))).click()
        lists = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='chosen-drop']/ul/li")))
        for list in lists:
            if list.text == "Annie test 2 updated":
                list.click()
                break

        #check tag
        argb = self.driver.find_element(By.XPATH, "//li[@class='search-choice']").value_of_css_property("background-color")
        check_hex = Color.from_string(argb).hex
        assert check_hex, '#00B0F2'

        # click x remove
        tag = self.driver.find_element(By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li[1]")
        if tag.is_displayed():
            self.driver.find_element(By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li[1]/a").click()
            assert True
        else:
            raise ValueError("tag is still show")
        self.driver.quit()
    def test_action1_1_6(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("13553")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        self.driver.switch_to.frame((self.driver.find_element(By.CLASS_NAME, "embed-responsive-item")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[1]/a"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li/input"))).click()
        lists = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='chosen-drop']/ul/li")))
        for list in lists:
            if list.text == "Annie test 2 updated":
                list.click()
                break
        #check save correctly
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[2]/button"))).click()
        self.driver.switch_to.default_content()
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()
        self.driver.switch_to.frame((self.driver.find_element(By.CLASS_NAME, "embed-responsive-item")))
        #check txt shown corectly
        user = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[1]/span/span")))
        assert user.text == "ANNIE TEST 2 UPDATED"

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[1]/a"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ticket_tag_chosen']/ul/li[1]/a"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='r_ticket_view']/div[2]/div[3]/span/span/form/span[2]/button"))).click()
        self.driver.quit()

    def test_action1_1_7(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        #login user
        self.lp = Loginpage(self.driver)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]"))).click()
        time.sleep(2)
        self.lp.setUsername(self.username)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button/span"))).click()
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #process group
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ticketNumber']").send_keys("13553")
        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()

        #click x
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[1]/button"))).click()
        #check close
        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        assert modal == True

        time.sleep(4)
        menu = self.driver.find_element(By.XPATH, "//*[@role='table']/tbody/tr[1]/td[7]")
        edit = self.driver.find_element(By.XPATH,"//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/div[1]/button")
        ActionChains(self.driver).move_to_element(menu).click(edit).perform()
        #click cancel
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[1]/button"))).click()
        # check close
        modal = WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//*[@class='modal-content']")))
        assert modal == True

        self.driver.close()

