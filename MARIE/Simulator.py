from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
import time
from MARIE.AssemblerError import MemoryLimitException as MLE
class Simulator():
    '''simulate MARIE_OBJECT using MARIE.js site and automation'''
    url="https://marie.js.org/"
    def __init__(self):
        '''start webdriver and hold it ready'''
        edge_options = Options()
        edge_options.add_experimental_option("detach", True)
        self.driver=webdriver.Edge(options=edge_options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.close_pop_ups()
        self.driver.find_element(By.ID, "assemble").click()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "memory-headers")))
        print('Simulator is ready')
    def close_pop_ups(self):
        try:
            element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//button[@data-role='end']")))
            element.click()
        except:
            pass
        try:
            element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "submitToU")))
            element.click()
        except:
            pass
    def write_to_memory(self,data):
        '''write to the memory of simulation'''
        memory=self.driver.find_element(By.XPATH,"//table[@id='memory']")
        #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        ptr=0
        end=len(data)
        rows=memory.find_elements(By.TAG_NAME,'tr')
        for row in rows:
            self.driver.execute_script("arguments[0].scrollIntoView();", row)
            cells=row.find_elements(By.TAG_NAME,'td')
            for cell in cells:
                #time.sleep(0.1)
                if ptr==end:
                    return
                #cell.clear()
                #cell.click()
                #cell.send_keys(data[ptr])
                self.driver.execute_script(f'arguments[0].innerHTML="{data[ptr]}"', cell)
                action = ActionChains(self.driver)
                action.double_click(on_element = cell)
                action.perform()
                ptr+=1
        #if ptr!=end ,memory limit exceeded
        if ptr!=end:
            raise MLE(f"Insufficient memory to store instructions, {end-ptr} remains..")
    def quit(self):
        self.driver.quit()


