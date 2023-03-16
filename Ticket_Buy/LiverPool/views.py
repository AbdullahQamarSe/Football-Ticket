from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from django.http import HttpResponse
import time
from LiverPool.models import TicketDetail




# Create your views here.

def Liver_pool(request):
    return render(request, 'index.html')

def Ticket_Selenium(request):
    from nordvpn_switcher import initialize_VPN, rotate_VPN, terminate_VPN
    import time

    settings = initialize_VPN()
    rotate_VPN(settings, location='Israel') # Rotate to a random location

    from selenium import webdriver
    xpath_list = [
    "/html/body/div[7]/div[2]/div/div[1]/div[2]/div[4]/div[2]/a",
    "/html/body/div[7]/div[2]/div/div[1]/div[3]/div[4]/div[2]/a",
    "/html/body/div[7]/div[2]/div/div[1]/div[4]/div[4]/div[2]/a",
    ]
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    if request.method == 'POST':
        my_data = request.POST.get('my-data')
        quantity = request.POST.get('Quantity')
        seats = int(quantity)

        driver = webdriver.Firefox()

        driver.get(my_data)
        try:
            # Close cookie popup if it appears
            time.sleep(5)
            popup_close_button = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            popup_close_button.click()
            time.sleep(5)
        except:
            pass
        
        # Iterate over the XPaths
        for i in range(1, 9):
            try:
                time.sleep(2)
                # Construct the current XPath
                xpath = f'/html/body/div[1]/div/div/div[2]/div/div/ul/li[{i}]/h3/span[2]/span'
                # Wait for the element to be visible
                try:
                    time.sleep(2)
                    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                except:
                    # If the element is not found, close the driver and exit
                    driver.quit()
                    break
                
                text = element.text.lower()
                time.sleep(2)
                
                # If the text is "Available", click on the element and exit the loop
                if text.lower() == 'available' or text.title() == 'Check Availability' :
                    time.sleep(10)
                    element.click()
                    try:
                        available = driver.find_elements(by=By.XPATH, value= f'/html/body/div[1]/div/div/div[2]/div/div/ul/li[{i}]/div/a')
                        time.sleep(5)
                        if available:
                            available[0].click()

                        Ticket = driver.find_elements(by=By.XPATH, value= f'/html/body/div[8]/div[2]/div[2]/div[4]/div/a')
                        if Ticket:
                            time.sleep(5)
                            Ticket[0].click()

                        time.sleep(15)
                        Xpat = driver.find_elements(by=By.XPATH, value='/html/body/div[7]/div[2]/div/div[1]/div[2]/div[4]/div[2]/a')
                        if Xpat:
                            
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
                            match_name = driver.title.split("|")[0].strip()
                            i=int(i)
                            i=2
                            # Get the match names from the xpaths
                            for xpath in xpaths:
                                
                                element = driver.find_element(by=By.XPATH, value=xpath)
                                text = element.text
                                text_words = text.split()
                                name_words = name1.split()
                                
                                # Check if the first word of each variable matches
                                if text_words[0].lower() == name_words[0].lower():
                                    element = driver.find_elements(by=By.XPATH, value=f'/html/body/div[7]/div[2]/div/div[1]/div{[i]}/div[4]/div[2]/a')
                                    element[0].click()
                                    i=i+1
                                    break
                                i=i+1
                        while seats > 0:
                            try:
                                time.sleep(6)
                                input_elem = driver.find_elements(by=By.XPATH, value='/html/body/div[8]/div/div[4]/div[1]/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[1]/label/span/input')
                                input_elem[0].clear()
                                input_elem[0].send_keys(str(seats))
                                
                                choose_btn = driver.find_elements(by=By.XPATH, value='/html/body/div[8]/div/div[4]/div[1]/div[3]/div[2]/div[2]/div/div[3]/div[1]/button[2]')
                                if choose_btn:
                                    time.sleep(5)
                                    choose_btn[0].click()
                                    break
                            except:
                                seats -= 1
                        time.sleep(5)
                        for i in range(1, seats+1):
                            xpath = f'/html/body/div[7]/div[2]/div[6]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[4]/div{[i]}'
                            data = driver.find_elements(by=By.XPATH, value=xpath)
                            if data:
                                savedata = data[0].text.replace("Remove", "").replace("Unknown", "")
                                ticket_detail = TicketDetail.objects.create(ticket=savedata)
                                ticket_detail.save()
                                name = driver.find_elements(by=By.XPATH, value="/html/body/div[7]/div[2]/div[6]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div[1]")
                                print(name1,savedata)
                                      

                    except Exception as e:
                        print(e)
                        break
                else:
                    continue
            except Exception as e:
                print(e)
                continue

        return render(request, 'index.html')

    return render(request, 'index.html') 