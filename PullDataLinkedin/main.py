from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

print("import okie")

#step 1 login
driver = webdriver.Chrome()
url = "https://www.linkedin.com/login"
driver.get(url)
sleep(2)

# credential = open("account_login.txt")
# line = credential.readlines()
# user_name = line[0]
# password = line[1]

# user_name_field = driver.find_element_by_id("username")
# user_name_field.send_keys(user_name)
# sleep(3)

# password_field = driver.find_element_by_id("password")
# password_field.send_keys(password)
# sleep(4)

# login_click = driver.find_ellement_by_xpath("//*[@id="organic-div"]/form/div[3]/button")
# login_click.click()
# sleep(4)

# # step 2 Search
# search_field = driver.find_ellement_by_xpath("//*[@id="global-nav-typeahead"]/input")
# search_query = input("What profile do you want to search?")
# search_field.send_keys(search_query)
# sleep(2)
# search_field.send_keys(Keys.RETURN)

# step 3

# def getURL():
#     page_source = BeautifulSoup(driver.page_source)
#     profiles = page_source.find_all("a", class_="app-aware-link")
#     all_profile_url = []
#     for profile in profiles:
#         profile_url = profile.get("href")
#         if profile_url not in all_profile_url:
#             all_profile_url,append(profile_url)
#     return all_profile_url

# def getPages():
#     input_page = int(input("How many pages you want to scrape: "))
#     url_all_page = []
#     for page in range(input_page):
#         url_one_page = getURL()
#         sleep(3)
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#         sleep(3)
#         next_button = driver.find_ellement_class_name("artdeco-pagination__button--next")
#         next_button.click()
#         url_all_page = url_all_page + url_one_page
#         sleep(3)
#     return url_all_page

# getPages()
