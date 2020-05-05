# API Permission webscraper

The API Permission webscraper does the following:

1. Gets the most recent listing of API documentation for the website
2. Checks each page of API documentation for *Authenticaton* information. Of present the page title, API section, permission and URL are saved
3. Groups these pages by permission. 
4. Produces a static HTML file. 