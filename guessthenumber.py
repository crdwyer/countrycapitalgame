from random import randint
from time import sleep
import sys

Capitalquiz = {'Afghanistan': 'Kabul',
'Albania': 'Tirana',
'Algeria': 'Algiers',
'Andorra': 'Andorra la Vella',
'Angola': 'Luanda',
'Antigua and Barbuda': 'Saint Johns',
'Argentina': 'Buenos Aires',
'Armenia': 'Yerevan',
'Australia': 'Canberra',
'Austria': 'Vienna',
'Azerbaijan': 'Baku',
'The Bahamas': 'Nassau',
'Bahrain': 'Manama',
'Bangladesh': 'Dhaka',
'Barbados': 'Bridgetown',
'Belarus': 'Minsk',
'Belgium': 'Brussels',
'Belize': 'Belmopan',
'Benin': 'Porto-Novo',
'Bhutan': 'Thimphu',
'Bolivia': 'La Paz',
'Bosnia and Herzegovina': 'Sarajevo',
'Botswana': 'Gaborone',
'Brazil': 'Brasilia',
'Brunei': 'Bandar Seri Begawan',
'Bulgaria': 'Sofia',
'Burkina Faso': 'Ouagadougou',
'Burundi': 'Gitega',
'Cambodia': 'Phnom Penh',
'Cameroon': 'Yaounde',
'Canada': 'Ottawa',
'Cape Verde': 'Praia',
'Central African Republic': 'Bangui',
'Chad': 'NDjamena',
'Chile': 'Santiago',
'China': 'Beijing',
'Colombia': 'Bogota',
'Comoros': 'Moroni',
'Congo': 'Brazzaville',
'Congo': 'Kinshasa',
'Costa Rica': 'San Jose',
'Cote dIvoire': 'Yamoussoukro',
'Croatia': 'Zagreb',
'Cuba': 'Havana',
'Cyprus': 'Nicosia',
'Czech Republic': 'Prague',
'Denmark': 'Copenhagen',
'Djibouti': 'Djibouti',
'Dominica': 'Roseau',
'Dominican Republic': 'Santo Domingo',
'East Timor (Timor-Leste)': 'Dili',
'Ecuador': 'Quito',
'Egypt': 'Cairo',
'El Salvador': 'San Salvador',
'Equatorial Guinea': 'Malabo',
'Eritrea': 'Asmara',
'Estonia': 'Tallinn',
'Ethiopia': 'Addis Ababa',
'Fiji': 'Suva',
'Finland': 'Helsinki',
'France': 'Paris',
'Gabon': 'Libreville',
'The Gambia': 'Banjul',
'Georgia': 'Tbilisi',
'Germany': 'Berlin',
'Ghana': 'Accra',
'Greece': 'Athens',
'Grenada': 'Saint Georges',
'Guatemala': 'Guatemala City',
'Guinea': 'Conakry',
'Guinea-Bissau': 'Bissau',
'Guyana': 'Georgetown',
'Haiti': 'Port-au-Prince',
'Honduras': 'Tegucigalpa',
'Hungary': 'Budapest',
'Iceland': 'Reykjavik',
'India': 'New Delhi',
'Indonesia': 'Jakarta',
'Iran': 'Tehran',
'Iraq': 'Baghdad',
'Ireland': 'Dublin',
'Israel': 'Jerusalem',
'Italy': 'Rome',
'Jamaica': 'Kingston',
'Japan': 'Tokyo',
'Jordan': 'Amman',
'Kazakhstan': 'Astana',
'Kenya': 'Nairobi',
'Kiribati': 'Tarawa Atoll',
'North Korea': 'Pyongyang',
'South Korea': 'Seoul',
'Kosovo': 'Pristina',
'Kuwait': 'Kuwait City',
'Kyrgyzstan': 'Bishkek',
'Laos': 'Vientiane',
'Latvia': 'Riga',
'Lebanon': 'Beirut',
'Lesotho': 'Maseru',
'Liberia': 'Monrovia',
'Libya': 'Tripoli',
'Liechtenstein': 'Vaduz',
'Lithuania': 'Vilnius',
'Luxembourg': 'Luxembourg',
'Macedonia': 'Skopje',
'Madagascar': 'Antananarivo',
'Malawi': 'Lilongwe',
'Malaysia': 'Kuala Lumpur',
'Maldives': 'Male',
'Mali': 'Bamako',
'Malta': 'Valletta',
'Marshall Islands': 'Majuro',
'Mauritania': 'Nouakchott',
'Mauritius': 'Port Louis',
'Mexico': 'Mexico City',
'Micronesia': 'Palikir',
'Moldova': 'Chisinau',
'Monaco': 'Monaco',
'Mongolia': 'Ulaanbaatar',
'Montenegro': 'Podgorica',
'Morocco': 'Rabat',
'Mozambique': 'Maputo',
'Myanmar (Burma)': 'Rangoon',
'Namibia': 'Windhoek',
'Nepal': 'Kathmandu',
'Netherlands': 'Amsterdam',
'New Zealand': 'Wellington',
'Nicaragua': 'Managua',
'Niger': 'Niamey',
'Nigeria': 'Abuja',
'Norway': 'Oslo',
'Oman': 'Muscat',
'Pakistan': 'Islamabad',
'Palau': 'Melekeok',
'Panama': 'Panama City',
'Papua New Guinea': 'Port Moresby',
'Paraguay': 'Asuncion',
'Peru': 'Lima',
'Philippines': 'Manila',
'Poland': 'Warsaw',
'Portugal': 'Lisbon',
'Qatar': 'Doha',
'Romania': 'Bucharest',
'Russia': 'Moscow',
'Rwanda': 'Kigali',
'Saint Kitts and Nevis': 'Basseterre',
'Saint Lucia': 'Castries',
'Saint Vincent and the Grenadines': 'Kingstown',
'Samoa': 'Apia',
'San Marino': 'San Marino',
'Sao Tome and Principe': 'Sao Tome',
'Saudi Arabia': 'Riyadh',
'Senegal': 'Dakar',
'Serbia': 'Belgrade',
'Seychelles': 'Victoria',
'Sierra Leone': 'Freetown',
'Singapore': 'Singapore',
'Slovakia': 'Bratislava',
'Slovenia': 'Ljubljana',
'Solomon Islands': 'Honiara',
'Somalia': 'Mogadishu',
'South Africa': 'Cape Town',
'South Sudan': 'Juba',
'Spain': 'Madrid',
'Sri Lanka': 'Colombo',
'Sudan': 'Khartoum',
'Suriname': 'Paramaribo',
'Swaziland': 'Mbabane',
'Sweden': 'Stockholm',
'Switzerland': 'Bern',
'Syria': 'Damascus',
'Taiwan': 'Taipei',
'Tajikistan': 'Dushanbe',
'Tanzania': 'Dar es Salaam',
'Thailand': 'Bangkok',
'Togo': 'Lome',
'Tonga': 'Nukualofa',
'Trinidad and Tobago': 'Port of Spain',
'Tunisia': 'Tunis',
'Turkey': 'Ankara',
'Turkmenistan': 'Ashgabat',
'Tuvalu': 'Vaiaku village',
'Uganda': 'Kampala',
'Ukraine': 'Kyiv',
'United Arab Emirates': 'Abu Dhabi',
'United Kingdom': 'London',
'United States of America': 'Washington DC',
'Uruguay': 'Montevideo',
'Uzbekistan': 'Tashkent',
'Vanuatu': 'Port-Vila',
'Vatican City (Holy See)': 'Vatican City',
'Venezuela': 'Caracas',
'Vietnam': 'Hanoi',
'Yemen': 'Sanaa',
'Zambia': 'Lusaka',
'Zimbabwe': 'Harare',
}
import sys
print ("Welcome to the Country Capitals quiz.")
print()
begin = input("Would you like to begin?⌛: ")
print()
print("Press Cntrl C to answer")

if begin == "yes":
    print(" ")



else:
    print ("Ok please try again later!")
    sys.exit()

import random
score =0

states = list(Capitalquiz.keys())
for n in range(2):
    print("round", n+1)
    state = random.choice(states)
    capital = Capitalquiz[state]

    print("What is the capital of " + state + "? ")
    print()
    limit = 30
    stop = False
    for remaining in range(30,0,-5):
      print(remaining, "seconds" )
      if stop == True:
        break
      try:
        sleep(1)
      except KeyboardInterrupt :
        capital_guess = input("  Type your answer >  ")
        stop=True
    if capital_guess == capital:
        print ("That is correct good job! 😊 🏆")
        score= score + 1
    else:
        print("That is not correct 😱. The capital of " + state + " is " + capital + ".", "\n")


print("You got ", score, "out of 10 points")
print("Quiz Complete.")

def get_high_score():
    # Default high score
    high_score = 10

    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")

    return high_score


def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")


def main():
    """ Main program is here. """
    # Get the high score
    high_score = get_high_score()

    # Get the score from the current game
    current_score= score
    try:
        # Ask the user for his/her score
        current_score = int(input("What is your score? "))
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")

    # See if we have a new high score
    if current_score > high_score:
        # We do! Save to disk
        print("Yea! New high score!")
        save_high_score(current_score)
    else:
        print("Better luck next time.")

# Call the main function, start up the game
if __name__ == "__main__":
    main()
