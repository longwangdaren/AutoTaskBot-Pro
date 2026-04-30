from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 无界面模式（更专业）
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    return driver
