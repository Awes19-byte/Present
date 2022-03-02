from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#Loads chrome with default settings
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

#Gives path to chrome webdriver and loads classroom webpage
driver=webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Users\Awes\Downloads\geckodriver\chromedriver.exe')
driver.get('https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')

#Logs in the classroom
username=driver.find_element_by_id('identifierId')
username.click()
username.send_keys('oussama.mahfoudhi@isticbc.org')

next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
next.click()
time.sleep(2)
password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys('Your Password here')


next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
next.click()

time.sleep(15)
#Go to google meet
driver.find_element_by_xpath('//*[@id="gbwa"]/div').click()
time.sleep(15)
try:
	driver.find_element_by_class_name('tX9u1b').click()
except:
	print('error')
try:
	driver.find_element_by_class_name('CgwTDb').click()
except:
	print('error2')
driver.get('https://meet.google.com/?hs=197&pli=1&authuser=0')
time.sleep(5)
#write the link code
driver.find_element_by_xpath(
		'//*[@id="i3"]').send_keys('mzr-buji-adf')
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div/div[2]/button/span').click()
driver.implicitly_wait(10)

#turnmiccamoff
time.sleep(2)
driver.find_element_by_xpath(
		'//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
driver.implicitly_wait(3000)
time.sleep(1)
driver.find_element_by_xpath(
		'//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
driver.implicitly_wait(3000)
#join
time.sleep(5)
driver.implicitly_wait(2000)
driver.find_element_by_css_selector(
		'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
	# Ask to join and join now buttons have same xpaths
