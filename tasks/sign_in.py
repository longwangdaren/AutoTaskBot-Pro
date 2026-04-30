from utils.browser import get_driver
from utils.logger import log

def run_sign_in(config):
    driver = get_driver()

    log("打开登录页面")
    driver.get(config["url"])

    log("输入账号密码")

    driver.find_element("id", config["username_id"]).send_keys(config["username"])
    driver.find_element("id", config["password_id"]).send_keys(config["password"])
    driver.find_element("id", config["login_id"]).click()

    log("登录完成")
    driver.quit()
