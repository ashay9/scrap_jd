import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.PhantomJS(r"C:\Python34\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs")
driver = webdriver.Firefox()
driver.get("http://www.justdial.com/Delhi-NCR/Garages-%3Cnear%3E-gurgaon/ct-253225")
continues_link=[]
time.sleep(10)


for i in range(500):
    bcard="bcard"+str(i)
    try:
        login_form=driver.find_element_by_id(bcard)
        login_form = login_form.find_element_by_xpath(".//span[@class='margin0']")
        #continue_link = driver.find_element_by_link_text(login_form.find_elements_by_xpath(".//a")[1].text)
    
        continue_link = login_form.find_element_by_link_text(login_form.find_elements_by_xpath(".//a")[1].text).get_attribute("href")
    except Exception as e:
        #pass
        print("danger!!!!!")
        #print(i)
        #continue_link = login_form.find_element_by_link_text(login_form.find_elements_by_xpath(".//a")[0].text).get_attribute("href")
    continues_link.append(continue_link)
    if i%10==0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(i)
        time.sleep(15)
        print(i)

with open(r"E:\salman\gurgaon\links_gurgaon.txt","w") as f:
    for i in continues_link:
        f.write(i+"\n")
