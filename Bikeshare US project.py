import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    #  Getting user's input for city (chicago, new york city, washington).
    while True:
        city = input("Would you like to see data from chicago, new york city, or washington?").lower().strip()

        if city not in CITY_DATA:
            print('Please enter a valid city name!')

        else:
            break

    # Getting user's input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to see data from january, february, march, april, may, june, or all of the them?").lower().strip()
        months = ['january', 'february', 'march', 'april', 'may', 'june']


        if month not in months and month != 'all':
            print("Please enter a valid month name!")

        else:
            break

    # Getting user's input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please type a day of the week or all in which you would like to see the data from.").lower().strip()
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

        if day not in days and day != 'all':
            print("Please write a valid day name!")

        else:
            break


    print('-'*40)
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

    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # Filtering by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # Filtering by month to create the new dataframe
        df = df[df['month'] ==month ]

    # Filtering by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

df = load_data('chicago', 'march', 'friday')

def display_raw_data(df):
    i = 0
    answer = input("Would you like to display the 1st 5 rows of data? please type yes or no.").lower().strip()
    pd.set_option('display.max_columns', None)

    while True:
        if answer == 'no':
            break
        print(df[i:i+5])
        answer = input("Would you like to display the following 5 rows of data? please type yes or no.").lower().strip()
        i+=5

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Displaying the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month:", most_common_month)

    # Displaying the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day of week:", most_common_day)

    # Displaying the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]

    print("Most common start hour:", most_common_start_hour)
    start_time = time.time()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Displaying most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most common start station:", most_common_start_station)

    # Displaying most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most common end station:", most_common_end_station)


    # Displaying most frequent combination of start station and end station trip
    most_frequent_start_end_station = (df['Start Station'] + df['End Station']).mode()[0]
    print("Most frequent combination of start station and end station trip:", most_frequent_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displaying total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total time travel:", total_travel_time)

    # Displaying mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean of travel time:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displaying counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:", user_types)

    # Displaying counts of gender
    if 'Gender' in df:
        print("Number of Gender:", df['Gender'].value_counts())


    # Displaying earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    print("The earliest year of birth:", earliest_year)

    most_recent_year = df['Birth Year'].max()
    print("The most recent year of birth:", most_recent_year)

    most_common_year = df['Birth Year'].mode()[0]
    print("The most common year of birth:", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
