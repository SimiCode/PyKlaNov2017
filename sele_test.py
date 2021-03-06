from pyvirtualdisplay import Display
from selenium import webdriver

with Display():
    # we can now start Firefox and it will run inside the virtual display
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(chrome_options=options)

    # put the rest of our selenium code in a try/finally
    # to make sure we always clean up at the end
    try:
        browser.get('https://www.pythonanywhere.com')
        print(browser.title) #this should print "Google"

    finally:
        browser.quit()
