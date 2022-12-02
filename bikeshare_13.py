from pickle import TRUE
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_name=CITY_DATA.keys()
month_name=['all','january','february','march','april','may','june']
day_name=['all','monday','tuesday','wednesday','thursday','friday','sunday']

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
        city=input("Enter your city from chicago, new york city, washington ?")
        if city in city_name:
            city=city.lower()
            print(city)
            break
        else:
            print("this is wrong choice,please return choice")

    # get user input for month (all, january, february, ... , june)
    while True:
        month =input("Enter your month from (all, january, february, ... , june)? ")
        if month in month_name:
            month=month.lower()
            print(month)
            break
        else:
            print("this is wrong choice,please return choice")

    # get user input for day of week (all, monday, tuesday, ... sunday)    
    while True:
        day=input('Enter your Day? ')
        if day in day_name :
            day=day.lower()
            print(day)
            break
        else:
            print("this is weong choice")
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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])

    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day
    df['hour']=df['Start Time'].dt.day
    # filter by month
    if month != 'all':
        months=['january','february','march','april','may','june']
        month = months.index(month)+1
        df=df[df['month']==month]
        print(df)
    # filter by day
    if day != 'all':
        days=['monday','tuesday','wednesday','thursday','friday','sunday']
        day=days.index(day)+1
        df=df[df['day']==day]
        print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # display the most common month
    common_month=df['month'].mode()[0]
    print(common_month)

    # display the most common day of week
    common_day=df['day'].mode()[0]
    print(common_day)
    # display the most common start hour
    common_start_hour=df['hour'].mode()[0]
    print(common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print(common_start_station)
    
    # display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print(common_end_station)
    # display most frequent combination of start station and end station trip
    frequent_combination=(df['Start Station']+df['End Station']).mode()[0]
    print(frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_tarvel=df['Trip Duration'].sum()
    print(total_tarvel)
    # display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print(mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df['User Type'].value_counts()
    print(user_types)
    # Display counts of gender
    if city == 'chicagoo.csv' or city == 'new york city.csv':
        gender=df['Gender'].value_counts()
        print(gender)
        # Display earliest, most recent, and most common year of birth
        earliest=df['Birth Year'].min()
        print(earliest)
        recent=df['Birth Year'].max()
        print(recent)
        common=df['Birth Year'].mode()[0]
        print(common)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def dispaly_data(df):
    
    print(df.head())
    start_loc = 0
    while TRUE:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data.lower()!= 'yes':
            break
        else :
            print("this is wrong choice,please return choice")
        end_loc = start_loc + 5
        print(df.iloc[start_loc:end_loc])
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        dispaly_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
