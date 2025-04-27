import pandas as pd

def authenticate_user(username, password, role):
    try:
        df = pd.read_csv("data/credentials.csv")
        user = df[(df['username'] == username) & (df['password'] == password) & (df['role'] == role)]
        return not user.empty
    except FileNotFoundError:
        return False
