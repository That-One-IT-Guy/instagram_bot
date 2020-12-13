from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('test')
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
tryn = 0

driver = webdriver.Chrome(executable_path='C:/Users/thech/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://www.instagram.com/direct/inbox/')
print(driver.title)
print(driver.current_url)
time.sleep(1)
id_box = driver.find_element_by_name('username')
id_box.send_keys('USERNAME HERE')
id_box = driver.find_element_by_name('password')
id_box.send_keys('PASSWORD HERE')
login_button = driver.find_elements_by_xpath("//*[contains(text(), 'Log In')]")
for btn in login_button:
    btn.click()
time.sleep(4)
userinfostate = driver.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
for btn in userinfostate:
    btn.click()
time.sleep(2)
try:
    noteoff = driver.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
    for btn in noteoff:
        btn.click()
        print("Exeption used!")
except:
    print("Exeption not used.")
print("UPDATE VERSION: 12/13/2020")
print("Logged in!")
input = input("Press enter to start loop.")
while True:
    try:
        #get to 1st user
        el=driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[2]')[0]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(el, 200,100)
        action.click()
        action.perform()
        time.sleep(1)
        dl=driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]')[0]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(dl, 0, 0)
        action.click()
        action.perform()
        #get text
        for element in driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/span'):
           textfu = element.text
        #get response
        outtext = chatbot.get_response(textfu)
        #send text
        dl=driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')[0]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(dl, 5, 5)
        action.click()
        action.perform()
        actions = ActionChains(driver)
        actions.send_keys(str(outtext))
        actions.send_keys(Keys.RETURN)
        actions.perform()
        #del conversation
        dl=driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button')[0]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(dl, 0, 0)
        action.click()
        action.perform()
        dl=driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button')[0]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(dl, 0, 0)
        action.click()
        action.perform()
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        driver.refresh()
        tryn = 0
    except:
        time.sleep(1)
        tryn = tryn + 1
        if tryn == 120:
            driver.refresh()
            tryn = 0


time.sleep(9999)
driver.close()
