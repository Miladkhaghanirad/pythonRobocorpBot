from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import FileSystem
import time
from RPA.HTTP import HTTP
import subprocess
import winsound
import psutil
from datetime import datetime
import winreg
from robocorp import tasks
import colorama
from colorama import Fore, Style
import configparser
import logging
from pushbullet import Pushbullet




# get device id of running machine
def get_device_id():
    device_id=""
    key_path = r"SOFTWARE\Microsoft\SQMClient"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,key_path) as key:
            device_id, _ = winreg.QueryValueEx(key,"MachineId")
            
        return device_id    
    except:
        print("not working")
        return None

name = "Exequiel Michael Alain"
def send_notification(title, body, name):
        # Pushbullet API key
    api_key = "o.mFcc9VCQIwF0M1UKQQ8Y0d8SAiXuKTAO"
    pb = Pushbullet(api_key)
    push = pb.push_note(title, body+" for : "+ name)

def setup_logging():
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the root logger level to the lowest (DEBUG)

    # Create a console handler that displays log messages on the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Log messages with INFO level or higher to the console

    # Create a formatter to specify how log messages should be formatted
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)

def disable_logging():
    # Create a logger
    print("disable logging")
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)  # Set the logger to the highest level (CRITICAL)

def appointment_sound():
    winsound.Beep(500, 1000)
    time.sleep(5)
    winsound.Beep(500, 1000)
    time.sleep(5)
    winsound.Beep(500, 1000)

def stop_sound():
    winsound.Beep(500, 500)
    time.sleep(1)
    winsound.Beep(500, 2000)  

# print welcome page
def print_welcome_page():
    # Set text color to blue
    colorama.init()
   
                                                         
                                                         
    # Print "ITWay" text with an icon
    print(Fore.BLUE + Style.BRIGHT + "ITWay" + Fore.RESET + "\t\t\t")
    lines = [
        " ___  _________  ___       __   ________      ___    ___ ",
        "|\  \|\___   ___\\  \     |\  \|\   __  \    |\  \  /  /|",
        "\ \  \|___ \  \_\ \  \    \ \  \ \  \|\  \   \ \  \/  / /",
        " \ \  \   \ \  \ \ \  \  __\ \  \ \   __  \   \ \    / /",
        "  \ \  \   \ \  \ \ \  \|\__\_\  \ \  \ \  \   \/  /  /",
        "   \ \__\   \ \__\ \ \____________\ \__\ \__\__/  / /",
        "    \|__|    \|__|  \|____________|\|__|\|__|\___/ /",
        "                                            \|___|/"
    ]

    for line in lines:
        print(line)

    # Print company name
    print(Fore.CYAN + Style.BRIGHT + "\n\t\t\t\tWelcome to ITWay!\n")

    # Print company motto
    print(Fore.WHITE + "\t\t\tYour BOT for  your appointment needs.\n")
    print("Hello " + name)

def test_sound():
    while True:
        print("1 - play appointment sound")
        print("2 - play bot stop sound")
        print("3 - start the bot\n")

        choice = input("choose 1, 2, 3 or close the program : ")

        if(choice == "1"):
            # call appointment sound
            print("now you should hear 3 beep with 5 second delay between.this is the sound that will play, when appointment is available")
            appointment_sound()
            answer = input("Did you hear the sounds?(y/n)")
            if (answer== "y"):
                print("Great .Now you can start the bot.before that you cab change ignore_test_page value to 'True' in file Config.ini .")
            if ( answer == "n"):
                print("Please contact us in telegram: https://t.me/MimMarouf ")
        if(choice == "2"):
            # call stop sound
            print("now you should hear 1 beep sound with 1 second duration and another sound with 2 second duration.this is the sound that will play, when bot stop working")
            stop_sound()
            answer = input("Did you hear the sounds?(y/n)")
            if (answer== "y"):
                print("Great .Now you can start the bot.before that you cab change ignore_test_page value to 'True' in file Config.ini .")
            if ( answer == "n"):
                print("Please contact us in telegram: https://t.me/MimMarouf ")
        if(choice == "3"):
            break

def init(chrome_executable):
    print ("please be aware that this program work just on one Machine and just for getting appointment for : " + name + "\n")
    print (" If you use it for others, we will deactive your bot remotly. \n")
    # kill chrome process before start
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_info = process.info
            if process_info['name'] == 'chrome.exe':
                psutil.Process(process_info['pid']).terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


    # chrome prot
    chrome_debug_port = 9222
    # Start a headless Chrome instance with the debugging port
    chrome_options = [
        "--headless",
        f"--remote-debugging-port={chrome_debug_port}"
    ]
    # start chrome as process 
    proc = subprocess.Popen([chrome_executable, f"--remote-debugging-port={chrome_debug_port}"])

browser=Selenium()
# start navigate to page of select page
def start_navigate():
    logging.info("\nStart navigate....")
    browser.set_selenium_implicit_wait(30)
    browser.attach_chrome_browser(9222)
    browser.go_to("https://otv.verwalt-berlin.de/")
    load_page()
    browser.reload_page()
    load_page()
    browser.set_selenium_implicit_wait(30)
    browser.wait_until_element_is_visible('//*[@id="mainForm"]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/a',30)
    browser.click_element('//*[@id="mainForm"]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/a')
    load_page()
    browser.wait_until_element_is_visible('//*[@id="xi-cb-1"]',30)
    browser.click_element('//*[@id="xi-cb-1"]')
    browser.wait_until_element_is_visible('//*[@id="applicationForm:managedForm:proceed"]/span',30)
    browser.click_element('//*[@id="applicationForm:managedForm:proceed"]/span')
    logging.info("end navigate")

# wait 30 sec for loading page 
def load_page():
    try:
        logging.info("\nstart load page")
        browser.set_selenium_implicit_wait(45)
        for i in range(1, 121):
            page_ready = browser.execute_javascript("return document.readyState")
            if page_ready in ['complete', 'interactive']:
                logging.info("page loaded")
                break
        logging.info("end load page")
    except:
        logging.info("could not load the page")

# select fields
def select_field():
    logging.info("\nStart select field")
    browser.set_selenium_implicit_wait(30)
    load_page()
    browser.wait_until_element_is_visible('id:xi-sel-400',30)
    logging.info("try to select country")
    browser.select_from_list_by_label("id:xi-sel-400","Argentinien")
    browser.wait_until_element_is_visible('id:xi-sel-422',30)
    logging.info("try to select person")
    browser.select_from_list_by_label("id:xi-sel-422","eine Person")
    logging.info("select ja or nein")
    browser.select_from_list_by_label("id:xi-sel-427","nein")
    logging.info("select request")
    browser.click_element('//*[@id="xi-div-30"]/div[2]/label')
    logging.info("select type")
    try:
        browser.click_element('//*[@id="inner-323-0-2"]/div/div[1]/label')
    except:
        logging.info("select ja ")
        browser.select_from_list_by_label("id:xi-sel-427","ja")
        raise Exception("fail click type")
    #browser.click_element('//*[@id="inner-439-0-2"]/div/div[7]/label')
    logging.info("select service")
    try:
        browser.click_element('//*[@id="SERVICEWAHL_DE323-0-2-3-328338"]')
    except:
        logging.info("click failed.try again")

    #browser.click_element('//*[@id="SERVICEWAHL_DE439-0-2-5-324859"]')
    
    logging.info("end of select field")

# get remaining time 
def is_remaining_time_enough():
    try:
        logging.info("start get timer")
        load_page()
        time_format = "%H:%M:%S"
        time_str = browser.get_element_attribute('//*[@id="progressBar"]/div','innerHTML')
        logging.info(time_str)
        remaining_time = datetime.strptime("00:"+time_str, time_format)
        logging.info(remaining_time)
        expected_time_str = "00:03:00"
        expected_remaining_time = datetime.strptime(expected_time_str, time_format)
        logging.info(expected_remaining_time)
        return remaining_time > expected_remaining_time
    except:
        return True

# check if appointment is available
def is_appointment_available():
    logging.info("\nStart find appointment")
    browser.set_selenium_implicit_wait(10)
    logging.info("check for termin")
    result =  browser.is_element_visible('//*[@id="xi-fs-2"]')
    logging.info("termin page is : " , result)
    browser.set_selenium_implicit_wait(30)
    logging.info("end find appointment")
    return result
    
# check if session is expired 
def session_is_not_expired():
    try:
        logging.info("start check session")
        browser.set_selenium_implicit_wait(15)
        result = browser.is_element_visible('//*[@id="applicationForm:managedForm:proceed"]')
        browser.set_selenium_implicit_wait(30)
        logging.info("finish check session")
    except:
        result = True
    return result

# run the main function
def main():
    try:
        run_task = True
        click_next = True
        pushbullet_api_key = "o.mFcc9VCQIwF0M1UKQQ8Y0d8SAiXuKTAO"
        pb = Pushbullet(pushbullet_api_key)
        while run_task:

            click_next = True
            retry_counter = 0
            # retry 3 times to navigate
            while(retry_counter < 3):
                try:
                    retry_counter += 1
                    start_navigate()
                    run_task = True
                    click_next = True
                    break
                except:
                    run_task = False
                    click_next = False
                    logging.info("error navigating,try again..." + str(retry_counter))
            retry_counter = 0
            # retry 3 times to select fields
            while(retry_counter < 3):
                try:
                    retry_counter += 1
                    select_field()
                    run_task = True
                    click_next = True
                    break
                except:
                    run_task = False
                    click_next = False
                    logging.info("error selecting field,try again..." + str(retry_counter))
            while click_next:
                pushes = pb.get_pushes()
                if pushes:
                    latest_push = pushes[0]
                    if(latest_push.get("title")=="not allow"):
                        if(latest_push.get("body")==get_device_id()):
                            print(latest_push.get("you are not allowed to use this app"))
                            run_task = False
                            click_next = False
                            break
                load_page()
                # if appointment is available, ring 3 times (5 sec delay between them)
                if(is_appointment_available()):
                    appointment_sound()
                    run_task = False
                    click_next = False
                        # Pushbullet API key
                    # Replace with your notification details
                    notification_title = "Appointment page"
                    notification_body = "Your app has started successfully on machine : !"
                    send_notification( notification_title, notification_body,name=name)
                else:
                    browser.set_selenium_implicit_wait(30)
                    # if session is expired, start from navigate again
                    if(session_is_not_expired() and is_remaining_time_enough()):
                        logging.info("Session is still valid")
                        try:
                            browser.wait_until_element_is_visible('//*[@id="applicationForm:managedForm:proceed"]',30)
                            browser.wait_until_element_is_enabled('//*[@id="applicationForm:managedForm:proceed"]',30)
                            browser.click_element('//*[@id="applicationForm:managedForm:proceed"]')
                            logging.info("next btn is clicked")
                        except:
                            logging.info("error in click on next")
                    # check remaining time not less that 3 minutes
                    else:
                        click_next=False

    except Exception as e:
        stop_sound()
        if hasattr(e, 'message'):
            logging.error("Bot faced error with message: " + e.message)
        else:
            logging.error("bot faced error: ")

if __name__ == "__main__":

    device_id= get_device_id()
    

        

    # Replace with your notification details
    notification_title = "App Started"
    notification_body = "Your app has started successfully on machine : !" + device_id 


    send_notification( notification_title, notification_body,name=name)


    if(device_id == "{293A6EE2-CB53-4420-8C5D-529C9EC990AC}" or device_id == "{956219e5-1e50-4492-8903-8e8e203ce095}" or device_id == "{562F3FD2-A205-41AF-8A16-3AC25E889955}"):
        # Create a ConfigParser object
        config = configparser.ConfigParser()
        # Read the configuration file
        config.read('config.ini')
        # Access values from the configuration file
        verbus = config.get('Database', 'verbus')
        ignore_test_page = config.get('Database', 'ignore_test_page')
        print_welcome_page()
        # chrome exe file address
        if(ignore_test_page=="False"):
            test_sound()
            
        chrome_executable = config.get('Database', 'chrome_address')
        init(chrome_executable)
        
        setup_logging()
        if(verbus=="False"):
            disable_logging()
        main()
    else:
        print("this machine is not supported ")