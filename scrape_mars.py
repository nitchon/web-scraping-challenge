from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser
def scrape_info():
    browser = init_browser()

    #Latest News Scrape
    mars_data = {}
    news_url = "https://redplanetscience.com/"
    browser.visit(news_url)
    news = []
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    articles = soup.find_all('div',class_='list_text')
    for article in articles:
        title = article.find('div',class_='content_title').text
        preview = article.find('div',class_='article_teaser_body').text
        news_dict = {'title':title,
                'preview':preview}
        news.append(news_dict)
    mars_data['news_title']=news_dict['title']
    mars_data['preview']=news_dict['preview']

    #JPL Featured Image Scrape
    jpl_url = 'https://spaceimages-mars.com/'
    browser.visit(jpl_url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    featured_image_url = jpl_url + soup.find('img',class_='headerimage fade-in')['src']
    mars_data['featured_image_url'] =featured_image_url

    #Mars Facts Scrape
    fact_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(fact_url)
    df= tables[0]
    df.columns = df.iloc[0]
    df=df[1:]
    df=df.set_index('Mars - Earth Comparison')
    html_table = df.to_html()
    html_table = html_table.replace('\n', '')
    mars_data['html_table']=html_table

    #Mars Hemispheres
    hemisphere_url = 'https://marshemispheres.com/'
    browser.visit(hemisphere_url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    images = soup.find_all('div',class_='item')
    hemisphere_img = []
    for image in images:
        name = image.find('img')['alt']
        grab_url = hemisphere_url + image.find('a')['href']
        browser.visit(grab_url)
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        img_url = hemisphere_url + soup.find('img',class_='wide-image')['src']
        name = soup.find('h2',class_='title').text
        hemisphere_dict={'name':name,
                        'img_url':img_url}
        hemisphere_img.append(hemisphere_dict)
    mars_data['hemisphere']=hemisphere_img
    

    browser.quit()

    return mars_data