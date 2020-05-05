from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import simplelogging
import json

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
        dynatrace_soup = get_api_start_doc()

    menu_items_dict = get_menu_items(dynatrace_soup)

    # test the menu_items_dict
    try:
        assert "https://dynatrace.com/support/help/extend-dynatrace/dynatrace-api/configuration-api/service-api/request-naming-api/get-all/" == menu_items_dict[
            'GET all rules']
    except AssertionError as assErr:
        log.exception(
            "URL has changed. Maybe not a problem in production. A problem in dev.")
    else:
        log.info("Dictionary tests passsed")
        log.debug("menu_item_dict[\'GET all rules\'] == expected URL")

    api_authentication_info = api_doc_crawler(menu_items_dict)


def get_api_start_doc():
    """ Initial support page to parse """
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


def get_menu_items(soup):
    """ Returns a dictorary of page names and links parsed from the menu
    """
    api_menu = soup.select(
        'body > div.layout.is-flex > nav > ul > li:nth-child(5) > ul > li:nth-child(1)')

    log.debug(f"Len: {len(api_menu)}")

    # print(api_menu[0].prettify())
    menu_links = api_menu[0].select('a')
    log.debug(type(menu_links))
    # log.debug(str(menu_links))

    menu_items_dict = {}
    for link in menu_links:
        menu_items_dict[link.string.strip(
        )] = "https://dynatrace.com" + link['href']

    return menu_items_dict


def api_doc_crawler(menu_items_dict):
    """ Crawl the menu_items_dict """

    api_authentication_info = []
    limiter = 11
    for name, page in menu_items_dict.items():
        log.debug(f"Crawling: {name}")

        try:
            response = requests.get(page)
            response.raise_for_status
        except HTTPError as http_err:
            log.error(f"Error crawling: {http_err}")

        soup = BeautifulSoup(response.text, features="html.parser")
        parsed_title = soup.h1.text.split(" - ")
        try:
            permission = soup.section.article.p.strong.text
        except:
            permission = ""

        if len(parsed_title) > 1 and permission is not "":
            api_authentication_info.append(
                [parsed_title[1], permission, parsed_title[0], page])
            log.info(f"{parsed_title[1]} added to the list")
        else:
            log.debug(f"SKIPPED: {parsed_title[0]} ({page})")
        if limiter == 10:
            log.debug(f"Stopping at {limiter} for testing purposes")
            break
        else:
            limiter += 1

    with open("api_info.json", "w") as fp:
        json.dump(api_authentication_info, fp, indent=4)

    return api_authentication_info


if __name__ == "__main__":
    main()
