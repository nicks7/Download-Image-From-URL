import os
import requests

url = 'https://homepages.cae.wisc.edu/~ece533/images/arctichare.png'
page = requests.get(url)

f_ext = os.path.splitext(url)[-1]
f_name = 'image{}'.format(f_ext)
with open(f_name, 'wb') as f:
    f.write(page.content)