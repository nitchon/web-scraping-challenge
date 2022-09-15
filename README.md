# web-scraping-challenge
Module 12 Challenge

# Description

Live by the web scrape, die by the scrape. Web scraping is another tool in the data science arsenal that allows a script to extract content and data from a website by using HTML elements. But it comes with a caveat: websites are not governed by an HTML monarch that dictates how exactly a page should be displayed. Therefore as long as the HTML behind a webpage is methodically created, the Python library, BeautifulSoup, in tandem with Splinter and PyMongo, will scrape for data with ease. 

The challenge combines web scraping with Flask and a non-relational database, MongoDB, to build a Flask app that returns a webpage pulling data on Mars from various sources. In this repository, there are two Python scripts, a Jupyter notebook and two folders containing HTML and CSS files. The first part of the challenge uses the interactive Jupyter Notebook to perfect scraping elements from the required websites. The notebook is titled 'mission_to_mars,' and gathers news articles and facts on Mars as well as images of the Mars hemispheres. After all the elements have been accounted for, the next part converts the Jupyter notebook into a Python script named 'scrape_mars.py,' packaging the code in the notebook as a function called 'scrape_info.' This also creates a database and collection in MongoDB. The remaining step is to building the Flask app that pulls that data stored in MongoDB, which is 'app.py' in the repository, and HTML to display the webpage, which is located in the templates folder entitled 'index.html.' The static folder contains a basic CSS styling. The final project is an empty webpage with a button 'Get Data!' Pressing the button returns all the Mars infomation scraped.

# Requirements

  - BeautifulSoup
  - Flask
  - MongoDB and PyMongo
  - Pandas
  - Requests
  - Splinter
  
# Visuals

Empty Webpage

![image](https://user-images.githubusercontent.com/107419765/190445442-7985c5d6-a090-48c7-b311-83a5bd609527.png)
