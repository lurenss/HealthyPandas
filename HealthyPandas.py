import pandas as pd 
import xml.etree.ElementTree as ET
from impl_healthy_pandas import all_workouts_durations, running_workouts

class HealthyPandas:
    def __init__(self, path):
        self.path = path
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
    
    def get_all_workouts_durations(self) -> pd.DataFrame:
        '''Returns a DataFrame with all workouts in the file'''
        return all_workouts_durations(self.root)


    def get_running_workouts(self)-> pd.DataFrame:
            '''Returns a DataFrame with all workouts of a certain type'''
            return running_workouts(self.root)
            
