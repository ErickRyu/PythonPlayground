import re

text = '   <meta property="og:image" content="https://scontent-icn1-1.cdninstagram.com/vp/70389481ae76a362a9eadc82e4456e2c/5D7F7727/t51.2885-15/e35/57056259_1304456143012542_4158355629822468895_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com" />\n   '

print(text)

result = re.findall('\S+?n.jpg\S+', text)
print(result)

jpg_url = result[0].split('"')[1]
print(jpg_url)
