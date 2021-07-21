<h1 align="center">:spider_web: Web Scraper :computer:</h1>

Web scraping is the practice of extracting content and data from a website using bots. Web scraping, unlike *screen scraping*, which replicates only the pixels seen onscreen, retrieves the underlying HTML code and, with it, the data contained in a database. The scraper can then copy the full website's content to another location. This custom code I built searches the source code of the page for specific parts I've defined and extracts the content I've asked it to extract.

### :warning: Beware
Before scraping any website, check the **_terms and conditions_** page to determine if there are any clear scraping rules. You should follow them if there are any. If there aren't any, it's more of a _guessing game._

#### :pensive:Note
- Sadly, not all websites support web scraping.

#### :books:Resource Used
- The example used is [Newegg eCommerce Online Store](https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?cm_sp=Tab_Components_3-_-visnav-_-Video-Graphic-Devices_2). Newegg Commerce, Inc. is a company that sells computer hardware and consumer gadgets online. Its headquarters are in the *City of Industry*, California.

## :hammer_and_wrench:Tools & Languages Used
- Anaconda Version 4.10.1
- Python Version 3.8.8
- Beautiful Soup - Beautiful Soup is a Python package for parsing HTML and XML documents.
- Extensible library for opening URLs -The `urllib.request` module

## :high_brightness: Best Practices when Web Scraping
- Never scrape more frequently than you need to.
- Consider caching the content you scrape so that it’s only downloaded once.
- Build pauses into your code using functions like `time.sleep()` to keep from overwhelming servers with too many requests too quickly.

## :electric_plug: What to Expect
- Script Results in `cmd.exe`
![Script Results in cmd.exe](https://user-images.githubusercontent.com/62080362/126538158-a6d698d6-c2a2-41b7-a7d8-420fa223ba83.png)

- Results in the Products.csv file
![Results in the Products.csv file)](https://user-images.githubusercontent.com/62080362/126538429-63c1468c-18f2-41ec-82a2-36a7ac069e4c.png)


<h3 align="center"> This code was built with :heart: and 2 cups of Coffee:coffee:</h3>
