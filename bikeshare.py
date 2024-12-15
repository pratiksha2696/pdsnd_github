
# Import necessary libraries
import time  # For handling time-related operations
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations and array handling

CITY_DATA = { 'chicago': "C:\\Users\\Pratiksha\\PythonWork\\Bikeshare\\chicago.csv",
              'new york city': 'C:\\Users\\Pratiksha\\PythonWork\\Bikeshare\\new_york_city.csv',
              'washington': 'C:\\Users\\Pratiksha\\PythonWork\\Bikeshare\\washington.csv' }

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
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input("Please enter a city (chicago, new york city, washington): ").lower()
        if city in cities:
            print(f"You selected: {city.title()}")
            break
        else:
            print("Invalid input. Please try again.")

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Please enter a month (january to december) or 'all' to apply no filter: ").lower()
        if month in months:
            print(f"You selected: {month.title()}")
            break
        else:
            print("Invalid input. Please try again.")

    # TO DO: Get user input for day of week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Please enter a day of the week or 'all' to apply no filter: ").lower()
        if day in days:
            print(f"You selected: {day.title()}")
            break
        else:
            print("Invalid input. Please try again.")
    
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start & End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    # filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day.lower()]
    
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(f"Most common month: {df['month'].mode()[0]}")

    # TO DO: display the most common day of week
    print(f"Most common day of week: {df['day_of_week'].mode()[0]}")

    # TO DO: display the most common start hour
    
    print(f"Most common start hour: {df['hour'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"Most commonly used start station: {df['Start Station'].mode()[0]}")

    # TO DO: display most commonly used end station
    print(f"Most commonly used end station: {df['End Station'].mode()[0]}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    print(f"Most frequent combination of start station and end station trip: {df['Trip'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate total travel time
    print(f"Total time travel: {df['Trip Duration'].sum()}")
    
    # TO DO: display mean travel time
    print(f"Mean time travel: {df['Trip Duration'].mean()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("Gender data is not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(f"Earliest year of birth: {int(df['Birth Year'].min())}")
        print(f"Most recent year of birth: {int(df['Birth Year'].max())}")
        print(f"Most common year of birth: {int(df['Birth Year'].mode()[0])}")
    else:
        print("Birth year data is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    
    index = 0
    step = 5
    
    while(True):
        ans = input("Do you want to see 5 rows of data? (yes/no): ")
        if ans.lower() == 'yes':
            if index < len(df):
                print(df.iloc[index : index + step])  
                index += step   
            else:
                print("No more data to display.")
        elif ans.lower() == 'no':
            break
        else:
            print("Invalid input")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() == 'no':
            break
        elif restart.lower() == 'yes':
            continue
        else:
            print('Invalid input')
            break


if __name__ == "__main__":
	main()
