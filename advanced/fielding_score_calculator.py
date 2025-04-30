# fielding_score_calculator.py

import pandas as pd

# Load the Excel file
df = pd.read_excel("cricket_fielding_analysis.xlsx")

# Define weights for Pick Types
weights = {
    'CP': 5,    # Clean Pick
    'GT': 4,    # Good Throw
    'C': 6,     # Catch
    'DC': -4,   # Dropped Catch
    'ST': 7,    # Stumping
    'RO': 8,    # Run Out
    'MRO': -3,  # Missed Run Out
    'DH': 6     # Direct Hit
}

# Calculate performance score
players = df['Player Name'].unique()
print("\n🎯 Fielding Performance Scores:")

for player in players:
    PS = 0
    data = df[df['Player Name'] == player]
    
    for event in data['Pick Type']:
        if event in weights:
            PS += weights[event]
    
    # Include Runs Saved/Conceded
    PS += data['Runs'].sum()
    
    print(f"{player}: {PS}")
