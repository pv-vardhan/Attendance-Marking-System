import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
import time


class Check:
    def checker(self, csv_file):
        print('Marking students Attendance')
        df = pd.read_csv(csv_file)
        df=df.iloc[1:]
        student_ids = list(set(df['ids'].tolist()))

        # Setup Chrome options
        options = Options()
        options.add_argument("--start-maximized")

        # Initialize WebDriver
        service = Service('/usr/bin/chromedriver')  # Provide the correct path to chromedriver
        driver = webdriver.Chrome(service=service, options=options)

        try:
            driver.get("https://pv-vardhan.github.io/Rest/")

            # Wait for the checkbox element to be clickable and then click it
            for id in student_ids:
                WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, str(id)))
                ).click()
            while True:
                try:
                    driver.title  # This will raise an exception if the window is closed
                    time.sleep(1)  # Check every second if the window is still open
                except WebDriverException:
                    break  
                
        except TimeoutException:
            print("Not avilable")

        finally:
            # Clean up and close the browser
            driver.quit()
            open(csv_file, 'w').close()

# Instantiate and run the checker
checkbox = Check()
checkbox.checker('Attendance.csv')
