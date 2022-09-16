# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model
import pandas as pd

def main():
    m, n = map(int, input().strip().split())
    
    #upackage x, y train
    df_list= [list(map(float, input().split())) for i in range(n)]
    df_train = pd.DataFrame(df_list)

    #input number of x_pred feature 
    q = int(input())
    
    #x_pred feature 
    df_list_pred = [list(map(float, input().split())) for i in range(q)]  
    df_pred = pd.DataFrame(df_list_pred)

    #train test split
    X_train, y_train = df_train.iloc[:, :m], df_train.iloc[:, m]
    #train
    model = linear_model.LinearRegression().fit(X_train, y_train)
    #predict
    y_pred = model.predict(df_pred)

    for num in y_pred:
        print(round(num, 2))

if __name__ == "__main__":
    main()