import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle

# Load dataset
data = pd.read_csv('train.csv')
data = data[['GrLivArea', 'YearBuilt', 'SalePrice']].dropna()

# Split data
X = data[['GrLivArea', 'YearBuilt']]
y = data['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, predictions))

# Save the model
with open('backend/model.pkl', 'wb') as file:
    pickle.dump(model, file)
