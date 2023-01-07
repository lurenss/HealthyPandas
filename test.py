from HealthyPandas import HealthyPandas 

hpdf = HealthyPandas('./apple_health_export/dati_esportati.xml')
df = hpdf.get_running_workouts()
df.head()