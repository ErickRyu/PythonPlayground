import xml.etree.ElementTree as ET
data = '''<person>
    <name>Woong</name>
    <phone type="intl">
    +1 123 456 789
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
