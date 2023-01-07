import pandas as pd 
import xml.etree.ElementTree as ET

def all_workouts_durations(root) -> pd.DataFrame:
    df_cols = []
    rows = []
    for node in root:
        if node.tag == 'Workout':
            df_cols = node.attrib.keys()
            rows.append(node.attrib.values())
    
    out_df = pd.DataFrame(rows, columns = df_cols)
    return out_df

def running_workouts(root) -> pd.DataFrame:
    #access also to the all the children of th node called WorkoutEvent
    df_cols = ['startDate','endDate','duration','StepCount','RunningGroundContactTimeAvg','RunningGroundContactTimeMin','RunningGroundContactTimeMax','RunningPowerAvg','RunningPowerMin','RunningPowerMax','ActiveEnergyBurned','BasalEnergyBurned','RunningVerticalOscillationAvg','RunningVerticalOscillationMin','RunningVerticalOscillationMax','RunningSpeedAvg','RunningSpeedMin', 'RunningSpeedMax','RunningStrideLengthAvg','RunningStrideLengthMin','RunningStrideLengthMax','DistanceWalkingRunning','HeartRateAvg','HeartRateMin','HeartRateMax']
    rows = []
    for node in root:
        row = []
        if node.tag == 'Workout' and node.attrib.get('workoutActivityType') == 'HKWorkoutActivityTypeRunning':
            row.append(node.attrib.get('startDate'))
            row.append(node.attrib.get('endDate'))
            row.append(node.attrib.get('duration'))
            for child in node:
                if child.tag == 'WorkoutStatistics':
                    #do a switch case here for the attrib 'type' StepCount RunningGroundContactTime RunningPower ActiveEnergyBurned BasalEnergyBurned RunningVerticalOscillation RunningSpeed RunningStrideLength DistanceWalkingRunning HeartRate
                    if child.attrib.get('type') == 'HKQuantityTypeIdentifierStepCount':
                        row.append(child.attrib.get('sum'))
                    elif child.attrib.get('type') == 'HKQuantityTypeIdentifierRunningGroundContactTime':
                        row.append(child.attrib.get('average'))
                        row.append(child.attrib.get('minimum'))
                        row.append(child.attrib.get('maximum'))
                    elif child.attrib.get('type') == 'HKQuantityTypeIdentifierRunningPower':
                        row.append(child.attrib.get('average'))
                        row.append(child.attrib.get('minimum'))
                        row.append(child.attrib.get('maximum'))
                    elif child.attrib.get('type') == 'HKQuantityTypeIdentifierActiveEnergyBurned':
                        row.append(child.attrib.get('sum'))
                    elif child.attrib.get('type') == 'HKQuantityTypeIdentifierBasalEnergyBurned':
                        row.append(child.attrib.get('sum'))
                    elif child.attrib.get('type') == 'HKQuantityTypeIdentifierRunningVerticalOscillation':
                        row.append(child.attrib.get('average'))
                        row.append(child.attrib.get('minimum'))
                        row.append(child.attrib.get('maximum'))
                    elif child.attrib.get('type') == 'HKQuantityTypeIdentifierRunningSpeed':
                        row.append(child.attrib.get('average'))
                        row.append(child.attrib.get('minimum'))
                        row.append(child.attrib.get('maximum'))
                    elif child.attrib.get('type') == 'HKQuantityTypeIdentifierRunningStrideLength':
                        row.append(child.attrib.get('average'))
                        row.append(child.attrib.get('minimum'))
                        row.append(child.attrib.get('maximum'))
                    elif child.attrib.get('type') == 'HKQuantityTypeIdentifierDistanceWalkingRunning':
                        row.append(child.attrib.get('sum'))
                    elif child.attrib.get('type') == 'HKQuantityTypeIdentifierHeartRate':
                        row.append(child.attrib.get('average'))
                        row.append(child.attrib.get('minimum'))
                        row.append(child.attrib.get('maximum'))
            rows.append(row)
                    
    return pd.DataFrame(rows, columns = df_cols)


# def all_heart_rates(root) -> pd.DataFrame:
#     df_cols = []
#     rows = []
#     for node in root:
#         if node.tag == 'HeartRateBpm':
#             df_cols = node.attrib.keys()
#             rows.append(node.attrib.values())
    
#     out_df = pd.DataFrame(rows, columns = df_cols)
#     return out_df