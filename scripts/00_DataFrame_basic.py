import pandas as pd

def main():
    print("-- DataFrame Practice --")

    # 0. Import csv as pandas DataFrame(행, 렬 데이터)
    df = pd.read_csv("../datas/titanic/train.csv")

    # 1. Display the first 5 rows of the DataFrame
    print(df.head())
    print('-' * 50)
    # 2. Dataframe type -> pandas.DataFrame
    print(type(df))
    print('-' * 50)
    # 3. Shape of dataframe(rows, columns), tuple
    print(df.shape)
    print('-' * 50)
    # 4. Display the column names of the DataFrame
    print(df.columns)
    print('-' * 50)
    # 5. Display the index of the DataFrame
    print(df.index) # -> RangeIndex(start=0, stop=891, step=1)
    print('-' * 50)

    # 6. Display information about the DataFrame, including the number of non-null values and data types of each column
    print(df.info())
    print('-' * 50)

    # 7. Display summary statistics of the DataFrame, including count, mean, standard deviation, minimum, and maximum values for each column
    print(df.describe())
    print('-' * 50)

    # 8. DataFrame []연산자를 통해서 내부 칼럼명을 입력하면 -> Series 형태 특정 컬럼 데이터 세트 반환
    value_counts = df['Pclass'].value_counts()
    print(type(df['Pclass'])) # -> pandas.Series
    print(f"value_counts: {value_counts}") # -> 데이터 분포 확인.(컬럼 데이터용)
    print('-' * 50)

    # 9. value_counts() 메서드는 기본적으로 내림차순 정렬 & drop_na=True 옵션이 기본값으로 설정되어 있음.
    test_Embarked = df['Embarked'].value_counts()
    test_Embarked_na = df['Embarked'].value_counts(dropna=False)
    test_Embarked_sort = df['Embarked'].value_counts(ascending=True)
    print(f"test_Embarked: {test_Embarked}")
    print(f"test_Embarked_na: {test_Embarked_na}")
    print(f"test_Embarked_sort: {test_Embarked_sort}")
    print('-' * 50)

    # 10. Series 데이터 확인
    pclass = df["Pclass"]
    print(pclass.head())

    return

if __name__ == "__main__":
    main()