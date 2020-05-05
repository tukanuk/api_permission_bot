from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import simplelogging
import json
import pandas


# TODO: to remove the URL column and make API column linkable I'd have to build the indivdiual tables by hand. 
# TODO: or maybe use soup to edit every place a <tr><td><ADD LINK HERE>name</a> occurs
USE_LOCAL_OBJECTS = True

log = simplelogging.get_logger(
    logger_level=simplelogging.DEBUG, console=True, console_level=simplelogging.DEBUG, file_name="log.log")


def main():

    # Get the inital page (used for scraping the menu)
    if USE_LOCAL_OBJECTS:
        with open('dynatrace_soup.html', 'r') as fp:
            dynatrace_soup = BeautifulSoup(fp.read(), features="html.parser")
        log.debug(
            f"Loaded soup from local storage. Object type: {type(dynatrace_soup)}")
    else:
        dynatrace_soup = get_api_start_doc()

    # Scrape the menu
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

    # Scrape the actual pages from the menu items
    if USE_LOCAL_OBJECTS:
        with open('api_info.json', 'r') as fp:
            api_authentication_info = json.load(fp)
    else:
        api_authentication_info = api_doc_crawler(menu_items_dict)

    # Build the df
    all_the_info = data_manipulation(api_authentication_info)

    log.debug(f"Name: {all_the_info[0][0]}")
    log.debug(f"List: {all_the_info[0][1]}")
    log.debug(f"HTML: {all_the_info[0][2]}")

    build_the_html(all_the_info)


def build_the_html(all_the_info):
    # Build the final output HTML document

    head = """<!DOCTYPE html>
<html lang="en">
    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>API Permissions</title>
  </head>"""
    body = "<body><div class=\"container\"><h1>API Permissions</h1>"

    # add anchor links
    body += "<ul>"
    for item in all_the_info:
        body += "<li><a href=\"#" + item[0] + "\">" + item[0] + "</a></li>"
    body += "</ul>"

    # add the tables
    for item in all_the_info:
        body += "<h2><a id=\"" + item[0] + "\"></a>" + item[0] + "</h2>"
        body += item[2]

    body += "</div></body>"
    footer = "</html>"

    with open('api_permission.html', 'w') as fp:

        fp.write(head)
        fp.write(body)
        fp.write(footer)


def data_manipulation(api_authentication_info):
    # Group by permission
    # Returns a list of API calls grouped by permisison
    df = pandas.DataFrame(api_authentication_info, columns=[
                          'API', 'Permission', 'Section', 'URL'])
    df_groups = df.groupby("Permission")
    groupNames = df_groups.groups
    sections = []
    for name in groupNames:
        # Add to list
        log.debug(f"Adding {name}")
        group = df_groups.get_group(name)
        log.debug(f"Type of group: {type(group)}")

        # save to html
        with open("html/" + name + ".html", 'w') as fp:
            group.sort_values(by=['Section'])[['API', 'Section', 'URL']].to_html(
                fp, index=False, border=None, render_links=True, classes='table table-hover')

        sections.append(
            [name, group[['API', 'Section', 'URL']], group.sort_values(by=['Section'])[['API', 'Section', 'URL']].to_html(
                index=False, border=0, render_links=True, classes='table table-hover table-sm')])

    return sections


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

    # full crawl takes a long time to run set a limit
    # very hacky fix this up
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
