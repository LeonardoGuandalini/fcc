import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    d = df['race'].value_counts()
    race_count = d

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    men_ages = men['age']
    average_age_men = men_ages.mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    education = df['education'].value_counts()
    bachelors = education['Bachelors']
    percentage_bachelors = ((bachelors/education.sum())*100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`Q
    advanced_ed = df.loc[:, ['education', 'salary']]
    advanced_ed = advanced_ed[(advanced_ed['education']=='Bachelors') | (advanced_ed['education']=='Masters') | (advanced_ed['education']=='Doctorate')]
    salaries = advanced_ed['salary']
    lower_education = df.loc[:, ['education', 'salary']]
    lower_education = lower_education[(lower_education['education']!='Bachelors') & (lower_education['education']!='Masters') & (lower_education['education']!='Doctorate')]
    salaries_low = lower_education['salary']
    # percentage with salary >50K
    higher_education_rich = (((salaries.value_counts().loc['>50K'])/((salaries.value_counts().loc['>50K']) + (salaries.value_counts().loc['<=50K'])))*100).round(1)

    lower_education_rich = (((salaries_low.value_counts().loc['>50K'])/((salaries_low.value_counts().loc['>50K']) + (salaries_low.value_counts().loc['<=50K'])))*100).round(1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_rich_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')] 
    min_workers = df[df['hours-per-week'] == min_work_hours]
    min_workers = min_workers['salary']
    min_rich_workers = min_rich_workers['salary']
    num_min_workers = min_workers.value_counts().sum()
    num_rich_min_workers = min_rich_workers.value_counts().sum()

    rich_percentage = ((num_rich_min_workers / num_min_workers)*100).round(1)

    # What country has the highest percentage of people that earn >50K?
    population = df['native-country']
    population_values = population.value_counts()
    #population_values = pd.Series(population_values, index=df['native-country'], name='Population')
    rich_people = df[df['salary'] == '>50K']
    rich_people_by_country = rich_people['native-country']
    rich_values = rich_people_by_country.value_counts()
   
    proportions = {} 
    for each_country in rich_values.index:
        proportion = ((rich_values[each_country] / population_values[each_country])*100).round(1)
        proportions[each_country] = proportion

    values = proportions.values()
    highest_earning_country_percentage = max(values)
    for each_country in proportions:
        if proportions[each_country] == highest_earning_country_percentage:
            highest_earning_country =  each_country




    # Identify the most popular occupation for those who earn >50K in India.
    rich_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    rich_indians_occupation = rich_indians['occupation']
    top_IN_occupation = rich_indians_occupation.value_counts().index[0]


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
