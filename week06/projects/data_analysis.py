# Exceeding Requirements: Asked the user to type in a country, then displayed the minimum, maximum, and average life expectancy
# for that country, as well as the years for minimum and maximum. Also added checks to ensure all prompts were valid.

# Open the file and close it after finish with the block
with open("life-expectancy.csv") as file:

    # Skip the first line
    next(file)

    # Create list for storing all names of the countries to check the validity of the user's prompt
    countries = ['afghanistan', 'africa', 'albania', 'algeria', 'american samoa', 'americas', 'andorra', 'angola', 'anguilla', 'antigua and barbuda', 'argentina',
                 'armenia', 'aruba', 'asia', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize',
                 'benin', 'bermuda', 'bhutan', 'bolivia', 'bonaire sint eustatius and saba', 'bosnia and herzegovina', 'botswana', 'brazil', 'british virgin islands',
                 'brunei', 'bulgaria', 'burkina faso', 'burundi', 'cambodia', 'cameroon', 'canada', 'cape verde', 'cayman islands', 'central african republic', 'chad',
                 'channel islands', 'chile', 'china', 'colombia', 'comoros', 'congo', 'cook islands', 'costa rica', "cote d'ivoire", 'croatia', 'cuba', 'curacao',
                 'cyprus', 'czech republic', 'democratic republic of congo', 'denmark', 'djibouti', 'dominica', 'dominican republic', 'ecuador', 'egypt', 'el salvador',
                 'equatorial guinea', 'eritrea', 'estonia', 'ethiopia', 'europe', 'faeroe islands', 'falkland islands', 'fiji', 'finland', 'france', 'french guiana',
                 'french polynesia', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'gibraltar', 'greece', 'greenland', 'grenada', 'guadeloupe', 'guam', 'guatemala',
                 'guinea', 'guinea-bissau', 'guyana', 'haiti', 'honduras', 'hong kong', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland',
                 'isle of man', 'israel', 'italy', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'kuwait', 'kyrgyzstan', 'laos',
                 'latin america and the caribbean', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'macao',
                 'macedonia', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall islands', 'martinique', 'mauritania', 'mauritius', 'mayotte',
                 'mexico', 'micronesia (country)', 'moldova', 'monaco', 'mongolia', 'montenegro', 'montserrat', 'morocco', 'mozambique', 'myanmar', 'namibia', 'nauru',
                 'nepal', 'netherlands', 'new caledonia', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'niue', 'north korea', 'northern america',
                 'northern mariana islands', 'norway', 'oceania', 'oman', 'pakistan', 'palau', 'palestine', 'panama', 'papua new guinea', 'paraguay', 'peru',
                 'philippines', 'poland', 'portugal', 'puerto rico', 'qatar', 'reunion', 'romania', 'russia', 'rwanda', 'saint barthlemy', 'saint helena',
                 'saint kitts and nevis', 'saint lucia', 'saint martin (french part)', 'saint pierre and miquelon', 'saint vincent and the grenadines', 'samoa',
                 'san marino', 'sao tome and principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles', 'sierra leone', 'singapore', 'sint maarten (dutch part)',
                 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south korea', 'south sudan', 'spain', 'sri lanka', 'sudan', 'suriname',
                 'swaziland', 'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'timor', 'togo', 'tokelau', 'tonga',
                 'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'turks and caicos islands', 'tuvalu', 'uganda', 'ukraine', 'united arab emirates',
                 'united kingdom', 'united states', 'united states virgin islands', 'uruguay', 'uzbekistan', 'vanuatu', 'vatican', 'venezuela', 'vietnam',
                 'wallis and futuna', 'western sahara', 'world', 'yemen', 'zambia', 'zimbabwe']

    # Declare variables for both the lowest and highest life expectancies
    min_expectancy = 999
    max_expectancy = -1

    # Declare variables for both the lowest and highest life expectancies of year of interest
    year_min_expectancy = 999
    year_max_expectancy = -1

    # Declare variables for both the lowest and highest life expectancies of country of interest
    country_min_expectancy = 999
    country_max_expectancy = -1

    # Declare variables for keeping track of the overall lowest and highest life expectancy year and the country
    min_year = ""
    max_year = ""
    min_country = ""
    max_country = ""
    year_sum = 0
    country_sum = 0
    year_count = 0
    country_count = 0

    # Declare variables for keeping track of the lowest and highest life expectancy countries of year of interest
    interest_min_country = ""
    interest_max_country = ""

    # Declare variables for keeping track of the lowest and highest year of country of interest
    country_min_year = ""
    country_max_year = ""

    # Prompt user for year of interest (ensuring it is a valid year number)
    year_interest = 0
    while year_interest < 1543 or year_interest > 2019:
        year_interest = (input("\nEnter the year of interest: "))

        # Check if 'year_interest' can be cast
        if year_interest.isdigit():
            year_interest = int(year_interest)

            # Check if the year of interest is valid
            if year_interest < 1543 or year_interest > 2019:
                print("Please, type a year between 1543 and 2019!")

        else:
            print("Please, type a year between 1543 and 2019!")
            year_interest = 0

    # Prompt user for country (ensuring it is a valid country name)
    country_interest = ""
    while country_interest not in countries:
        country_interest = input("Enter the country of interest: ").lower()

        if country_interest not in countries:
            print("Not a valid country!\n")

    # Iterate through each line of the file
    for line in file:

        # Strip each line of the file of any unwanted new lines "\n"
        clean_line = line.strip()

        # Split each line into parts
        parts = clean_line.split(",")

        # Declare variables for country, year, and life expectancy of each line
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])
    
       # Check if the lowest, reassign otherwise
        if life_expectancy < min_expectancy:
            min_expectancy = life_expectancy
            min_year = year
            min_country = country

        # Check if the highest, reassign otherwise
        if life_expectancy > max_expectancy:
            max_expectancy = life_expectancy
            max_year = year
            max_country = country
            
        # Get the same data for year of interest
        if year == year_interest:
            # Get the average
            year_sum += life_expectancy
            year_count += 1

            if life_expectancy < year_min_expectancy:
                year_min_expectancy = life_expectancy
                interest_min_country = country

            if life_expectancy > year_max_expectancy:
                year_max_expectancy = life_expectancy
                interest_max_country = country

        # Get the same data for country of interest
        if country.lower() == country_interest:
            country_sum += life_expectancy
            country_count += 1

            if life_expectancy < country_min_expectancy:
                country_min_expectancy = life_expectancy
                country_min_year = year

            if life_expectancy > country_max_expectancy:
                country_max_expectancy = life_expectancy
                country_max_year = year

    # Calculate the averages
    year_average = year_sum / year_count
    country_average = country_sum / country_count

    # Display all data
    print("\nThe overall max life expectancy is: {:.2f} from {} in {}".format(max_expectancy, max_country, max_year))
    print("The overall min life expectancy is: {:.2f} from {} in {}".format(min_expectancy, min_country, min_year))

    print("\nFor the year {}:".format(year_interest))
    print("The average life expectancy across all countries was {:.2f}".format(year_average))
    print("The max life expectancy was in {} with {:.2f}".format(interest_max_country, year_max_expectancy))
    print("The min life expectancy was in {} with {:.2f}".format(interest_min_country, year_min_expectancy))
    
    print("\nIn {}:".format(country_interest).title())
    print("The average life expectancy is: {:.2f}".format(country_average))
    print("The max life expectancy was {:.2f} in {}".format(country_max_expectancy, country_max_year))
    print("The min life expectancy was {:.2f} in {}\n".format(country_min_expectancy, country_min_year))