# Selenium Tutorial

- To Install Selenium
> $ pip install selenium

This Python library wraps the Selenium WebDriver and provides methods for automating a range of tasks like filling up the form, logging into a website, clicking on buttons, and more.

- Import the Selenium library
  > from selenium import webdriver

- Driver Initialization with Python

By Python to start the Selenium WebDriver and browser driver.

>`# Initialize Chrome WebDriver`
> 
>driver = webdriver.Chrome()

>`# Initialize Firefox/Gecko WebDriver`
> 
>driver = webdriver.Firefox()
> 
>`# Initialize Safari WebDriver`
> 
>driver = webdriver.Safari()

>`# Initialize IE WebDriver`
> 
>driver = webdriver.Ie()



In case the location of the browser driver is not added to the PATH variable (or if it is not in the System Path), you need to add the following arguments:

-	executable_path: Path to your Selenium WebDriver (binary file)
-	options: Options regarding the web browsers execution

Example:
>driver=webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options )

- Setting Options in Selenium WebDriver

The Options class in Selenium Python is commonly used in conjunction with Desired Capabilities to customize Selenium WebDriver.
It helps to perform various operations like opening the browser in maximized mode, enabling and disabling browser extensions, disabling GPU mode, disabling pop-ups, and more. 
>`#Importing Chrome options`
> 
>from selenium import webdriver
>from selenium.webdriver.chrome.options import Options

>`#Initialization of Chrome options`
> 
>chrome_options = Options()

>`#Adding Desired Capabilities`
> 
>chrome_options.add_argument("--disable-extensions")

>`#Adding Desired Capabilities to a session`
> 
>driver = webdriver.Chrome(chrome_options=chrome_options)

- Finding an element

Locators in Selenium are majorly used for locating WebElements present in the DOM. Appropriate interactions (or actions) are further performed on the located WebElements. Some popular Selenium web locators are ID, Name, Link Text, Partial Link Text, CSS Selectors, XPath, TagName, etc.
Locate Elements by the ID attribute
In this method, the element in the DOM is searched using the ID attribute. ID is unique for every element on the page.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com")
email_form = driver.find_element_by_id("testing_form")
Locate Elements by CSS Class
Elements in HTML DOM can also be searched by Class Name, which is stored in the Class attribute of an HTML tag. A class can have many instances; it returns the first element with a matching class.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com")
first_form_input = driver.find_element_by_class_name(" form-control ")
Locate Elements by Name
WebElements like input tag have a Name attribute associated with them. Selenium also provides a method to search for WebElements using the NAME attribute. If there are multiple elements of the same name, the first matched element is returned by the method.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com")
# for selection input with name attribute "name"
name_input = driver.find_element_by_name("name")
Locate Elements by XPath
XPath uses path expressions to select nodes and locate the required WebElement.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com")
email_input = driver.find_element_by_xpath("//input[@name='email']")
Locate Element by tag name
This method is used to locate and select WebElements using the HTML tag name(H1, DIV, INPUT, etc.). If there are multiple occurrences of the same tag, it returns the first matching tag. 
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com")
email_input = driver.find_element_by_tag_name("input")
Locate Element by Link text or Partial Link Text
It selects elements based on the link text (either complete link text or partial link text). Partial link text does not look for an exact match of the string value since it looks for a string subset (in the link text). 
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com")
email_input = driver.find_element_by_link_text('Start Free Testing')
email_input1 = driver.find_element_by_partial_link_text('Start Free')
5. Misc methods for finding elements
Two private methods might be useful for locating page elements in conjunction with the “By” class for selecting attributes.
It is to be noted that there is no difference between find_element_by_tag method and find_element(By.tag) method. By default, find_element_by_tag calls the find_element(By.tag) method.
•	find_element – It returns the first instance from multiple web elements with a particular attribute in the DOM. The method throws NoSuchElementException if no web elements are matching the required web locator. 
•	find_elements – It returns a list of all the instances of WebElements matching a particular attribute. The list is empty in case there are no matching elements in the DOM.
Here are the attributes available for the By class:
ID = “id”
XPATH = “xpath”
NAME = “name”
TAG_NAME = “tag name”
CLASS_NAME = “class name”
LINK_TEXT = “link text”
PARTIAL_LINK_TEXT = “partial link text”
Example:
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//input[name()="password"]')
driver.find_elements(By.XPATH, '//input')
6. Opening a URL (or document)
driver.get(URL)
The driver.get() method navigates to the page that is passed as a parameter to the method. Selenium WebDriver will wait until the page has fully loaded, post which it fires an “onload” event before returning control to the test script. 
driver.get("https://www.lambdatest.com")
7. Refresh a page
There are scenarios where you would want to refresh the contents on the page. 
driver.refresh()
8. Writing text inside a WebElement
The send_keys() method in Python is used for entering text inside a text element. 
# get element 
element = driver.find_element_by_id("useremail")  
# send keys 
element.send_keys("emailid@lambdatest.com")
9. Clearing text of a WebElement
The element.clear() method in Selenium Python is used to clear text from fields like input fields of a form.
# get element 
element = driver.find_element_by_id("useremail")  
# send keys 
element.clear()
10. Clicking a WebElement
The element.click() method in Selenium Python is used to click on an element like anchor tag, button tag, etc.
# get element 
button_element = driver.find_element_by_link_text("Start Free Testing")  
# click the element
button_element.click()
11. Dragging and Dropping a WebElement
The drag_and_drop(element, target) method in Selenium Python helps in automating the functionality of dragging WebElements from the source and dropping them on target area (or element).
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")
from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
12. Selecting an option
Select(element) provides useful methods for interacting with drop-downs, selecting elements, and more.
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_id('city'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
select.deselect_all()

13. Navigating between windows
If there are multiple windows, you might need to switch to the right window before performing actions on the WebElements present in the DOM.
driver.switch_to_window(“window_name”)
The switch_to_window() method of Selenium WebDriver lets you switch to the desired window. The window handle is passed as an argument to the switch_to_window() method. 
driver.switch_to_window("window_handle")
All the subsequent calls of the WebDriver are now applicable to the window under focus (or the newly switched window).
driver.window_handles
Window_handles property of the WebDriver returns handles of the windows. You can now use the switch_to_window() method to navigate to each window available in the list of window_handles. 
for handle in driver.window_handles:
    driver.switch_to_window(handle)
driver.current_window_handle
The current_window_handle() method returns the handle of the current window (or window currently under focus) 
handler = driver.current_window_handle 
14. Switching to iFrames
Selenium WebDriver can not access or locate the web elements inside an iFrame in the context of the main web page. Hence, you need to switch to an iFrame before accessing the WebElements inside the iframe.
driver.switch_to_frame(“frame_name”)
The switch_to_frame() method in Selenium Python lets you switch the context of WebDriver from the context of the main page. We can also access subframes by separating the path and index with a dot. 
driver.switch_to_frame("frame_name.0.child")
driver.switch_to_default_content()
This method allows you to switch back to the context of the main page. 
driver.switch_to_default_content()
15. Handling pop-ups and alerts
There are three main types of popups & alerts that are commonly used in web applications:
•	Simple Alert
•	Confirmation Alert
•	Prompt Alert
You have the option to switch to the alert, dismiss the alert, or accept the alert. 
driver.switch_to.alert
The switch_to.alert property of WebDriver returns the currently open alert object. You can use the object to accept, dismiss, read its contents, or type into the prompt. 
alert_obj = driver.switch_to.alert
alert_obj.accept()
Once you have the handle of the alert window (e.g. alert_obj), the accept() method is used to accept the Alert popup. 
alert_obj = driver.switch_to.alert 
alert_obj.accept()
alert_obj.dismiss()
Once you have switched to the alert window (e.g. alert_obj), you can use the dismiss() method to cancel the Alert popup. 
alert_obj = driver.switch_to.alert 
alert_obj.dismiss()
alert_obj.text()
This method is used to retrieve the message included in the Alert popup. 
alert_obj = driver.switch_to.alert 
msg = alert_obj.text()
print(msg)
16. Getting Page Source
The page_source() method in Selenium WebDriver is used to get the target document’s page source (or test page). 
page_source = driver.page_source
17. Navigating browser history
Selenium WebDriver in Python provides some functionalities to move backward and forward in the web browser’s history
driver.forward()
This method allows scripts to navigate one step forward in history. 
driver.forward()
driver.back()
This method allows scripts to navigate one step backward in history. 
driver.back()
18. Handling Cookies in Selenium
Handling cookies in Selenium WebDriver is one of the common scenarios that you might have to deal with in Selenium web automation. You can perform various operations like add, remove, get cookie name, and more.
driver.add_cookie()
This method helps to set a cookie to a Selenium session. It accepts values in the key-value pair. 
# Go to the domain
driver.get("https://www.lambdatest.com/")
# Now set the cookie. 
cookie = {'name' : 'user', 'value' : 'vinayak'}
driver.add_cookie(cookie)
driver.get_cookies()
This method outputs all the available cookies for the current Selenium session. 
# Go to the domain
driver.get("https://www.lambdatest.com/")
driver.get_cookies()
driver.delete_cookie()
There is an option to delete a specific cookie or all the cookies associated with the current Selenium session. 
# delete one cookie
driver.delete_cookie(cookie)
# delete all cookies
driver.delete_all_cookies()
19. Setting Window Size
The set_window_size() method is used to set the browser window’s size to desired dimensions (in height and width). 
# Setting the window size to 1200 * 800
driver.set_window_size(1200, 800)
20. Configuring TimeOuts in Selenium WebDriver
When the browser loads a page, the WebElements inside the page may load at various time intervals. This might create complications when interacting with the dynamic elements present on the page.
If an element is not present in the DOM of the web page, the locate method will raise an exception. Waits in Selenium lets you add delays (in ms or seconds) between the actions performed between loading the page and locating the required WebElement.
Implicit wait and Explicit wait are the two major ways you can add delays in Selenium Python code for handling dynamic WebElements on the page.
Implicit Wait in Selenium Python
An implicit wait informs the Selenium WebDriver to examine the DOM for a particular amount of time when trying to find the WebElement that is not immediately available for access.
By default, implicit wait is set as zero. However, once we define implicit wait, it is set for the lifetime of the WebDriver object. 
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10) # in seconds
driver.get("https://www.lambdatest.com/")
element = driver.find_element_by_id("testing_form")
Explicit Wait in Selenium Python
Explicit wait in Selenium Python is used when we want to wait for a particular condition to happen before proceeding further in the code.
There are some convenient methods provided by the Selenium WebDriver that let you wait until a particular condition is satisfied. For example, explicit waits can be achieved using the webdriverWait class combined with Expected Conditions in Selenium.
Here are some of the Expected Conditions that can be used in conjunction with Explicit wait in Selenium Python:
•	presence_of_all_elements_located
•	text_to_be_present_in_element
•	text_to_be_present_in_element_value
•	frame_to_be_available_and_switch_to_it
•	invisibility_of_element_located
•	title_is
•	title_contains
•	presence_of_element_located
•	visibility_of_element_located
•	visibility_of
•	element_located_selection_state_to_be
•	alert_is_present
•	element_to_be_clickable
•	staleness_of
•	element_to_be_selected
•	element_located_to_be_selected
•	Element_selection_state_to_be
Shown below is an example that demonstrates the usage of explicit wait where a non-blocking wait of 10 seconds is performed until the required WebElement is located (using its ID attribute): 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "testing_form"))
    )
except:
    print(“some error happen !!”)
21. Capturing Screenshots
During the process of Selenium web automation, you might want to capture the screenshot of the entire page or screenshot of a particular WebElement.
capture_path = 'C:/capture/your_desired_filename.png'
driver.save_screenshot(capture_path)


