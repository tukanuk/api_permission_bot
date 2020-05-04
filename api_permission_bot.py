from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import simplelogging
import pickle

USE_LOCAL_OBJECTS = True

log = simplelogging.get_logger(
    logger_level=simplelogging.DEBUG, console=True, console_level=simplelogging.DEBUG, file_name="log.log")


def main():
    if USE_LOCAL_OBJECTS:
        with open('dynatrace_soup.html', 'r') as fp:
            dynatrace_soup = BeautifulSoup(fp.read(), features="html.parser")
        log.debug(
            f"Loaded soup from local storage. Object type: {type(dynatrace_soup)}")
    else:
        dynatrace_soup = get_api_doc_list()


def get_api_doc_list():
    try:
        response = requests.get(
            'https://www.dynatrace.com/support/help/')
        response.raise_for_status()
    except HTTPError as http_err:
        log.error(f'HTTP error occured: {http_err}')
    except Exception as err:
        log.error(f'Other error occured: {err}')
    else:
        log.info(f"Response is {response.status_code}. Looking good!")

    dynatrace_soup = BeautifulSoup(response.text, features="html.parser")

    with open('dynatrace_soup.html', 'w', encoding='utf-8') as fp:
        fp.write(str(dynatrace_soup.prettify()))

    return dynatrace_soup


if __name__ == "__main__":
    main()
