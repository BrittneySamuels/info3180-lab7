import requests
from bs4 import BeautifulSoup
import urlparse

url = "https://www.google.com.jm/search?hl=en&site=imghp&tbm=isch&source=hp&biw=1280&bih=656&q=shoes&oq=shoes&gs_l=img.3..0l10.12875.14469.0.14726.5.5.0.0.0.0.127.544.2j3.5.0....0...1ac.1.64.img..0.5.543.AoMSNWvARB0#imgrc=_"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

# This will look for a meta tag with the og:image property
og_image = (soup.find('meta', property='og:image') or
                    soup.find('meta', attrs={'name': 'og:image'}))
if og_image and og_image['content']:
    print og_image['content']
    print ''

# This will look for a link tag with a rel attribute set to 'image_src'
thumbnail_spec = soup.find('link', rel='image_src')
if thumbnail_spec and thumbnail_spec['href']:
    print thumbnail_spec['href']
    print ''


image = """<img src="%s"><br />"""
for img in soup.findAll("img", src=True):
   print img["src"]
   print ''

def get_image():
	image_url = []
	for img in soup.findAll("img", src=True):	
	   image_url.append(img["src"])
	return image_url

#print get_image()
