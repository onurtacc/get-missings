from selenium import webdriver

url = input("URL: ")

if url:
    driver = webdriver.Chrome(executable_path='./driver/chromedriver')
    driver.get(url)

    expected_metas = ['description', 'keywords', 'robots', 'copyright', 'author', 'viewport', 'twitter:card',
                      'twitter:site',
                      'twitter:title', 'twitter:description', 'twitter:creator', 'twitter:image:src', 'og:title',
                      'og:type',
                      'og:url', 'og:image', 'og:description', 'og:site_name']

    exist_metas = []

    metas = driver.find_elements_by_xpath('//meta')

    for meta in metas:
        meta_name = meta.get_attribute('name')
        meta_property = meta.get_attribute('property')
        meta_itemprop = meta.get_attribute('itemprop')
        if meta_name:
            exist_metas.append(meta_name)
        elif meta_property:
            exist_metas.append(meta_property)
        elif meta_itemprop:
            exist_metas.append(meta_itemprop)

    for m in expected_metas:
        if m not in exist_metas:
            print(m)
