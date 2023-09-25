from selenium import webdriver
import json 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  
# chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (for headless mode)
# chrome_options.add_argument('--remote-debugging-port=9222')  # Specify the debugging port
chrome_options.add_argument('--disable-web-security')  # Disable web security to prevent CORS issues (optional)
# chrome_options.add_argument('--allow-running-insecure-content')  # Allow running insecure content (optional)
# chrome_options.add_argument('--disable-dev-shm-usage')  # Disable /dev/shm usage (for headless mode)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://exactspace.co/")
# driver.get("https://cybervidyapeeth.in/")
performance_logs = driver.execute_script("return window.performance.getEntries();")

with open("captured_data.har", "w") as har_file:
    har_file.write(json.dumps(performance_logs))
driver.quit()
