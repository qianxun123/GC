import requests
import login

headers = {"Content-Type": "application/json;charset=UTF-8"}


def login():
    """获取token"""
    data = {"pwd": "123456b22",
            "userName": "cba123"
            }

    url = "http://api.yansl.com:8084/login"

    r = requests.post(url=url, json=data, headers=headers)
    print(r.headers)
    print(r.json())
    # 将获取到的token返回
    return (r.json()["data"]["token"])

def confirm_login():
    """调用获取登录信息接口，将登录成功后，返回的token放在该请求的header中"""
    # 将login（）方法中返回的token放入header中
    headers["Token"] = login()
    data = {
        "newPwd": "123456b23",
        "oldPwd": "123456b22",
        "reNewPwd": "123456b23",
        "userName": "cba123"
    }
    r = requests.post(
        url="http://api.yansl.com:8084/user/changepwd",
        headers=headers,json=data
    )
    print(r.headers)
    print(r.json())
if __name__ == '__main__':
    confirm_login()

