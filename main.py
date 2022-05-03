import requests
import logging

URL = 'https://reqbin.com/echo'

def write_to_log(URL):
    # TODO: add parametrizing output
    print(URL)
    logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    logging.info(URL)
    

def is_response_200(status_code):

    if status_code == 200:
        print("OK -200")
        write_to_log(URL)
    else:
        print("status_code")


def main ():
    x = requests.get(URL)
    is_response_200(x.status_code)


if __name__ == '__main__':
    main()
