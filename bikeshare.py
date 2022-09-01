# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import statistics
import time
import pandas as pd
import numpy as np
from statistics import mode, multimode

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months=["all","january","february","march","april","june"]
monthabv = ["all", "jan", "feb", "mar", "apr", "jun"]
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
    cities = ["chicago", "new york city", "washington"]
    months = ["all", "january", "february", "march", "april", "june"]
    monthabv = ["all", "jan", "feb", "mar", "apr", "jun"]
    while True:
    # Validating the user input and not accepting any wrong input (spelling + wrong types)
        try:
            city =input("Please Enter the name of the city you want to analyze (chicago, new york city, washington) : ")
            city=city.lower()
            if city in cities :
                break
            print("PLease Enter a Valid City Name Chicago - New york city - Washington ")
        except TypeError or KeyboardInterrupt:
            print('A keyboard short cut was entered please enter a city')


    # get user input for month (all, january, february, ... , june)
    while True:
        # Validating the user input
        try:
            month = input("Please Enter the name of the month you want to analyze (all, january, february, ... , june) or ( all, jun, feb, .. jun): ")

            if month in months:
                break
            elif month in monthabv:
                index=monthabv.index(month)
                month=months[index]
                break
            else:
                print("--------------- Please Enter a Valid Month (January to June) And Try Again --------------")

        except Exception as e:
            print("\n")
            print("That\'s not a valid Month please Try again",e)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    while True:
        # Validating the user input
        try:
            day = input("Please Enter the name of the weekday you want to analyze (all, monday, tuesday, ... sunday) : ")
            if day not in days:
                print("Please check the spelling and try again")
            else:
                break
        except TypeError or KeyboardInterrupt or ValueError :
            print("That\'s not a valid city")

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
    if city == 'washington':
        washn=1
    if city == "new york city":
        df=pd.read_csv("new_york_city.csv")
    else:
        df=pd.read_csv(city+".csv")


    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['month'] =df["Start Time"].dt.month
    df['day_of_week'] = df["Start Time"].dt.day_name()
    df['hour'] = df["Start Time"].dt.hour

    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    month=months.index(month)
    # check if the day or month is equal to all no filter will be applied
    if month !=0 and day!='all':
        df = df[ df['month'] == month ]
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df,months=months):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month=df['month']
    mnth=statistics.mode(month)

    print("The most common month of the year is :",months[mnth-1])

    # display the most common day of week
    day_of_week = df['day_of_week']
    print("The most common day of the month is :", statistics.mode(day_of_week))

    # display the most common start hour
    hour=df['hour']
    mstchr=statistics.mode(hour)
    print("The most common hour is :",mstchr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station=df['Start Station']
    cntst = start_station.value_counts().max()
    mc=statistics.mode(start_station)
    print("The most common Start station is :",mc,"Count :",cntst)

    # display most commonly used end station
    end_station = df["End Station"]
    mostcommonEstation=statistics.mode(end_station)
    cnten=end_station.value_counts().max()
    print("The most common End station is :", mostcommonEstation,"Count :",cnten)

    # display most frequent combination of start station and end station trip
    df["full trip"]=df["Start Station"]+df["End Station"]
    ftr=df["full trip"]
    fulltrip=statistics.mode(ftr)

    print("Most frequent trip is :",fulltrip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    #Displays statistics on the total and average trip duration.

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=np.sum(df['Trip Duration'])
    print("The total trip time is :",total_time)


    # display mean travel time
    number_of_trips = len(df["Trip Duration"])
    print("Another avg",total_time/number_of_trips)
    avg_travel_time=np.mean(df['Trip Duration'])
    print("The average trip time is :",avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    #Displays statistics on bikeshare users.

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    usercountsCol = df["User Type"]
    usercounts= pd.value_counts(usercountsCol)
    print("The number of customers and subscribers is : ",usercounts)
    print(20*".")
    users=df.groupby(['User Type'])['User Type'].count()
    print("Another way to calculate the Customers and Subscribers by count",users)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\n'*2)
    return df


def user_age_stats(df):
        start_time = time.time()
        columns=df.columns

        if "Birth Year" in columns:



        # Display counts of gender
            usergenderCol = df["Birth Year"]
        #Get teh mode of years col to give the most common year of birth
            most_common_yob = statistics.mode(usergenderCol)
        #Filter Null values by adding the most common year of birth to the missing values cannot use the mean as because it is a date (years)
            df_nanfilter = usergenderCol.fillna(most_common_yob)
            count_by_year = df_nanfilter.value_counts()
            count_by_year.index=count_by_year.index.astype(int)

            print("The count of users by year of birth is :")
            print(count_by_year)
            print("Earliest, most recent, and most common year of birth are : ")


        # Display earliest, most recent, and most common year of birth
            earliest_bd=np.min(df_nanfilter)
            print("The earliest year of birth is :",earliest_bd.astype(int))

            most_recent_bd=np.max(df_nanfilter)
            print("most recent year of birth is :",most_recent_bd.astype(int))

            print("The most common year of birth is :", int(most_common_yob))


            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)

        else :
            print("This DataSet Dosen\'t Contain Any Statistics About Age.")

def data_output(df):
    start_time = time.time()
    """
          Main functions Take a dataframe and return Summary Stat filtered by the get filter function
          time_stats : Summary Stat for time
          station_stats : Stations Stats
          trip_duration_stats: Trip stats
          user_age_stats: Age stats only .
          user_stats : user_status without age
          """
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    user_age_stats(df)
    print("\nThis took %s seconds." % (time.time() - start_time))

def main():
    city, month, day = get_filters()
    df = load_data(city, month, day)
    n = 0
    indx=0
    while True:
        try:
            inpt = input('\nWould you like show 5 lines of data? Enter yes or no.\n')
            if inpt.lower() == 'yes':
                indx = indx+5
                pt = df[n:indx]
                n+=5
                print(pt)
            elif inpt.lower() == 'no':
                break
            print("...... Please Enter Yes or No And Try again ...... ")



        except KeyboardInterrupt as Ke:
            print(Ke)

    data_output(df)

    while True:
        try:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'no':
                break
            elif restart.lower()=='yes':
                city, month, day = get_filters()
                df = load_data(city, month, day)
                data_output(df)
            print(".......Please Enter Yes or No As an answer.......")
        except KeyboardInterrupt as Ke:
                    print(Ke)

if __name__ == "__main__":
	main()
