from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from loguru import logger
import undetected_chromedriver as uc

# 创建 SeleniumWire 的 Chrome 浏览器实例
option = webdriver.ChromeOptions()
option.binary_location = r'C:\Users\yuanzhijian\Downloads\Win_x64_1095473_chrome-win\chrome-win\chrome.exe'

driver = uc.Chrome(options=option)

# 添加请求拦截处理逻辑
def intercept_request(request):
    # 打印请求 URL 和请求头
    logger.debug('Request URL: %s' % request.url)
    # print('Request Headers:', request.headers)

# 注册请求拦截回调函数
# driver.request_interceptor = intercept_request

def interceptor_response(request, response):
    if request.url:
        logger.debug("request_url: %s" % request.url)


driver.response_interceptor = interceptor_response

# 打开页面
driver.get('https://www.life-data.cn/login')

# 等待页面加载完成
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# 等待一段时间，让JavaScript代码有足够的时间捕获网络请求
time.sleep(50)

# 关闭浏览器
driver.quit()