# Import the necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load the event data
event_data = pd.read_csv('event_data.csv')

# Preprocess the data
label_encoder = LabelEncoder()
event_data['Event_Type'] = label_encoder.fit_transform(event_data['Event_Type'])
event_data['Location'] = label_encoder.fit_transform(event_data['Location'])
event_data['Attended'] = label_encoder.fit_transform(event_data['Attended'])

# Split the data into features and target
features = event_data[['Event_Type', 'Location']]
target = event_data['Attended']

# Create and train the random forest classifier model
rf_model = RandomForestClassifier()
rf_model.fit(features, target)

# Define a function to get event recommendations based on previous events attended
def get_event_recommendations(previous_events):
    # Preprocess the previous events
    previous_events = label_encoder.transform(previous_events)
    
    # Predict the attendance of all events
    event_predictions = rf_model.predict(features)
    
    # Get the indices of recommended events that were not attended
    recommended_indices = [i for i, prediction in enumerate(event_predictions) if prediction and i not in previous_events]
    
    # Get the recommended event details
    recommendations = event_data.iloc[recommended_indices][['Event_Name', 'Event_Date', 'Location']]
    
    return recommendations

# Example usage
recommendations = get_event_recommendations(previous_events)
