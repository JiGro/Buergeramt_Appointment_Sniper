import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
import os


def browser_startup(chrome_driver):
    # List of user agents
    profiles = [
        {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'},
        {'user_agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'},
        {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'},
        {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.864.58'},
        {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'},
    ]
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={random.choice(profiles)["user_agent"]}')
    return webdriver.Chrome(executable_path=chrome_driver, options=options)


def get_ba_appointment(chrome_driver, ba_url, full_name, email, phone_number):
    driver = browser_startup(chrome_driver)
    driver.minimize_window()
    driver.get(ba_url)
    button = driver.find_element(By.XPATH, "//*[contains(text(), 'Termin berlinweit suchen')]")
    button.click()
    time.sleep(0.5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    termine = soup.find_all('td', attrs={'class':'buchbar'})
    result = [td for td in termine if "buchbar" in td.get("class") and "heutemarkierung" not in td.get("class")]
    if len(result) > 0:
        print("Bürgeramt appointment available")
        tag_knopf = driver.find_element(By.XPATH, "//td[@class='buchbar']")
        tag_knopf.click()
        try:
            time.sleep(0.5)
            termin_knopf = driver.find_element(By.XPATH, "//a[@title='Zu diesem Zeitpunkt einen Termin eintragen…']")
            termin_knopf.click()
            input_name = driver.find_element(By.XPATH, "//input[@id='familyName']")
            input_name.send_keys(full_name)
            input_email = driver.find_element(By.XPATH, "//input[@id='email']")
            input_email.send_keys(email)
            input_phone = driver.find_element(By.XPATH, "//input[@id='telephone']")
            input_phone.send_keys(phone_number)
            survey = driver.find_element(By.XPATH, "//select[@name='surveyAccepted']")
            select = Select(survey)
            select.select_by_visible_text('Ich stimme zu')
            agb_gelesen = driver.find_element(By.XPATH, "//input[@id='agbgelesen']")
            agb_gelesen.click()
            submit = driver.find_element(By.XPATH, "//button[@id='register_submit']")
            submit.click()
            print("Appointment successfully booked")
            driver.quit()
        except:
            print("Bürgeramt appointment no longer available")
            driver.quit()
    else:
        print("No Bürgeramt appointment available")
        driver.quit()


# Start-up variables
name = os.environ.get("FULL_NAME")
email_address = os.environ.get("EMAIL")
phone_nr = os.environ.get("PHONE_NUMBER")
chromedriver_path = os.environ.get("CHROMEDRIVER_PATH")
print(f"*** Start Scraping ***"
      f"\n - Name: {name}"
      f"\n - Email: {email_address}"
      f"\n - Phone Number: {phone_nr}")

# Personalausweis
#url_starting_point = "https://service.berlin.de/dienstleistung/120703/"
# Führerschein umtauschen
url_starting_point = "https://service.berlin.de/dienstleistung/121616/"
# Via Websocket
#dienstleistungs_id = "121616"
#websocket = f"https://service.berlin.de/terminvereinbarung/termin/tag.php?termin=1&anliegen[]={dienstleistungs_id}&dienstleisterlist=122210,122217,122219,122227,122231,122238,122243,122252,122260,122262,122254,122271,122273,122277,122280,122282,122284,327539,122291,122285,122286,122296,150230,122301,122297,122294,122312,122314,122304,122311,122309,317869,122281,122279,122276,122274,122267,122246,122251,122257,122208,122226&herkunft=http%3A%2F%2Fservice.berlin.de%2Fdienstleistung%2F{dienstleistungs_id}%2F"

for i in tqdm(range(1, 51)):
    get_ba_appointment(chrome_driver=chromedriver_path, ba_url=url_starting_point, full_name=name, email=email_address, phone_number=phone_nr)
    time.sleep(random.randint(10, 25))
