import requests
import logging
import time


logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# sample URL of the application to check
URL = 'http://your-application-url.com'

# Function to check application status
def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f'Application is UP. Status code: {response.status_code}')
            return 'UP'
        else:
            logging.warning(f'Application is DOWN. Status code: {response.status_code}')
            return 'DOWN'
    except requests.exceptions.RequestException as e:
        logging.error(f'Application is DOWN. Error: {e}')
        return 'DOWN'

def main():
    while True:
        status = check_application_status(URL)
        print(f'Application status: {status}')
        time.sleep(60) 
if __name__ == '__main__':
    main()
