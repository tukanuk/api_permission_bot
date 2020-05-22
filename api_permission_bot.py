from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import simplelogging
import json
import pandas


# TODO: to remove the URL column and make API column linkable I'd have to build the indivdiual tables by hand.
# TODO: or maybe use soup to edit every place a <tr><td><ADD LINK HERE>name</a> occurs
# TODO: or use the formmater in to_html to edit on export
# TODO: add group by api

USE_LOCAL_OBJECTS = False

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
        # log.debug(menu_items_dict)
        assert "https://dynatrace.com/support/help/dynatrace-api/configuration-api/plugins-api/" == menu_items_dict[
            'Plugins']
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
    # all_the_info = data_manipulation_param(api_authentication_info, "Section")
    all_the_info = data_manipulation(api_authentication_info)

    # log.debug(f"Name: {all_the_info[0][0]}")
    # log.debug(f"List: {all_the_info[0][1]}")
    # log.debug(f"HTML: {all_the_info[0][2]}")

    build_the_html(all_the_info)


def build_the_html(all_the_info):
    # Build the final output HTML document

    log.debug(f"Length of all_the_info: {len(all_the_info)}")

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

    # add the tabs
    body += """
    <nav>
  <div class="nav nav-tabs" id="nav-tab" role="tablist">
    <a class="nav-item nav-link active" id="nav-permission-tab" data-toggle="tab" href="#nav-permission" role="tab" aria-controls="nav-permission" aria-selected="true">Group by Permission</a>
    <a class="nav-item nav-link" id="nav-profile-tab" data-toggle="tab" href="#nav-api" role="tab" aria-controls="nav-api" aria-selected="false">Group by Section</a>
  </div>
</nav>
"""

    # add the permission tab
    body += """
    <div class="tab-content" id="nav-tabContent">
  <div class="tab-pane fade show active" id="nav-permission" role="tabpanel" aria-labelledby="nav-permission-tab">
"""
    # add anchor links
    body += 'Jump to:'
    body += '<div class="container"><div class="row"><div class="col-sm"><ul>'
    column_one = True
    for i, item in enumerate(all_the_info):
        body += '<li><a href=\"#' + \
            item[0] + "\">" + item[0] + '</a></li>'
        if i / len(all_the_info) >= 0.5 and column_one:
            log.debug(f"New column on enum {i-1}")
            log.debug(f"Len: {len(all_the_info)}")
            body += '</ul></div><div class="col-sm"><ul>'
            column_one = False
    body += "</ul></div></div></div>"

    # add the permission tables
    for item in all_the_info:
        body += "<h2><a id=\"" + item[0] + "\"></a>" + item[0] + "</h2>"
        body += item[2]

    body += """</div>"""

    # add the API tab
    body += """<div class = "tab-pane fade" id = "nav-api" role = "tabpanel" aria-labelledby = "nav-api-tab" > Group by API coming soon </div>


</div>
"""

    body += """ </div> <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src = "https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity = "sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin = "anonymous" > </script>
    <script src = "https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity = "sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin = "anonymous" > </script>
    <script src = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity = "sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin = "anonymous" > </script> </body>
    """
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


def data_manipulation_param(api_authentication_info, group_by="Permission"):
    # Group by group_by
    # Returns a list of API calls grouped by parameter
    df = pandas.DataFrame(api_authentication_info, columns=[
                          'API', 'Permission', 'Section', 'URL'])
    df_groups = df.groupby(group_by)
    groupNames = df_groups.groups
    sections = []
    for name in groupNames:
        # Add to list
        log.debug(f"Adding {name}")
        group = df_groups.get_group(name)
        log.debug(f"Type of group: {type(group)}")

        # save to html
        with open("html/" + group_by + "/" + name + ".html", 'w') as fp:
            group.sort_values(by=['API']).drop(group_by, axis=1).to_html(
                fp, index=False, border=None, render_links=True, classes='table table-hover')

        sections.append(
            [name, group[['API', 'Section', 'URL']], group.sort_values(by=['API'])[['API', 'Permission', 'URL']].to_html(
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
        'body > div.layout.is-flex > nav > ul > li:nth-child(7)')
    # api_menu = soup.select(
    #     'body > div.layout.is-flex > nav > ul > li:nth-child(7) > ul > li:nth-child(1)')

    log.debug(f"Len: {len(api_menu)}")

    # print(api_menu[0].prettify())
    menu_links = api_menu[0].select('a')
    log.debug(type(menu_links))
    # log.debug(str(menu_links))

    # problem is that there are repeat names and the dict overwrites them

    menu_items_dict = {}
    dup_counter = 0
    for link in menu_links:
        clean_link = link.string.strip()
        if clean_link in menu_items_dict:
            dup_counter += 1
            menu_items_dict[clean_link +
                            f" ({dup_counter})"] = "https://dynatrace.com" + link['href']
        else:
            menu_items_dict[clean_link] = "https://dynatrace.com" + \
                link['href']

    log.info(f"menu_items_dict is {len(menu_items_dict)} enteries long")
    link_list = ""
    for key, value in menu_items_dict.items():
        link_list += (f"{key:50}: {value}\n")
    log.debug(link_list)

    return menu_items_dict


def api_doc_crawler(menu_items_dict):
    """ Crawl the menu_items_dict """

    api_authentication_info = []

    # full crawl takes a long time to run set a limit
    # very hacky fix this up
    limiter = 10

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
