from sklearn.preprocessing import MinMaxScaler# Импортируем нормализацию от scikit-learn
from sklearn.preprocessing import StandardScaler # Импортируем стандартизацию от scikit-learn
from sklearn.preprocessing import PowerTransformer  # Степенное преобразование от scikit-learn



# предварительная обработка категориальных признаков
from sklearn.preprocessing import OneHotEncoder# Импортируем One-Hot Encoding от scikit-learn
from sklearn.preprocessing import OrdinalEncoder# Импортируем Порядковое кодированиеот scikit-learn

from sklearn.compose import ColumnTransformer # т.н. преобразователь колонок

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline # Pipeline.Не добавить, не убавить


def num_pipes(num_columns: list):

    result = []

    for cat in num_columns:

        column_name = f'num_{cat}'
        pipe = Pipeline([
            ('scaler', StandardScaler())
        ])

        pre_result = (column_name, pipe, cat)
        result.append(pre_result)
    
    return result

def cat_pipes(cat_columns: list):

    result = []

    for cat in cat_columns:

        column_name = f'cat_{cat}'
        pipe = Pipeline([
            ('encoder', OneHotEncoder(drop='if_binary', handle_unknown='ignore', sparse_output=False))
        ])

        pre_result = (column_name, pipe, cat)
        result.append(pre_result)
    
    return result


# Сделаем отдельно Pipeline с числовыми признаками
