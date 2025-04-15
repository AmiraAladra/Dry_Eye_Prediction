import pandas as pd

# create dummy features
def features_engineering(df):
    
   # change values in  column "Sleep disorder" to N = 0, and Y =1
    df['Sleep disorder'] = df['Sleep disorder'].map({'N': 0, 'Y': 1}) 
    
    # change values in  column "Wake up during night" to N = 0, and Y =1
    df['Wake up during night'] = df['Wake up during night'].map({'N': 0, 'Y': 1})
    
    # change values in  column "Feel sleepy during day" to N = 0, and Y =1
    df['Feel sleepy during day'] = df['Feel sleepy during day'].map({'N': 0, 'Y': 1})
    
   # change values in  column "Caffeine consumption" to N = 0, and Y =1
    df['Caffeine consumption'] = df['Caffeine consumption'].map({'N': 0, 'Y': 1}) 
    
   # change values in  column "Alcohol consumption" to N = 0, and Y =1
    df['Alcohol consumption'] = df['Alcohol consumption'].map({'N': 0, 'Y': 1}) 
    
    # change values in  column "Smoking" to N = 0, and Y =1
    df['Smoking'] = df['Smoking'].map({'N': 0, 'Y': 1})
    
  # change values in  column "Ongoing medication" to N = 0, and Y =1
    df['Ongoing medication'] = df['Ongoing medication'].map({'N': 0, 'Y': 1})  
    
    # change values in  column "Smart device before bed" to N = 0, and Y =1
    df['Smart device before bed'] = df['Smart device before bed'].map({'N': 0, 'Y': 1})
    
    # change values in  column "Medical issue" to N = 0, and Y =1
    df['Medical issue'] = df['Medical issue'].map({'N': 0, 'Y': 1})
    
    # change values in  column "Blue-light filter" to N = 0, and Y =1
    df['Blue-light filter'] = df['Blue-light filter'].map({'N': 0, 'Y': 1})
    
   # change values in  column "Discomfort Eye-strain" to N = 0, and Y =1
    df['Discomfort Eye-strain'] = df['Discomfort Eye-strain'].map({'N': 0, 'Y': 1}) 
    
   # change values in  column "Redness in eye" to N = 0, and Y =1
    df['Redness in eye'] = df['Redness in eye'].map({'N': 0, 'Y': 1}) 

    # change values in  column "Dry Eye Disease" to N = 0, and Y =1
    df['Dry Eye Disease'] = df['Dry Eye Disease'].map({'N': 0, 'Y': 1})

    # change values in  column "Itchiness/Irritation in eye" to N = 0, and Y =1
    df['Itchiness/Irritation in eye'] = df['Itchiness/Irritation in eye'].map({'N': 0, 'Y': 1})

    # Split values in column "Blood pressure" by "/" into two columns  systolic/diastolic
    df[['systolic', 'diastolic']] = df['Blood pressure'].str.split('/', expand=True)

    # drop "Blood pressure" column
    df.drop('Blood pressure', axis=1, inplace=True)

    # convert "systolic" and "diastolic" columns to integer
    df['systolic'] = df['systolic'].astype('int')
    df['diastolic'] = df['diastolic'].astype('int')

    # convert "Stress level" and "Stress level" columns to integer
    df['Stress level'] = df['Stress level'].astype('object')

    # Creating dummy variables of columns "Gender", "Stress level"
    df = pd.get_dummies(df, columns=['Gender', 'Stress level'])

    # Create a new feature called BMI according to this equation (Weight)/((Height/100)**2)
    df['BMI'] = df['Weight']/((df['Height']/100)**2)

    # export the cleaned data ti a csv file and call it cleaned
    df.to_csv('data//processed/cleaned_Dry_Eye_Dataset.csv', index=False)

    return df