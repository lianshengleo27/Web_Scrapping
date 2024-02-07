from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import glob

def download_data():
    options = webdriver.EdgeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Edge(options=options)
    # driver = webdriver.Edge()
    print("Scraping data...")
    # LOG IN
    driver.get('https://krccloud.secsynet.net/krccloud/login')
    driver.find_element(By.NAME, "login_id").send_keys("kyjctg")
    driver.find_element(By.NAME, "login_password").send_keys("kyjctg")
    # driver.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-caption btn-block"]').click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(3)

    # MOVE TO DOWNLOAD PAGE
    driver.find_element(By.LINK_TEXT, "データＤＬ").click()

    # SELECT SENSOR
    sensor_select = '土留壁の変位:G5-R26'
    driver.find_element(By.ID, "data_download_setting_id").click()
    dropdown_sensor = driver.find_element(By.ID, "data_download_setting_id")
    dropdown_sensor.find_element(By.XPATH, f"//option[. = '{sensor_select}']").click()

    # SELECT PERIOD
    period_select = '2週間'
    driver.find_element(By.ID, "designation_method_a").click()
    driver.find_element(By.ID, "designation_period").click()
    dropdown_period = driver.find_element(By.ID, "designation_period")
    dropdown_period.find_element(By.XPATH, f"//option[. = '{period_select}']").click()

    # SELECT INTERVAL
    interval_select = '30分'
    driver.find_element(By.ID, "interval_minute").click()
    dropdown_interval = driver.find_element(By.ID, "interval_minute")
    dropdown_interval.find_element(By.XPATH, f"//option[. = '{interval_select}']").click()

    # DOWNLOAD!!!
    driver.find_element(By.ID, "download_make").click()

    time.sleep(2)
    driver.quit()

    # MOVE FILE TO DESIGNATED DIR & RENAME FILE
    download_dir = r"C:\Users\u860011\Downloads"
    new_dir = r"C:\Users\u860011\Downloads\Measuring_Data\Web_Scrapping_Project\downloaded_RawData"
    # dt = str(datetime.datetime.now().strftime("%Y%m%d_%H%M"))

    new_file_name = sensor_select[-6:] + "_" + period_select + "_" + interval_select + ".csv"
    new_file_path = os.path.join(new_dir, new_file_name)  # G5-R26_2週間_30分
    # return path of the downloaded file
    file_pattern = 'download_*'
    downloaded_file_path = glob.glob(os.path.join(download_dir, file_pattern))
    old = downloaded_file_path[0]

    #REPLACE EXISTING FILE
    os.replace(old, new_file_path)

try:
    while True:
        download_data()
        print("Successfully downloaded data, waiting for the next loop...")
        time.sleep(60)

except KeyboardInterrupt:
    print("Exiting Data scrap...")
