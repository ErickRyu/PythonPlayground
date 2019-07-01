books = dict()

books = {
    'Cosmopolis': 'ST', 'Praise of doubt': "PB"
}

view = books.get('Cosmopois', 'what')
print(view)

if 'Cosmpolis' in books:
    print(books['Cosmopolis'])
else:
    print('NO')

try:
    print(books['Cosmoplis'])
except KeyError as e:
    print('KeyError: ', e)
