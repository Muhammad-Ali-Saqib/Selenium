from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set the inputs
chromeDriverPath = 'chromedriver-linux64/chromedriver'
URL = 'https://pencilsketch.imageonline.co/#google_vignette'
imagePath = '/media/muhammad/Projects1/web_automation/img_1.jpeg'
downloadPath = '/media/muhammad/Projects1/web_automation/'

# setting browser configurations
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": downloadPath
})

# setting the browser to open
driver = webdriver.Chrome(chromeDriverPath, chrome_options=chrome_options)

# go to the url
driver.get(URL)

# upload image 
uploadButton = driver.find_element_by_class_name('btn') # not clicking jsut passing the path of image

# giving the path of image
uploadButton.send_keys(imagePath)

# wait for upload
time.sleep(5)

# Performing sketch
pencilButton = driver.find_element_by_id('convert').click()

# wait for conversion
time.sleep(5)

# downloading resultant image
downloadButton = driver.find_element_by_class_name('btn-success').click()

# wait for download to begin
time.sleep(5)

# close tab
driver.close()

# close window
driver.quit()