import re

url ='https://hstream.braydenlab.com/hstream/cpr_analyze_provider.php'


domain = re.findall('//([^.]*)', url)

print(domain[0])