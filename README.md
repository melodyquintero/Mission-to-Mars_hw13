

```python
# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import pandas as pd

```

# NASA Mars News

Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.


```python
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
```


```python
news_url = 'https://mars.nasa.gov/news/'
browser.visit(news_url)
```


```python
html = browser.html
soup = bs(html, 'html.parser')
```


```python
# find the latest news, results return the first 'slide' it found
latest_news = soup.find('li', class_='slide')
latest_news

news_title = latest_news.find('div',class_='content_title').text
news_p = latest_news.find('div',class_='article_teaser_body').text

```


```python
news_title
```




    'NASA Statement on Possible Subsurface Lake near Martian South Pole'




```python
news_p
```




    "A new paper suggests that liquid water may be sitting under a layer of ice at Mars' south pole."



# JPL Mars Space Images

find the image url for the current Featured Mars FULL SIZE Image


```python
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)
```


```python
browser.click_link_by_partial_text('FULL IMAGE')
# script shows picture as "Mediumsize", thus keep looking
```


```python
browser.click_link_by_partial_text('more info')
# lead to detailed page with fullsize image
```


```python
featured_image_url = browser.find_by_tag('figure').first.find_by_tag('a')['href']
```


```python
featured_image_url
```




    'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA19330_hires.jpg'



# Mars Weather

Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page


```python
weather_url = 'https://twitter.com/marswxreport'
browser.visit(weather_url)
```


```python
weather_html = browser.html
soup_weather = bs(weather_html, 'html.parser')

#print(soup_weather.prettify())
```


```python
mars_weather = soup_weather.find(class_='js-tweet-text-container').text
print(mars_weather)
```

    
    Radar analysis from the Mars Express orbiter indicates liquid water beneath the Planum Australe region.
    https://www.esa.int/Our_Activities/Space_Science/Mars_Express/Mars_Express_detects_liquid_water_hidden_under_planet_s_south_pole …pic.twitter.com/30d37fSxQc
    
    

# Mars Facts

###### Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.


```python
facts_url = 'https://space-facts.com/mars'
```


```python
facts_df = pd.read_html(facts_url)[0]
facts_df.columns = ['Measurement','Facts']
```


```python
facts_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Measurement</th>
      <th>Facts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Equatorial Diameter:</td>
      <td>6,792 km</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Polar Diameter:</td>
      <td>6,752 km</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mass:</td>
      <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Moons:</td>
      <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Orbit Distance:</td>
      <td>227,943,824 km (1.52 AU)</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Orbit Period:</td>
      <td>687 days (1.9 years)</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Surface Temperature:</td>
      <td>-153 to 20 °C</td>
    </tr>
    <tr>
      <th>7</th>
      <td>First Record:</td>
      <td>2nd millennium BC</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Recorded By:</td>
      <td>Egyptian astronomers</td>
    </tr>
  </tbody>
</table>
</div>




```python
facts_html = facts_df.to_html()
#facts_html
```




    '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>Measurement</th>\n      <th>Facts</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Equatorial Diameter:</td>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Polar Diameter:</td>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Mass:</td>\n      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Moons:</td>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Orbit Distance:</td>\n      <td>227,943,824 km (1.52 AU)</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Orbit Period:</td>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Surface Temperature:</td>\n      <td>-153 to 20 °C</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>First Record:</td>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Recorded By:</td>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>'




```python
soup_facts = bs(facts_html, 'html.parser')
mars_facts = soup_facts.find('table')
mars_facts
```




    <table border="1" class="dataframe">
    <thead>
    <tr style="text-align: right;">
    <th></th>
    <th>Measurement</th>
    <th>Facts</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <th>0</th>
    <td>Equatorial Diameter:</td>
    <td>6,792 km</td>
    </tr>
    <tr>
    <th>1</th>
    <td>Polar Diameter:</td>
    <td>6,752 km</td>
    </tr>
    <tr>
    <th>2</th>
    <td>Mass:</td>
    <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
    <th>3</th>
    <td>Moons:</td>
    <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
    <th>4</th>
    <td>Orbit Distance:</td>
    <td>227,943,824 km (1.52 AU)</td>
    </tr>
    <tr>
    <th>5</th>
    <td>Orbit Period:</td>
    <td>687 days (1.9 years)</td>
    </tr>
    <tr>
    <th>6</th>
    <td>Surface Temperature:</td>
    <td>-153 to 20 °C</td>
    </tr>
    <tr>
    <th>7</th>
    <td>First Record:</td>
    <td>2nd millennium BC</td>
    </tr>
    <tr>
    <th>8</th>
    <td>Recorded By:</td>
    <td>Egyptian astronomers</td>
    </tr>
    </tbody>
    </table>



# Mars Hemispheres

Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.


```python
hmph_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hmph_url)
```


```python
hmph_html = browser.html
soup_hmph = bs(hmph_html, 'html.parser')
```


```python
hmph_img_urls = []
hmph_items = soup_hmph.find_all("h3")
hmph_items
```




    [<h3>Cerberus Hemisphere Enhanced</h3>,
     <h3>Schiaparelli Hemisphere Enhanced</h3>,
     <h3>Syrtis Major Hemisphere Enhanced</h3>,
     <h3>Valles Marineris Hemisphere Enhanced</h3>]




```python
for i in hmph_items:
    items = {"title": " ".join(i.text.split(" ")[:-1])}
    browser.click_link_by_partial_text(i.text)
    items["img_url"] = browser.find_by_css("img[class='wide-image']").first["src"]
    hmph_img_urls.append(items)
    browser.click_link_by_partial_text("Back")
```


```python
hmph_img_urls
```




    [{'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg',
      'title': 'Cerberus Hemisphere'},
     {'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg',
      'title': 'Schiaparelli Hemisphere'},
     {'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg',
      'title': 'Syrtis Major Hemisphere'},
     {'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg',
      'title': 'Valles Marineris Hemisphere'}]


