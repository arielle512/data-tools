# 日期：2020-05-09
# 用途：自动截取日报图片，用于自动发送日报邮件
# 问题：（1）页面没有完全加载完，需要设置等待时间；（2）页面图片截取不完整，需要调整option参数。

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_full_screenshot(chromedriver_path,wait_time,url,save_fn):
	option = webdriver.ChromeOptions()
	option.add_argument('--headless')                   # 不加该参数时，截图受使用的显示器影响，无法截取完整图片，加上该参数后解决
	option.add_argument('--disable-gpu')
	option.add_argument("--window-size=1600,2000")      # 当该参数的宽、高小于页面图片，也无法截取完成图片。该参数与第1个参数需同时符合条件。
	option.add_argument("--hide-scrollbars")            # 隐藏侧边滚动条

	driver = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=option)
	print(url)
	driver.get(url)
	time.sleep(wait_time)
	print(driver.title)

	scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
	scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
	driver.set_window_size(scroll_width, scroll_height)
	print(scroll_width,scroll_height)
	driver.save_screenshot(save_fn)
	time.sleep(5)

	driver.close()
	driver.quit()


if __name__ == '__main__':
	chromedriver_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver81.exe"        # chromedriver版本需与chrome浏览器版本一致
	url=r"https://bi.aliyuncs.com/token3rd/dashboard/view/pc.htm?pageId=873b45fc-4fcf-4efc-98c9-a2ddd649acc6&accessToken=b3d0fb2ba7badc56f001dd7f5e079be8"
	save_fn=r"D:\auto_job\daily_report.png"
	wait_time=5
	get_full_screenshot(chromedriver_path,wait_time,url,save_fn)
