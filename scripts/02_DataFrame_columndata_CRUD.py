import pandas as pd


def main():
    df = pd.read_csv("../datas/titanic/train.csv")
    print("0. Input data")
    print(df.head(5))

    print("\n1. 컬럼추가하기: []연산자를 활용하여 바로 가능")
    print(f"Before: {df.columns}")
    df['added_col'] = '0'
    print(f"After: {df.columns}")

    print("\n2. 컬럼수정하기: []연산자를 활용하여 가능(0 -> 1)")
    print(f"Before --- \n{df['added_col'].head(5)}")
    df['added_col'] = '1'
    print(f"After --- \n{df['added_col'].head(5)}")
    df['added_col'] = '1'

    print("\n3. 컬럼수정하기2: 이미 있는 값을 통해서도 가능(Age 이용)")
    df['Age_by_10'] = df['Age'] * 10
    print(f"Age_by_10 from df['Age']")
    print(df[['Age', 'Age_by_10']].head(5))

    print("\n4. 컬럼값이용: 덧셈 연산도 이용하가능")
    df['Age+Age*10+1'] = df['Age'] + df['Age_by_10'] + 1
    print(df[['Age', 'Age_by_10', 'Age+Age*10+1']].head(5))

    print("\n5. 데이터삭제 - 컬럼삭제(Age_by_10삭제)")
    print(f"Before: {df.columns}")
    df_dropped = df.drop('Age_by_10', axis=1)
    print(f"After: {df_dropped.columns}")
    # cf) inplace=True를 하면 원본 dataframe이 변경된다. # cf) inplace=True는 폐기될 예정. 메모리 성능없지만. 버그는 나옴...
    # 아무래도 빅데이터에선 inplace과정에서 문제가 생길 것으로 판단.

    print("\n6. 데이터삭제 - 여러 컬럼삭제(Age, Age_by_10)")
    print(f"Before: {df.columns}")
    df_dropped2 = df.drop(['Age', 'Age_by_10'], axis=1)
    print(f"After: {df_dropped2.columns}")

    print("\n7. 데이터삭제 - row 기준 삭제(0~4번 row, 삭제 후 index 5번부터 존재)")
    print(f"Befroe: {df.head(5)}")
    df_drop_row = df.drop([0, 1, 2, 3, 4], axis=0)
    print(f"After: {df_drop_row.head(5)}")

    print("**cf) drop()은 일반적으론 컬럼값 삭제에 사용...!(경험적)")
    return

if __name__ == "__main__":
    main()