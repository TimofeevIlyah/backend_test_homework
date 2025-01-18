import requests

LOGIN_URL = 'http://158.160.172.156/login/'

if __name__ == '__main__':
    session = requests.session()
    response = session.get(LOGIN_URL)
    # print(session.cookies.get_dict())
    CSRFToken = response.text.split(
        '<input type="hidden" name="csrfmiddlewaretoken" value="'
        )[1].split('"')[0]

    data = {
        'username': 'test_parser_user',
        'password': 'testpassword',
        'csrfmiddlewaretoken': CSRFToken
    }

    response = session.post(LOGIN_URL, data=data)
    response.encoding = 'utf-8'
    response.raise_for_status()
    # print(response.text)
    print(response.status_code)
