# from time import sleep
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# sleep(2)
# driver.get("https://baidu.com")
# sleep(2)
# driver.find_element_by_id('kw').send_keys('你好')
# sleep(2)
# driver.find_element_by_id('su').click()
# sleep(2)
# driver.quit()


import requests

data={
  "pwd": "123456a",
  "userName": "cba123"
}

def denglu():
    r=requests.post("http://api.yansl.com:8084/login",json=data)
    print(r.status_code)
    print(r.json())



# 修改密码
data1 = {
    "newPwd": "123456b",
    "oldPwd": "123456a",
    "reNewPwd": "123456b",
    "userName": "cba123"
}

def xg():

    r = requests.post("http://api.yansl.com:8084/user/changepwd", json=data1)
    print(r.status_code)
    print(r.json())













if __name__ == '__main__':
    denglu()
    xg()


