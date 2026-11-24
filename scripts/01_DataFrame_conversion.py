import numpy as np
import pandas as pd 

def main():
    # DataFrame과 리스트, 딕셔너리, 넘파이 ndarray, 시리즈 등 다양한 데이터 구조를 상호 변환할 수 있음.
    df = pd.read_csv("../datas/titanic/train.csv")

    # 1. From 넘파이ndarray, 리스트, 딕셔너리 -> DataFrame
    print("--- From 넘파이ndarray, 리스트, 딕셔너리 -> DataFrame ---")
    # 1) list, ndarray -> DataFrame
    print("\n0) Input list, array")
    list1 = [1, 2, 3]
    array1 = np.array(list1)
    print(f"list1   : {list1}")
    print(f"list1_type  : {type(list1)}")
    print(f"array1  : {array1}")
    print(f"array1_type : {type(array1)}")
    print("\n1) 예제1. list -> DataFrame | 컬럼지정없이")
    df_from_list_without_col = pd.DataFrame(list1)
    print(df_from_list_without_col) # column명이 자동으로 들어감. 0
    print("list를 DataFrame으로 변환가능(컬럼명이 0으로 자동으로 들어감을 확인할 수 있음)")

    print("\n2) 예제2. list -> DataFrame | 컬럼지정있이")
    cols = ['col1']
    df_from_list_with_col = pd.DataFrame(list1, columns=cols)
    print(df_from_list_with_col)
    print("컬럼명이 cols로 들어감. columns 인자에 list로 컬럼 이름을 정해넣어줘야함")
    
    print("\n3) 예제3. ndarray -> DataFrame")
    df_from_array_with_col = pd.DataFrame(array1, columns=cols)
    print(df_from_array_with_col)
    print("ndarray를 DataFrame으로 변환가능")

    # 2) dict -> DataFrame
    print("\n4) 예제4. dict -> DataFrame")
    dict1 = {'col1': [1, 2], 'col2': ["ww", 4], 'col3': [11, 31]}
    print(type(dict1))
    df_from_dict = pd.DataFrame(dict1)
    print(df_from_dict)
    print("Key는 컬럼명으로, value는 리스트 형(또는 ndarray) 칼럼 데이터로 매핑")

    print("+ 컬럼 value input에 따라서 각 컬럼 series의 dtype이 바뀐다.")
    print(f"* df_from_dict['col1'].dtype: {df_from_dict['col1'].dtype}")
    print(f"* df_from_dict['col2'].dtype: {df_from_dict['col2'].dtype}")
    print(f"* df_from_dict['col3'].dtype: {df_from_dict['col3'].dtype}")
    print(df_from_dict.info())

    # 2. DataFrame -> 넘파이 ndarray, 리스트, dict
    print("\n\n--- From DataFrame -> 넘파이 ndarray, list, dict ---")
    # 1) DataFrame -> ndarray
    print("1) 예제1. DataFrame -> ndarray (df.values, 속성값임을 기억)")
    array_from_df = df_from_dict.values
    print("array_from_df는 아래와 같다.")
    print(array_from_df)
    print(f"array shape: {array_from_df.shape}")
    print(f"array_from_df type: {type(array_from_df)}")

    # 2) DataFrame -> list (ndarray를 거쳐서 진행)
    print("\n2) 예제2. DataFrame -> list (df.values.tolist(), ndarray로 변환 후, tolist() 메서드를 사용)")
    list_from_df = df_from_dict.values.tolist()
    print(list_from_df)
    print(type(list_from_df))

    # 3) DataFrame -> dict (바로 dict로 변환)
    print("\n3) 예제3. DataFrame -> dict (df.to_dict() 메서드로 바로 수행)")
    dict_from_df = df_from_dict.to_dict()
    print(dict_from_df)
    print(type(dict_from_df))
    return

if __name__ == "__main__":
    main()