
# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import pandas as pd
import time
from selenium import webdriver

# # NASA Mars News
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.

# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

mars_data = dict()


def scrape():
    browser = init_browser()
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    # find the latest news, results return the first 'slide' it found
    latest_news = soup.find('li', class_='slide')
    
    news_title = latest_news.find('div',class_='content_title').text
    news_p = latest_news.find('div',class_='article_teaser_body').text
    #debug
    time.sleep(5)



    # # JPL Mars Space Images
    # find the image url for the current Featured Mars FULL SIZE Image
    
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    # lead to detailed page with fullsize image
    time.sleep(5)
    featured_image_url = browser.find_by_tag('figure').first.find_by_tag('a')['href']


    
    # # Mars Weather
    # Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page
    weather_url = 'https://twitter.com/marswxreport'
    browser.visit(weather_url)
    weather_html = browser.html
    soup_weather = bs(weather_html, 'html.parser')
    mars_weather = soup_weather.find(class_='js-tweet-text-container').text
  


    # # Mars Facts
    facts_url = 'https://space-facts.com/mars'
    facts_df = pd.read_html(facts_url)[0]
    facts_df.columns = ['Measurement','Facts']
    facts_html = facts_df.to_html()


    # # Mars Hemispheres
    # Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
    hmph_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hmph_url)
    hmph_html = browser.html
    soup_hmph = bs(hmph_html, 'html.parser')

    hmph_img_urls = []
    hmph_items = soup_hmph.find_all("h3")
    hmph_items


    for i in hmph_items:
        items = {"title": " ".join(i.text.split(" ")[:-1])}
        browser.click_link_by_partial_text(i.text)
        items["img_url"] = browser.find_by_css("img[class='wide-image']").first["src"]
        hmph_img_urls.append(items)
        browser.click_link_by_partial_text("Back")

    mars_data = {
        'news_title':news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url,
        'mars_weather': mars_weather,
        'mars_facts': facts_html,
        'hemisphere_image_urls': hmph_img_urls
        }

    return mars_data

