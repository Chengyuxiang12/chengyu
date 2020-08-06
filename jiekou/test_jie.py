import re

import pytest
import requests


# @pytest.fixture(scope="session")
def test_regist(username, password, phone, email):
    # 注册
    data = {

        "username": username,
        "password": password,
        "phone": phone,
        "email": email

    }
    res = requests.post("http://124.70.151.212:2333/regist", json=data)
    return res.json()


def test_login(username,password):
    # 登陆
    data = {
        "username": username,
        "password": password
    }
    res = requests.post("http://124.70.151.212:2333/login", json=data)

    return res.json()['data']['token']


def test_usersertmb():
    # 设置密保
    data = {
        "nickname": "程宇翔",
        "phone": "15574416429",
        "sex": "男",
        "job": "测试",
        "email": "fdwdwdwt@qq.com",
        "weixin": "1575785",
        "qq": "155sdds6",
        "userinfo": "hhhhhh",
        "address": "hhhhhhhh"
    }

    headers = {
        "Content-Type": "application/json",
        "token": test_login()
    }

    res = requests.post(f"http://124.70.151.212:2333/updateuserinfo",
                        json=data, headers=headers
                        )
    return res.json()


# def test_update(userid, name, mobile, test_token):
#     # 更新成员
#     data = {
#         "userid": userid,
#         "name": name,
#         "mobile": mobile,
#     }
#     res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",
#                         json=data)
#     return res.json()
#
#
# def test_delete(userid, test_token):
#     # 删除成员
#     res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
#     return res.json()


@pytest.mark.parametrize("username, password,phone,email", [("zhasfddwfa56", "1285416585", "15532719495", "wdoffge@qq.com"),("zhasdddwfa56", "1285416585", "15564719495", "ffge@qq.com")])
def test_all(username, password, phone, email):
    # 可能发生创建失败
    # try:
    assert True == test_regist(username, password, phone, email)["msg"]
    test_login(username,password)
# except AssertionError as e:
#     if "mobile existed" in e.__str__():
#         # 如果手机号被使用了，找出使用手机号的 userid ，进行删除
#         re_userid = re.findall(":(.*)'$", e.__str__())[0]
#         assert "deleted" == test_delete(re_userid, test_token)['errmsg']
#         assert 60111 == test_get(re_userid, test_token)['errcode']
#         assert "created" == test_create(userid, name, mobile, test_token)["errmsg"]
# # 可能发生userid不存在异常
# assert name == test_get(userid, test_token)['name']
# assert "updated" == test_update(userid, "xxxxxxx", mobile, test_token)['msg']
# assert "xxxxxxx" == test_get(userid, test_token)['name']
# assert "deleted" == test_delete(userid, test_token)['errmsg']
# assert 60111 == test_get(userid, test_token)['errcode']
