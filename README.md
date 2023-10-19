# Python-scripts
This README.md is for the Webscraper script ➡️

Visit my blog here to see an in-depth explanation of the code ➡️ https://spcyber.wixsite.com/shonepcyber/post/github-secrets-scraper-python
#
This code is a Python script that uses the Selenium library to scrape a GitHub repository or webpage for potential credentials. It does this by navigating through the repository's pages and searching for specific keywords like "password" in the HTML source.

Here's a breakdown of how the code works:
#
#
Import necessary modules:

- time: This module is used for adding delays to the script.
- selenium: The selenium library is used for automating web browser interactions.
- webdriver: This is the main class that allows you to control a web browser.
- Options and chrome_options: These are used to configure the Chrome web driver for Selenium.
- By: This class from selenium.webdriver.common.by is used for locating web elements by various methods (e.g., by class name).
#
#
- The script starts by asking the user for the URL of the webpage they want to scrape for credentials. The input is stored in the scraper variable.

- It configures the Chrome web driver with the specified options using webdriver.ChromeOptions().

- It initializes the web driver with the configured options.

- The script then opens the specified webpage using driver.get(scraper).

- It initializes two empty lists, links and flink, which will be used to store links to different pages and repository URLs.

- The loop_link function is defined. This function takes a URL as an argument and is responsible for navigating to that URL, finding links to files within a GitHub repository, and calling the last_page function for each file URL.

- The last_page function is responsible for checking the HTML source of a given page for the presence of the word "password" and printing a message if credentials are found.

- The script iterates through the repositories on the current GitHub page and appends their names to the links list. It also constructs the full repository URLs and appends them to the flink list.

- The script then calls the loop_link function for each repository URL in the flink list, which navigates to each repository's page and searches for credentials in the files.

- This code is a basic web scraping script, but it's important to note that scraping websites, especially those with login and password pages, can potentially violate terms of service and legal restrictions. Always ensure that you have permission to scrape a website and consider ethical and legal implications before using such code.
