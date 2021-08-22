import random as r
import sqlite3
Names = ['Liam',
    'Noah',
    'Oliver',
    'Elijah',
    'William',
    'James',
    'Benjamin',
    'Lucas',
    'Henry',
    'Alexander',
    'Mason',
    'Michael',
    'Ethan',
    'Daniel',
    'Jacob',
    'Logan',
    'Jackson',
    'Levi',
    'Sebastian',
    'Mateo',
    'Jack',
    'Owen',
    'Theodore',
    'Aiden',
    'Samuel',
    'Olivia',
    'Emma',
    'Ava',
    'Charlotte',
    'Sophia',
    'Amelia',
    'Isabella',
    'Mia',
    'Evelyn',
    'Harper',
    'Camila',
    'Gianna',
    'Abigail',
    'Luna',
    'Ella',
    'Elizabeth',
    'Sofia',
    'Emily',
    'Avery',
    'Mila',
    'Scarlett',
    'Eleanor',
    'Madison',
    'Layla',
    'Penelope']
lastNames = ['Smith',

    'Johnson',
    'Williams',
    'Brown',
    'Jones',
    'Garcia',
    'Miller',
    'Davis',
    'Rodriguez',
    'Martinez',
    'Hernandez',
    'Lopez',
    'Gonzalez',
    'Wilson',
    'Anderson',
    'Thomas',
    'Taylor',
    'Moore',
    'Jackson',
    'Martin',
    'Lee',
    'Perez',
    'Thompson',
    'White',
    'Harris',
    'Sanchez',
    'Clark',
    'Ramirez',
    'Lewis',
    'Robinson',
    'Walker',
    'Young',
    'Allen',
    'King',
    'Wright',
    'Scott',
    'Torres',
    'Nguyen',
    'Hill',
    'Flores',
    'Green',
    'Adams',
    'Nelson',
    'Baker',
    'Hall',
    'Rivera',
    'Campbell',
    'Mitchell',
    'Carter',
    'Roberts']
memberships = ['Free', 'Silver', 'Gold', 'Diamond']
countries = [
    'Austria',
    'Italy',
    'Belgium',
    'Latvia',
    'Bulgaria',
    'Lithuania',
    'Croatia',
    'Luxembourg',
    'Cyprus',
    'Malta',
    'Czechia',	
    'Netherlands',
    'Denmark',	
    'Poland',
    'Estonia',	
    'Portugal',
    'Finland',
    'Romania',
    'France'	,
    'Slovakia',
    'Germany',
    'Slovenia',
    'Greece'	,
    'Spain',
    'Hungary',	
    'Sweden',
    'Ireland'
]
addresses = ['Second', 'Third', 'First', 'Fourth','Park','Main','Oak', 'Pine','Maple', 'Elm']
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

print('Number of customers:')
input1 = input()
#Change the range to get that many users in the database.
for i in range(input1):
    firstname = Names[r.randint(0,49)]
    lastname = lastNames[r.randint(0,49)]
    email = firstname + lastname + "@email.com"
    id = i

    sign = '17.08.2021'

    membership = memberships[r.randint(0,3)]
    country = countries[r.randint(0,26)]
    address = addresses[r.randint(0,9)]+' Street'


    
    cursor.execute("INSERT INTO data VALUES (:first_name, :last_name, :email, :id, :sign_up_date, :membership, :country, :address)",
        {
            'first_name': firstname,
            'last_name': lastname,
            'email': email,
            'id': id,
            'sign_up_date': sign,
            'membership': membership,
            'country': country,
            'address': address
        })
    
conn.commit()
conn.close()
