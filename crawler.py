from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')

url = 'https://mops.twse.com.tw/mops/web/index'
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get(url)

time.sleep(2)

driver.find_element_by_xpath("//*[@id='table02']/form[1]/table/tbody/tr/td/font/input[4]").send_keys(Keys.SPACE)

while True:
    num_rows = len(driver.find_elements_by_xpath("//*[@id='tab2']/tr"))
    num_cols = len(driver.find_elements_by_xpath("//*[@id='tab2']/tr[1]/td"))

    before_XPath = "//*[@id='tab2']/tr["
    aftertd_XPath = "]/td["
    aftertr_XPath = "]"

    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            FinalXPath = before_XPath + str(i+1) + aftertd_XPath + str(j+1) + aftertr_XPath
            cell_text = driver.find_element_by_xpath(FinalXPath).text
            if cell_text == "6645":
                #Do something
                print("散戶要來啦！！！")
            row.append(cell_text)
        print(row)
    
    time.sleep(20)
