# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-02

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 48 - Cookie Clicker

from selenium import webdriver

# Path for Selenium Chrome Driver
chrome_driver_path = "D:\\Users\\Marcelo\\Documents\\Code\\chromedriver.exe"

# Start Chrome Driver
driver = webdriver.Chrome(chrome_driver_path)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)


# Find number of English articles on Wikipedia
def find_number_of_articles(input_driver):
    article_count = driver.find_element_by_css_selector("#articlecount a")
    print(article_count.text)
    return driver


driver = find_number_of_articles(driver)

# Stop Chrome Driver
driver.quit()
