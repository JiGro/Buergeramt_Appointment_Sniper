# Berlin Bürgeramt Appointment Scraper (Experimental Use ONLY)

![Logo of the Project](https://images.pexels.com/photos/7821688/pexels-photo-7821688.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2)

This script is designed to experimentally scrape available appointments at Berlin's Bürgeramter (government offices) for document applications such as obtaining a driver's license or ID card. The script uses Selenium and BeautifulSoup to navigate the website and check for available appointments.

The script is designed to run for the set range, with a delay between each iteration to avoid overwhelming the website. The delay time is randomized between 10 and 25 seconds.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

### Installing
1. Clone the repository to your local machine
```
git clone https://github.com/<username>/berlin-buergeramt-scraper.git
```

2. Install the required packages
```
pip install -r requirements.txt
```
You will need to have the following installed:
- Python3
- Selenium
- BeautifulSoup
- Tqdm
- Chromedriver

3. Download the latest version of Chromedriver from here and add the path of the executable to the chromedriver_path variable in the script.

4. You will also need to set the following environment variables:
- FULL_NAME: Your full name
- EMAIL: Your email address
- PHONE_NUMBER: Your phone number
- CHROMEDRIVER_PATH: The path to the chrome driver executable


## Running the script
To run the script, simply execute the following command:
```
python BA_Termin_Sniper.py
```
The script will start running and will continue until you either manually stop it or the range limit is reached. It will print out messages to indicate whether an appointment was successfully booked, or if no appointment slots were available.

## Authors
- **Jimmy (JiGro)** - *Initial work* - [My Github Profile](https://github.com/JiGro)
