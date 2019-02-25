from selenium import webdriver

driver = webdriver.Chrome(executable_path='./driver/chromedriver')

url = input("URL: ")

if url:
    driver.get(url)

    expected_metas = ['description', 'keywords', 'robots', 'copyright', 'author', 'viewport', 'twitter:card',
                      'twitter:site',
                      'twitter:title', 'twitter:description', 'twitter:creator', 'twitter:image:src', 'og:title',
                      'og:type',
                      'og:url', 'og:image', 'og:description', 'og:site_name']

    exist_metas = []

    metas = driver.find_elements_by_xpath('//meta')

    for meta in metas:
        exist_metas.append(meta.get_attribute('name'))

    for m in expected_metas:
        if m not in exist_metas:
            print(m)
