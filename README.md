# HealthyPandas

<img src="https://images2.imgbox.com/15/36/pONlxu0M_o.png)" alt="drawing" height="50" width="50"/>
Transform your Health app data into actionable insights with HealthyPandas - the easy-to-use library that takes the raw output from your iPhone's Health app export and converts it into Pandas dataframes. With HealthyPandas, you can quickly and easily analyze and work with your health data, using the full power of Pandas for data manipulation and analysis. Don't let your health data go to waste!


## Setup
1. Take your Iphone and go to Health app
2. Click your icon image on the top right
3. At the bottom there is 'Export all your health data' bottom, click on it
4. Once you have moved the zip file to your PC/MAC export it in the same folder of HealtyPandas 🐼
5. Now you are able to extrac what you need 

## Usage
```py
from HealthyPandas import HealthyPandas 

hpdf = HealthyPandas('./apple_health_export/exported_data.xml')
df = hpdf.get_running_workouts()
df.head()
```

## To do
1. Implement heart data extractor
2. Implement data extractor for other activities like (walking 🚶‍♂️,swimming 🏊‍♀️...)

