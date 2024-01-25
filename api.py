import requests
import random
import string
import datetime
domain = '@xxx.onmicrosoft.com'
username = 'xxx@xxx.onmicrosoft.com'
def get_users(accessToken):
    url = 'https://graph.microsoft.com/v1.0/users'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(f"获取用户列表的API: {response.status_code}")
    return response.json()
    
def post_user(accessToken):
    url = 'https://graph.microsoft.com/v1.0/users'
    headers = {'Authorization': 'Bearer ' + accessToken}
    name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    Pw = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
    payload = {
        "accountEnabled": True,
        "displayName": name,
        "mailNickname": name,
        "userPrincipalName": name + domain,
        "passwordProfile": {
            "forceChangePasswordNextSignIn": False,
            "password": Pw
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"创建用户的API: {response.status_code}\n 名字: {name}\n 密码: {Pw}")
    
def get_me(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    return (f"获取当前用户的API: {response.status_code}")
    
def delete_user(accessToken):
    users = get_users(accessToken)
    userPrincipalName = users.get('value')[random.randint(1,2)].get('userPrincipalName')
    if userPrincipalName != username:
        url = f'https://graph.microsoft.com/v1.0/users/{userPrincipalName}'
        headers = {'Authorization': 'Bearer ' + accessToken}
        response = requests.delete(url, headers=headers)
        print(f"删除用户的API: {response.status_code}\n 用户名: {userPrincipalName}")
        
# def post_posseword(accessToken):
#     users = get_users(accessToken)
#     userPrincipalName = users.get('value')[random.randint(1,2)].get('userPrincipalName')
#     url = f'https://graph.microsoft.com/v1.0/users/{userPrincipalName}/changePassword'
#     headers = {'Authorization': 'Bearer ' + accessToken}
#     Pw = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
#     payload = {
#         "currentPassword": "123456",
#         "newPassword": Pw
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     print(f"修改密码的API: {response.status_code}\n 用户名: {userPrincipalName}\n 密码: {Pw}")
   
def get_appRoleAssignments(accessToken):
    url = f'https://graph.microsoft.com/v1.0/users/{username}/appRoleAssignments'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(f"获取用户应用角色的API: {response.status_code}")
    
def post_calendar(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/calendars'
    headers = {'Authorization': 'Bearer ' + accessToken}
    name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    payload = {
        "name": name
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"创建日历的API: {response.status_code}\n 日历名: {name}")
    
def post_calendarGroup(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/calendarGroups'
    headers = {'Authorization': 'Bearer ' + accessToken}
    name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    payload = {
        "name": name
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"创建日历组的API: {response.status_code}\n 日历组名: {name}")

def post_event(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/events'
    Prefer = 'outlook.timezone="China Standard Time"'
    headers = {'Authorization': 'Bearer ' + accessToken, 'Prefer': Prefer}
    payload = {
        "subject": "Let's go for lunch",
        "body": {
            "contentType": "HTML",
            "content": "Does noon work for you?"
        },
        "start": {
            "dateTime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "timeZone": "China Standard Time"
        },
        "end": {
            "dateTime": (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "timeZone": "China Standard Time"
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"创建事件的API: {response.status_code}")
    
def post_findMeetingTimes(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/findMeetingTimes'
    Prefer = 'outlook.timezone="China Standard Time"'
    headers = {'Authorization': 'Bearer ' + accessToken, 'Prefer': Prefer}
    response = requests.post(url, headers=headers)
    print(f"查找会议时间的API: {response.status_code}")
 
# def post_getSchedule(accessToken):
#     url = 'https://graph.microsoft.com/v1.0/me/calendar/getSchedule'
#     Prefer = 'outlook.timezone="China Standard Time"'
#     headers = {'Authorization': 'Bearer ' + accessToken, 'Prefer': Prefer}
#     payload = {
#         "schedules": [username],
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     print(f"获取日历忙闲时间的API: {response.status_code}")

def get_calendar(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/calendars'
    header = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=header)
    print(f"获取日历列表的API: {response.status_code}")

def get_calendarGroup(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/calendarGroups'
    header = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=header)
    print(f"获取日历组列表的API: {response.status_code}")

def get_calendarView(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/calendarView'
    Prefer = 'outlook.timezone="China Standard Time"'
    headers = {'Authorization': 'Bearer ' + accessToken, 'Prefer': Prefer}
    starttime = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    endtime = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    response = requests.get(url, headers=headers, params={'startDateTime': starttime, 'endDateTime': endtime})
    print(f"获取日历视图的API: {response.status_code}")
    
def get_event(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/events'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(f"获取事件列表的API: {response.status_code}")
    
# def get_reminderView(accessToken):
#     starttime = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
#     endtime = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
#     url = f'https://graph.microsoft.com/v1.0/me/reminders(startDateTime={starttime},endDateTime={endtime})'
#     headers = {'Authorization': 'Bearer ' + accessToken}
#     response = requests.get(url, headers=headers)
#     print(response.json())
#     print(f"获取提醒列表的API: {response.status_code}")

def post_getMemberGroups(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/getMemberGroups'
    headers = {'Authorization': 'Bearer ' + accessToken}
    payload = {
        "securityEnabledOnly": False
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"获取用户(成员)组的API: {response.status_code}")
    return response.json()

def post_checkMemberGroups(accessToken):
    groupIds = post_getMemberGroups(accessToken).get('value')
    url = 'https://graph.microsoft.com/v1.0/me/checkMemberGroups'
    headers = {'Authorization': 'Bearer ' + accessToken}
    payload = {
        "groupIds": groupIds
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"检查用户(成员)组的API: {response.status_code}")

def post_getMemberObjects(accessToken):
    groupIds = post_getMemberGroups(accessToken).get('value')
    url = 'https://graph.microsoft.com/v1.0/me/getMemberObjects'
    headers = {'Authorization': 'Bearer ' + accessToken}
    payload = {
        "securityEnabledOnly": True,
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"获取用户(成员)对象的API: {response.status_code}")
    return response.json()

def post_checkMemberObjects(accessToken):
    memberIds = post_getMemberObjects(accessToken).get('value')
    url = 'https://graph.microsoft.com/v1.0/me/checkMemberObjects'
    headers = {'Authorization': 'Bearer ' + accessToken}
    payload = {
        "ids": memberIds
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"检查用户(成员)对象的API: {response.status_code}")

def get_createdObjects(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/createdObjects'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(f"获取用户创建的对象的API: {response.status_code}")

def get_licenseDetails(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/licenseDetails'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(f"获取用户许可证详情的API: {response.status_code}")

def get_drive(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/drive'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(f"获取用户驱动器的API: {response.status_code}")

def get_drive_children(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(f"获取用户驱动器子项的API: {response.status_code}")

def get_joinedTeams(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/joinedTeams'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(f"列出用户加入的团队的API: {response.status_code}")

def get_memberOf(accessToken):
    url = 'https://graph.microsoft.com/v1.0/me/memberOf'
    headers = {'Authorization': 'Bearer ' + accessToken}
    response = requests.get(url, headers=headers)
    print(f"获取用户(隶属于)的成员组的API: {response.status_code}")    
