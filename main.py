import requests



URL = 'https://reqbin.com/echo'

def isResponse200(status_code):

    if status_code == 200:
        print("OK -200")
        print(URL)
    else:
        print("status_code")


def main ():
    x = requests.get(URL)

    # print(x.text)
    # print(x.status_code)
    isResponse200(x.status_code)


if __name__ == '__main__':
    main()