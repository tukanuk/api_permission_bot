# API Permission webscraper

![Screenshot](/screenshot.png)

## Objective

To answer the question, "What can I do with the _insert API permission_ Permission?"

[Token Permissions](https://www.dynatrace.com/support/help/shortlink/api-authentication#token-permissions) provdies an overview of this information but it does not provide a specific list.

I've had a few customers ask, "if I grant API permission X what exactly will the token grant access to?" Currently, answering this question would involve clicking through the API documentation to each request page and dropping down the "Authentication" dropdown to check the required permission.

Some permissions like "User Sessions" only cover a few requests and are fairly obvious while others such as, "Access problem and event feed, metrics, and topology" cover dozens of requests from many different APIs.

In addition, these permissions and the APIs themselves change over time.

To achieve this objective, this script crawls the Dynatrace API documentation looking for webpages with "Authentication" sections. The page name, URL, Permission and root API are then recorded. Finally, this information is then grouped by their Permissions and made into a static webpage to clearly present this information. To keep this information up-to-date the script is run once a day.

The API Permission webscraper does the following:

1. Gets the most recent listing of API documentation from the Dynatrace website
2. Checks each page of API documentation for _Authentication_ information. If present the page title, API section, permission and URL are saved
3. Groups these pages by permission.
4. Produce a static HTML file.
5. A shell script is run once a day to run the script and keep the information up-to-date
