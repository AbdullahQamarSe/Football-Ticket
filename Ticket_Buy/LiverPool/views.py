from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from django.http import HttpResponse
import time
from LiverPool.models import TicketDetail
from .models import sel
from selenium.webdriver.firefox.options import Options
from datetime import datetime


# Create your views here.

def Liver_pool(request):
    return render(request, 'index.html')


def Ticket_Selenium(request):
    driver_list = []
    if request.method == 'POST':
        my_data = request.POST.get('my-data')
        action = request.POST.get('action')
        dri=0
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        if action == 'start':   
            sel.objects.update(Selnium=1)
            from selenium import webdriver
            from selenium.webdriver.firefox.options import Options

            while sel.objects.get(pk=1).Selnium == "1":
                try:
                    
                    firefox_options = Options()
                    driver_name = f"driver{dri}"
                    
                    globals()[driver_name] = webdriver.Firefox(options=firefox_options)

                    current_time = datetime.now()

                    formatted_time = current_time.strftime("%A, %B %d, %Y %I:%M:%S %p")
                    print(formatted_time + " : Start bot")

                    xpath_list = [
                    "/html/body/div[7]/div[2]/div/div[1]/div[2]/div[4]/div[2]/a",
                    "/html/body/div[7]/div[2]/div/div[1]/div[3]/div[4]/div[2]/a",
                    "/html/body/div[7]/div[2]/div/div[1]/div[4]/div[4]/div[2]/a",
                    ]

                    
                    
                    if request.method == 'POST':
                        my_data = request.POST.get('my-data')

                        globals()[driver_name].minimize_window()
                        globals()[driver_name].get(my_data)

                            # Close cookie popup if it appears
                        time.sleep(5)
                        popup_close_button = globals()[driver_name].find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')      
                        popup_close_button.click()
                        time.sleep(5)

                        

                        # Iterate over the XPaths
                        for i in range(1, 9):
                            try:
                                time.sleep(2)
                                # Construct the current XPath
                                xpath = f'/html/body/div[1]/div/div/div[2]/div/div/ul/li[{i}]/h3/span[2]/span'
                                # Wait for the element to be visible
                                try:
                                    time.sleep(2)
                                    element = WebDriverWait(globals()[driver_name], 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                                except:
                                    # If the element is not found, close the driver and exit
                                    globals()[driver_name]
                                    break
                                
                                text = element.text.lower()
                                time.sleep(2)
                                
                                # If the text is "Available", click on the element and exit the loop
                                if text.lower() == 'available' or text.title() == 'Check Availability' :
                                    time.sleep(10)
                                    element.click()
                                    try:

                                        
      

                                        available = globals()[driver_name].find_elements(by=By.XPATH, value= f'/html/body/div[1]/div/div/div[2]/div/div/ul/li[{i}]/div/a')
                                        time.sleep(5)
                                        if available:
                                            available[0].click()
                                            
                                            print(formatted_time + " : Reached ticket page")


                                        from selenium.webdriver.support.ui import WebDriverWait
                                        from selenium.webdriver.support import expected_conditions as EC
                                        from selenium.webdriver.common.by import By
                                        from twocaptcha import TwoCaptcha

                                        # create a WebDriverWait instance with a timeout of 10 seconds
                                        wait = WebDriverWait(globals()[driver_name], 20)
                                        time.sleep(10)
                                        # wait for the captcha elements to appear on the page
                                        captcha_elements = globals()[driver_name].find_elements(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/b/div/div/div/div/div[1]/div/fieldset/div[1]/img')
                                        if captcha_elements:
                                            print("Captcha detected")

                                            # extract the captcha image source URL
                                            captcha_img = globals()[driver_name].find_element(by=By.XPATH,value='/html/body/div[2]/div[2]/div[3]/div/b/div/div/div/div/div[1]/div/fieldset/div[1]/img')
                                            captcha_src = captcha_img.get_attribute('src')

                                            # solve the captcha using 2captcha API
                                            api_key = "3608f5e5012070ab8e5d1209dca111d6"
                                            solver = TwoCaptcha(api_key)

                                            try:
                                                result = solver.normal(captcha_src)
                                                print(result)
                                                code = result['code']

                                                # enter the captcha code into the input field
                                                scaptha = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/b/div/div/div/div/div[1]/div/fieldset/div[2]/div[2]/input')))
                                                scaptha.send_keys(code)

                                                # click the submit button
                                                scaptha1 = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/b/div/div/div/div/div[1]/button')))
                                                scaptha1.click()

                                            except Exception as e:
                                                print("Captcha Error:", e)


                                        Ticket = globals()[driver_name].find_elements(by=By.XPATH, value= f'/html/body/div[8]/div[2]/div[2]/div[4]/div/a')
                                        if Ticket:
                                            time.sleep(5)
                                            Ticket[0].click()
                                            print(formatted_time + " : Chose ticket and seats")

                                        time.sleep(15)
                                        Xpat = globals()[driver_name].find_elements(by=By.XPATH, value='/html/body/div[7]/div[2]/div/div[1]/div[2]/div[4]/div[2]/a')
                                        if Xpat:
                                            print(formatted_time + " : Chose ticket and seats")
                                            xpaths = [
                                                "/html/body/div[7]/div[2]/div/div[1]/div[2]/div[1]/span",
                                                "/html/body/div[7]/div[2]/div/div[1]/div[3]/div[1]/span",
                                                "/html/body/div[7]/div[2]/div/div[1]/div[4]/div[1]/span"
                                            ]
                                            from selenium import webdriver
                                            from selenium.webdriver.common.keys import Keys
                                            from bs4 import BeautifulSoup
                                            from urllib.parse import urlparse
                                            import os.path
                                            # Get the link from a form input
                                            link = my_data

                                            parsed_link = urlparse(link)

                                            # Get the name from the last path component
                                            name = os.path.splitext(os.path.basename(parsed_link.path))[0]

                                            # Replace hyphens with spaces
                                            name1 = name.replace("-", " ")


                                            # Get the match name from the page title
                                            match_name = globals()[driver_name].title.split("|")[0].strip()
                                            i=int(i)
                                            i=2
                                            # Get the match names from the xpaths
                                            for xpath in xpaths:
                                                
                                                element = globals()[driver_name].find_element(by=By.XPATH, value=xpath)
                                                text = element.text
                                                text_words = text.split()
                                                name_words = name1.split()
                                                
                                                # Check if the first word of each variable matches
                                                if text_words[0].lower() == name_words[0].lower():
                                                    element = globals()[driver_name].find_elements(by=By.XPATH, value=f'/html/body/div[7]/div[2]/div/div[1]/div{[i]}/div[4]/div[2]/a')
                                                    element[0].click()
                                                    i=i+1
                                                    break
                                                i=i+1
                                        seats=4  

                                        while seats > 0:

                                            try:
                                                input_elem = globals()[driver_name].find_elements(by=By.XPATH, value='/html/body/div[8]/div/div[4]/div[1]/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[1]/label/span/input')
                                                input_elem[0].clear()
                                                input_elem[0].send_keys(str(seats))
                                                
                                                choose_btn = globals()[driver_name].find_elements(by=By.XPATH, value='/html/body/div[8]/div/div[4]/div[1]/div[3]/div[2]/div[2]/div/div[3]/div[1]/button[2]')
                                                if choose_btn:
                                                    choose_btn[0].click()
                                                    firefox_options.headless = False
                                                    break
                                            except:
                                                seats -= 5
                                        time.sleep(5)
                                        print(formatted_time + " : Tickets added to cart")

                                        
                                        

                                        for i in range(1, seats+1):
                                            
                                            xpath = f'/html/body/div[7]/div[2]/div[6]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[4]/div{[i]}'
                                            data = globals()[driver_name].find_elements(by=By.XPATH, value=xpath)
                                            if data:
                                                savedata = data[0].text.replace("Remove", "").replace("Unknown", "")
                                                ticket_detail = TicketDetail.objects.create(ticket=savedata)
                                                ticket_detail.save()
                                                name = globals()[driver_name].find_elements(by=By.XPATH, value="/html/body/div[7]/div[2]/div[6]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[1]")
                                                globals()[driver_name].maximize_window()
                                                print(" : Ticket information: " , name1,savedata)
                                                dri = dri+1;
 
                                    except Exception as e:
                                        print(e)
                                        continue
                            except Exception as e:
                                print(e)
                                continue
                except Exception as e:
                    print(e)
                    continue
    return render(request, 'index.html')



def Stop_pool(request):
    if request.method == 'POST':
        my_data = request.POST.get('my-data')
        action = request.POST.get('action')
        if action == 'stop':
                sel.objects.update(Selnium=2)
                return render(request, 'stop.html')
    return render(request, 'stop.html')
