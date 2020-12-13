from selenium import webdriver
import getpass


def create_user():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    username = input("Username: ")
    email = input("Email address: ")
    password = getpass.getpass()
    password_again = getpass.getpass()
    if username and password == password_again:
        web = webdriver.Chrome("chromedriver.exe")
        web.get("http://127.0.0.1:8000/accounts/signup/")
        web.find_element_by_xpath(
            '//*[@id="id_first_name"]').send_keys(first_name)
        web.find_element_by_xpath(
            '//*[@id="id_last_name"]').send_keys(last_name)
        web.find_element_by_xpath('//*[@id="id_username"]').send_keys(username)
        web.find_element_by_xpath('//*[@id="id_email"]').send_keys(email)
        web.find_element_by_xpath(
            '//*[@id="id_password1"]').send_keys(password)
        web.find_element_by_xpath(
            '//*[@id="id_password2"]').send_keys(password_again)
        web.find_element_by_xpath('/html/body/div/form/input[2]').click()
        web.close()


def login():
    username = input("Username: ")
    password = getpass.getpass()
    web = webdriver.Chrome("chromedriver.exe")
    web.get("http://127.0.0.1:8000/accounts/login/")
    web.find_element_by_xpath('//*[@id="id_username"]').send_keys(username)
    web.find_element_by_xpath('//*[@id="id_password"]').send_keys(password)
    web.find_element_by_xpath('/html/body/div/form/input[2]').click()
    web.close()


def like_aricle_1():
    web = webdriver.Chrome("chromedriver.exe")
    web.get("http://127.0.0.1:8000/")
    web.find_element_by_xpath('//*[@id="likearticle1"]').click()


def post_comment_on_article_1():
    comment = input("Comment: ")
    web = webdriver.Chrome("chromedriver.exe")
    web.get("http://127.0.0.1:8000/")
    web.find_element_by_xpath('//*[@id="commenttext1"]').send_keys(comment)
    web.find_element_by_xpath('//*[@id="comments"]/div/ul/li/input').click()
