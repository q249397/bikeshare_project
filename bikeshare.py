import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("\nPlease enter a city! "
                     "Chicago, New York City, Washington! \n>").lower()
        if city in cities:
            break
        else:
            print("\n{} is not in Database!\nPlease try again!".format(city))

    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input("\nPlease enter a month! "
                      "January - June or all for all! \n>").lower()
        if month in months:
            break
        else:
            print("\n{} is not in Database!\nPlease try again!".format(month))
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("\nPlease enter a day! "
                    "Monday - Sunday or all for all! \n>").lower()
        if day in days:
            break
        else:
            print("\n{} is not in Database!\nPlease try again!".format(day))

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['Start Hour'] = df['Start Time'].dt.hour
    df['Start End'] = df['Start Station'] + ' to '+ df['End Station']

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['Month'] == month]

    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) +1

        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    commonMonth = df['Month'].mode()[0]
    print('\n{} is the most common month.'.format(months[commonMonth -1].title()))

    # TO DO: display the most common day of week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    commonDay = df['day'].mode()[0]
    print('\n{} is the most common day.'.format(days[commonDay -1].title()))
    # TO DO: display the most common start hour
    commonHour = df['Start Hour'].mode()[0]
    print('\n{}:00 is the most common hour.'.format(commonHour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print('\n{} is the most common Start Station.'.format(common_start_st.title()))

    # TO DO: display most commonly used end station
    common_end_st = df['End Station'].mode()[0]
    print('\n{} is the most common End Station.'.format(common_end_st.title()))

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = df['Start End'].mode()[0]
    print('\n{} is the most common Start/End Station combination.'.format(common_start_end.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tripDurSum = df['Trip Duration'].sum()/3600
    tripDurSum = np.round(tripDurSum, 1)
    print('\n{} hour(s) is the total of Trip Duration.'.format(tripDurSum))

    # TO DO: display mean travel time
    tripDurMean = df['Trip Duration'].mean()/60
    tripDurMean = np.round(tripDurMean, 1)
    print('\n{} minute(s) is the mean of Trip Duration.'.format(tripDurMean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of different User Types:\n')
    user_types_ct = df['User Type'].value_counts().to_string()
    print(user_types_ct)

    # TO DO: Display counts of gender
    try:
        print('\nCounts of Gender:\n')
        gender_ct = df['Gender'].value_counts().to_string()
        print(gender_ct)
    except:
        print('\nSorry, there is no Gender Data for {}.\n'.format(city.title()))

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_yob = df['Birth Year'].min()
        max_yob = df['Birth Year'].max()
        common_yob = df['Birth Year'].mode()[0]
        print('\nThe oldest customer was born in {} ,the youngest customer was born in {} and the most year of birth is {}.'.format(int(min_yob),int(max_yob),int(common_yob)))
    except:
        print('\nSorry, there is no Birth Year Data for {}.\n'.format(city.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_raw_data(df):
    """Displays 5 lines of raw data."""
    print('Press enter to display 5 lines of raw data! Enter no to finish!')
    row = 0
    while (input()!= 'no'):
        row = row+5
        print(df.head(row))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
