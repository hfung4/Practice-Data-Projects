import numpy as np
import pandas as pd

'''scikit-learn'''
from sklearn.base import BaseEstimator, TransformerMixin

# Transformer to capture the elaspe time (in years) between a year variable and YrSold (when the house
# was sold)

# inherit the required parent classes from scikit-learn
class TemporalVariableTransformer(BaseEstimator, TransformerMixin):

    # constructor
    def __init__(self, variables, reference_variable):  # reference_variable is YrSold

        """Constructor

        Args:
            variables (List[str]): a list of year variable names
            reference_variable (str): name of the reference variable

        Returns:
            void
        """

        # Error handling: Do some sanity checks on the input parameter (it should be a list)
        if not isinstance(variables, list):
            raise ValueError('variables shold be a list')

        # set the attributes variables and reference_variable
        self.variables = variables  # a list of variables
        self.reference_variable = reference_variable

    # fit method
    def fit(self, X, y=None):
        """ Fit

        Args:
            X (DataFrame): a input dataframe of features to train the transformer
            y (DataFrame): a input Series of response variable to train the transformer (optional)

        Returns:
            self
        """
        # We don't need to learn any parameters for this transformer. Nonetheless, we still need
        # to include a fit method so that the Transformer class would be compatible to sklearn

        return self

    def transform(self, X):
        """ Transform

        Args:
            X (DataFrame): a input dataframe of features to be transformed

        Returns:
            X (DataFrame): the transformed Dataframe of features
        """

        # Make a copy of the input Dataframe of features to be transformed
        # so we won't overwrite the original Dataframe that was passed as argument
        X = X.copy()

        # Perform the transformation: df[var] = df[reference_variable] - df[var]
        for var in self.variables:
            X[var] = X[self.reference_variable] - X[var]

        return X


# Categorical variables encoding (the encoding of categorical variables that already have ordered
# levels from strings to numeric)

class Mapper(BaseEstimator, TransformerMixin):
    """
    Constructor

    Args:
        variables (List[str]): a list of variables to be recoded (specified by user)
        mappings (dict): a dictionary of mappings from old to new encoding

    Returns:
        void
    """

    def __init__(self, variables, mappings):

        # Error handling: check to ensure variables is a list
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')

        # Error handling: check to ensure variables is a dict
        if not isinstance(mappings, dict):
            raise ValueError('mapping should be a dictionary')

        # set attributes at instantiation of class
        self.variables = variables
        self.mappings = mappings

    def fit(self, X,
            y=None):  # need to have y as argument to make class compatible with sklearn pipeline
        """ Fit

        Args:
            X (DataFrame): a input dataframe of features to train the transformer
            y (DataFrame): a input Series of response variable to train the transformer (optional)

        Returns:
            self
        """
        # We don't need to learn any parameters for this transformer. Nonetheless, we still need
        # to include a fit method so that the Transformer class would be compatible to sklearn

        return self

    def transform(self, X):
        """ Transform

        Args:
            X (DataFrame): a input dataframe of features to be transformed

        Returns:
            X (DataFrame): the transformed Dataframe of features
        """

        # Make a copy of the input Dataframe of features to be transformed
        # so we won't overwrite the original Dataframe that was passed as argument
        X = X.copy()

        # Perform recoding of the levels of var
        for var in self.variables:
            X[var] = X[var].map(self.mappings)

        return X