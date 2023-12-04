import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from power_predict.logic.data import load_local_df
#from sklearn.externals import joblib



def run_linear_regression_model():
    df = load_local_df()

    # Preprocessing
    final = df
    columns_X = [col for col in final.columns if 'value' in col]

    if not columns_X:
        raise ValueError("No columns with 'value' in their names.")

    X = final[columns_X]
    columns_to_drop = ['value_CDD_18', 'value_CDD_21', 'value_HDD_16', 'value_HDD_18', 'value_Heat_index']
    X = X.drop(columns=columns_to_drop)

    # Feature scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Here you can choose which technology output to predict
    #y = final['total_sol_wind_hyd']
    #y = final['Solar']
    y = final['Wind']
    # y = final['Hydro']

    # Split training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Linear regression model
    model = LinearRegression()

    # Print the model type
    print('Model Type: Linear Regression')

    # Fit
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    cod = r2_score(y_test, y_pred)

    print(f'Mean Absolute Error: {mae}')
    print(f'Mean Squared Error: {mse}')
    print(f'Coefficient of Determination (COD): {cod}')
    print(f'R-squared: {r2}')

    return model

#save_model(run_linear_regression_model, 'Linear Regression')

#def save_model(model, model_type):
    model_filename = f'{model_type}_model.joblib'
    joblib.dump(model, model_filename)
    print(f'Model saved as: {model_filename}')

# Run the linear regression model and save it
#linear_regression_model = run_linear_regression_model()
#save_model(linear_regression_model, 'Linear Regression')
run_linear_regression_model()
