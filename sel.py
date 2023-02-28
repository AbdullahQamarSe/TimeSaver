from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# set up the proxy
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = '185.238.228.179:80'

# create a new Firefox driver with the proxy settings
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", proxy.http_proxy.split(':')[0])
profile.set_preference("network.proxy.http_port", int(proxy.http_proxy.split(':')[1]))
driver = webdriver.Firefox(firefox_profile=profile)

# navigate to a website to check the IP address
driver.get('https://www.whatismyip.com/')

# close the browser
driver.quit()
