import pandas as pd 
import random
i=1
sample_num=100

data=pd.DataFrame(columns=['Age','Chest pain', 'Fever', 'Persistent cough', 'Fatigue',
                            'Night sweats','Loss of appetite','Weight loss',
                            'Shortness of breath', 'Diagnosis'])#excel columns

while i<=sample_num:#columns datas generation
    for num in range(sample_num):
        age=random.randint(18, 70)
        chest_pain=random.choice(['Yes', 'No'])
        fever=random.choice(['Yes', 'No'])
        persistent_cough=random.choice(['Yes', 'No'])
        fatigue=random.choice(['Yes', 'No'])
        night_sweats=random.choice(['Yes', 'No'])
        loss_of_appetite=random.choice(['Yes', 'No'])
        weight_loss=random.choice(['Yes', 'No'])
        shortness_of_breath=random.choice(['Yes', 'No'])
        diagnosis=random.choice(['Healthy', 'Tuberculosis(TB)'])
        data=data._append({'Age':age,'Chest pain':chest_pain, 'Fever':fever,
                            'Persistent cough':persistent_cough,
                              'Fatigue':fatigue,'Night sweats':night_sweats,'Loss of appetite':loss_of_appetite,
                               'Weight loss':weight_loss,'Shortness of breath':shortness_of_breath, 'Diagnosis':diagnosis},ignore_index=True)
        
    i=i+1
    
data.to_csv('TB_data.csv', index=False)