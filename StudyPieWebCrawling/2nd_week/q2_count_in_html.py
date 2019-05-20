import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum_of_comments = 0
for tag in tags:
    sum_of_comments += int(tag.text)

print('Sum of comments is', sum_of_comments)
