import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']
months=['all','january','february','march','april','may','june']
days=['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("select the desired city [chicago or new york city or washington]")
    while True:    
        city = str(input()).lower()
        if city in cities:
            break
        else:
             print("Not-included, Enter valid city")
            

    print("Select filter: [month, day, both, no filter]")
    while True:
        type = str(input()).lower()
        if type == 'month' or type == 'day' or type == 'both' or type == 'no filter':
            break
        else:
            print("Enter a valid filter:")
               
    month = 'all'
    day = 'all'
    if type == 'month' or type == 'both':
        # TO DO: get user input for month (all, january, february, ... , june)
        print('Select the month or all:')
        while True:
            month = str(input()).lower()
            if month in months:  
                break
            else:
                print ("Not-included, Enter valid month")
            
    if type == 'day' or type == 'both':
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        print('Select the weekday or all:')
        while True:
            day = str(input()).lower()
            if day in days:                
                break
            else:
                print ("Not-included, Enter valid day")
                
    if type == "no filter":
        return city,month,day

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['Trip'] = df['Start Station']  + df['End Station']

    if month != 'all':
        months=['january','february','march','april','may','june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months=['january','february','march','april','may','june']
    # TO DO: display the most common month
    month = df['month'].mode()[0]
    print('The most common month is: ', months[month-1].title())

    # TO DO: display the most common day of week
    print('The most common day of the week is:', df['weekday'].mode()[0])

    # TO DO: display the most common start hour
    print('The most common start hour is:', df['hour'].mode()[0])   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station is:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is:', df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("the total travel time is:", "%.2f" % ((df['Trip Duration'].sum())/60.00), "Minutes")

    # TO DO: display mean travel time
    print("the mean travel time is:", "%.2f" % ((df['Trip Duration'].mean())/60.00), "Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types are:\n", df['User Type'].value_counts(), "\n")

    # TO DO: Display counts of gender
    if city != "washington":
        print("Counts of gender are:\n", df['Gender'].value_counts(), "\n")
    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birth year is", int(df['Birth Year'].min()))
        print("The most recent birth year is", int(df['Birth Year'].max()))
        print("The most common birth year is", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == "yes"):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()    
        if view_display == "no":
                             break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
