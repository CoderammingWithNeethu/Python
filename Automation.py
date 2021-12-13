from selenium import webdriver
driver = webdriver.Chrome()
#Either set PATH else, ChromeDrive should be in same path as that of the script
'''
FireFox Webdriver name is Gecko
'''
driver.get('https://www.youtube.com/')
#copy xpath of serach box : //*[@id="search"]
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Python Tutorials')
#search button xpath : //*[@id="search-icon-legacy"]
searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()

