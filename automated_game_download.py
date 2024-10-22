from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

EXTENSION_PATH = r"C:\Program Files (x86)\Internet Download Manager\IDMGCExt.crx" # Adjust the extension path according to your requirement
WAIT = 10  # Maximum wait time for elements to load (in seconds)
PARALLEL_DOWNLOADS = 5  # Number of downloads to initiate before pausing
PAUSE = 180  # Duration to pause (in seconds)

# Set up Chrome options and add the IDM extension
chrome_options = Options()
chrome_options.add_extension(EXTENSION_PATH)
chrome_options.headless = True

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Replace with the actual URL for the game download site
url = "https://example.com/game"

try:
    driver.get(url)  # Navigate to the game download site

    try:
        # Wait until the dropdown element is clickable and then click it
        dropdown = WebDriverWait(driver, WAIT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.su-spoiler-title'))
        )
        dropdown.click()  # Open the dropdown to reveal download links
        
    except Exception as e:
        print(f"Error clicking dropdown: {e}")
        driver.quit()  # Exit if unable to click the dropdown
        exit()  # Stop further execution

    try:
        # Wait until all part links are present and gather their href attributes
        links = WebDriverWait(driver, WAIT).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "su-spoiler-content") and not(ancestor::div[contains(@class, "su-spoiler-closed")])]//a'))
        )
        part_links = [link.get_attribute('href') for link in links]  # Extract the URLs of all parts
    
    except Exception as e:
        print(f"Error retrieving part links: {e}")
        driver.quit()  # Exit if unable to retrieve links
        exit()  # Stop further execution

    # Iterate through each part link to initiate the download
    for count, part_link in enumerate(part_links, start=0):
        print(f"Index: {count} | {part_link}")  # Print the current index and part link
        driver.get(part_link)  # Navigate to the current part link

        # Wait for the free download method button to be clickable and click it
        try:
            continue_download = WebDriverWait(driver, WAIT).until(
                EC.element_to_be_clickable((By.ID, "method_free"))
            )
            continue_download.click()  # Click to continue to the download page

        except Exception as e:
            print(f"Error clicking continue download: {e}")
            continue  # Skip to the next part if an error occurs

        # Wait for the download button to be clickable and click it
        try:
            download_button = WebDriverWait(driver, WAIT).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Download")]'))
            )
            download_button.click()  # Initiate the download

        except Exception as e:
            print(f"Error clicking download button: {e}")
            continue  # Skip to the next part if an error occurs

        # Wait for the confirmation button to be clickable and click it
        try:
            confirm_download = WebDriverWait(driver, WAIT).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Continue")]'))
            )
            confirm_download.click()  # Confirm the download

        except Exception as e:
            print(f"Error clicking confirm download: {e}")
            continue  # Skip to the next part if an error occurs

        # Close any new windows that open during the download process
        window_handles = driver.window_handles
        for i in range(1, len(window_handles)):
            driver.switch_to.window(window_handles[i])  # Switch to the new window
            driver.close()  # Close the new window

        driver.switch_to.window(window_handles[0])  # Switch back to the original window

        # Increment the count for the number of downloads initiated
        count += 1

        # Pause the script after a set number of downloads
        if count % PARALLEL_DOWNLOADS == 0:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"{PAUSE} seconds wait started at {current_time}")  # Log the pause time
            time.sleep(PAUSE)  # Pause the script for the specified duration
            count = 0  # Reset the count after pausing

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the WebDriver and close all associated windows
    driver.quit()
