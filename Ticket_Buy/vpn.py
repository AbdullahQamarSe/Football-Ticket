from selenium import webdriver

# create a new instance of the web driver


# define the number of iterations for the loop
num_iterations = 3

# loop through the iterations and navigate to the URL
try:
    for i in range(num_iterations):
        driver_name = f"driver{i}"
        globals()[driver_name] = webdriver.Firefox()
        

        globals()[driver_name].get('https://www.google.com')

except Exception as e:
    print(e)
    


