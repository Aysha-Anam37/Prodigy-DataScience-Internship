import pandas as pd
import matplotlib.pyplot as plt

data = {'Acc_ID': [1,2,3,4,5,6,7,8,9,10],
    'Weather': [
        'Rainy', 'Clear', 'Foggy', 'Rainy', 'Clear',
        'Foggy', 'Rainy', 'Clear', 'Foggy', 'Rainy'],
    'Road_Cond': [
        'Wet', 'Dry', 'Wet', 'Wet', 'Dry',
        'Slippery', 'Wet', 'Dry', 'Slippery', 'Wet'],
    'TimeOfDay': [
        'Night', 'Morning', 'Evening', 'Night', 'Afternoon',
        'Morning', 'Evening', 'Afternoon', 'Night', 'Morning'],
    'Location': [
        'Highway', 'City Center', 'Highway', 'Bridge', 'City Center',
        'Bridge', 'Highway', 'City Center', 'Bridge', 'Highway'],
    'Severity': [
        'High', 'Low', 'Medium', 'High', 'Low',
        'Medium', 'High', 'Low', 'Medium', 'High']}

df = pd.DataFrame(data)
print(df.head())

plt.figure(figsize=(8,6))
df['Weather'].value_counts().plot(kind='bar',color=['salmon', 'skyblue', 'purple'],
    edgecolor='black')
plt.title('Accidents by Weather Condition', fontsize=14)
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
df['Road_Cond'].value_counts().plot(kind='bar',color=['lightcoral', 'lightblue', 'lightgreen'],
    edgecolor='black')
plt.title('Accidents by Road Condition', fontsize=14)
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
df['TimeOfDay'].value_counts().plot(kind='bar',color=['lavender', 'skyblue', 'lightgreen', 'salmon'],
    edgecolor='black')
plt.title('Accidents by Time of Day', fontsize=14)
plt.xlabel('Time of Day')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
df['Location'].value_counts().plot(kind='bar',color=['salmon', 'skyblue', 'lightgreen'],
    edgecolor='black')
plt.title('Accident Hotspots by Location', fontsize=14)
plt.xlabel('Location')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()