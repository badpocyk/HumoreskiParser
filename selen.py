from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException
from time import sleep
import json

ChromeDriver = webdriver.Chrome()

login = "89109255012"
password = "ctyzuykjifhffrhfcfdxbr"
# main function

def main(log, passw):
    auth(log, passw)
    sleep(1)
    humoureski()
    sleep(1)
    k_zapisyam()
    sleep(1)
    sleep(1)
    printout()


# authentication

def auth(log,passw):
    ChromeDriver.get("https://www.vk.com/")
    setClickOnField_id("index_email")
    sleep(3)
    setTextInField("index_email", log)
    sleep(0.5)
    setClickOnField_id("index_pass")
    sleep(0.1)
    setTextInField("index_pass", passw)
    sleep(0.2)
    setClickOnField_id("index_login_button")
    sleep(0.7)



# go to group

def humoureski():
    setClickOnField_id("l_gr")
    sleep(0.5)
    setClickOnField_text("Мои любимые юморески")
    sleep(0.5)


# go to all posts

def k_zapisyam():
    for p in range(6):
        try:
            setClickOnField_text("Записи сообщества")
            break
        except WebDriverException:
            ChromeDriver.execute_script("window.scrollTo(0,document.body.scrollHeight*(0.1800067));")
    sleep(0.3)


# number of posts

def number_of_posts():
    count_of_posts = ChromeDriver.find_element_by_id("fw_summary")
    count_of_posts = count_of_posts.text
    count_of_posts = count_of_posts.replace(' ', '')
    count_of_posts = int(count_of_posts)


def scroll():
    for i in range(5):
        sleep(0.2)
        ChromeDriver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

def printout():
    dictionary = {}
    num = 0

    jons = open('jons.json', 'w', encoding='utf-8')
    scroll()
    show_full()
    sleep(1)
    spisok = ChromeDriver.find_elements_by_class_name("wall_post_text")
    show_full()
    sleep(1)
    for i in spisok:
        dictionary[num] = i.text
        print(i.text)
        print('\n')
        print('----------------------------------------------------------------------------')
        num += 1
    sleep(2)
    json.dump(dictionary, jons, separators=(',', ': '), ensure_ascii=False)
    jons.close()


def show_full():
    try:
        findElementsByClass("wall_post_more")
    except:
        return 0

def setTextInField(id_elem, text):
    elem = ChromeDriver.find_element_by_id(id_elem)
    for i in text:
        elem.send_keys(i)
        sleep(0.1)

def setClickOnField_id(id_elem):
    elem = ChromeDriver.find_element_by_id(id_elem)
    elem.click()

def setClickOnField_class(id_elem):
    elem = ChromeDriver.find_element_by_class_name(id_elem)
    elem.click()

def setClickOnField_text(name):
    elem = ChromeDriver.find_element_by_link_text(name)
    elem.click()

def findElementsByClass(clas):
    elem = ChromeDriver.find_elements_by_class_name(clas)
    for i in elem:
        i.click()
        sleep(1)

main(login,password)