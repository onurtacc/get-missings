from selenium import webdriver

driver = webdriver.Chrome(executable_path='./driver/chromedriver')

url = input("URL: ")

if url:
    driver.get(url)

    img_tags = driver.find_elements_by_xpath('//img')

    for img in img_tags:
        if img.get_attribute('title') == '':
            print(img.get_attribute('src') + ' ' + '- Missing Title')

    for img in img_tags:
        if img.get_attribute('alt'):
            print(img.get_attribute('src') + ' ' + '- Missing Alt')
