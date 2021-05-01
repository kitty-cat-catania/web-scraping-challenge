from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    #Splinter setup 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)

    url = 'https://redplanetscience.com'
    browser.visit(url)

    html = browser.html
    chum = bs(html, 'html.parser')

    for x in range(0,1):
        titles = chum.find('div', class_='content_title').text
        p_text = chum.find('div', class_ = 'article_teaser_body').text
    
    
        print(titles)
        print('-----')
        print(p_text)

    mars_news_title= titles
    mars_news_p = p_text

    browser.quit()


    #JPA Featured Image

    #Splinter setup 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)    

    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    html = browser.html
    noodle = bs(html,'html.parser')

    rel_path = noodle.find('img', class_="headerimage fade-in")['src']

    featured_img_url = url + '/'+ rel_path

    browser.quit()


    #Mars Facts

    url = 'https://galaxyfacts-mars.com'
    

    m_facts=pd.read_html(url)

    good_table = m_facts[1]
    html_tab=good_table.to_html()


    #Mars Hemisphere
    #Splinter setup 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)
    h_url = 'https://marshemispheres.com'
    browser.visit(h_url)

    html=browser.html
    chowder = bs(html, 'html.parser')

    items = chowder.find_all('div', class_='item')
    h_titles = []
    url_things=[]

    for item in items:
        h3=item.find('h3').text
        h_titles.append(h3)
    
        try:
            browser.links.find_by_partial_text(h3).click()
        
            html2 = browser.html
            clamy= bs(html2, 'html.parser')
            download = clamy.find('div', class_='downloads')
            list1=download.find('li')
            attribute = list1.find('a')
            img_spec= attribute['href']
            url_things.append(img_spec)
            browser.links.find_by_partial_text('Back').click()
        except:
            print('nope')

    browser.quit()

    h_titles2=[]
    for h in h_titles:
        crystal=h.strip('Enhanced')
        h_titles2.append(crystal)

    img_urls=[]
    title=[]

    for i in range(0,4):
        seriously= h_titles2[i]
        k=url_things[i]
        why = (h_url + "/" + k)

        if i==0:
            dict1={"title":seriously, "img_url":why}
        elif i==1:
            dict2={"title":seriously, "img_url":why}
        elif i==2:
            dict3={"title":seriously, "img_url":why}
        elif i==3:
            dict4={"title":seriously, "img_url":why}

    hemisphere_image_urls = [dict1, dict2, dict3, dict4]
        
    
    mars_dict = {"mars_news_title": mars_news_title,
                 "mars_news_p": mars_news_p,
                 "featured_img_url": featured_img_url,
                 "html_tab": html_tab, 
                 "hemisphere_image_urls": hemisphere_image_urls}
    

    return mars_dict