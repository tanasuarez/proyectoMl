from modeltools.preprocessing import get_numerical_features
import pandas as pd

""""""


def test_get_numerical_features_simple():
    """
    En este test vamos a probar que logra distinguir
    entre cadenas de textos y numeros de entero
    """
    # assert es "como un if" pero que falla si la condición es falsa.

    
    df = df = pd.DataFrame({
        "numerica" : [5],
        "categorica" : ["rojo"]
    })

    assert get_numerical_features(df) == ["numerica"]

def test_get_numerical_features_empty():
    df = df = pd.DataFrame({
        "numerica" : [5],
        "categorica" : ["rojo"]
    })
    """Este test comprueba que se devuelve una lista vacía si no hay ninguna variable num."""
    assert not get_numerical_features(df).empty

def test_get_numerical_features_zero_columns():

    """Este test comprueba que se devuelve una lista vacía si el dataframe no tiene ninguna columna."""
    
    df = pd.DataFrame({})
    assert get_numerical_features(df).empty




def test_get_numerical_features_zero_rows():

    """Este test comprueba que se devuelve una con una variable si el DF

    tiene una variable numérica pero NINGUNA FILA."""
    df = pd.DataFrame({
        "numerica" : pd.Series(dtype=int)
    })

    assert get_numerical_features(df) == ["numerica"]





