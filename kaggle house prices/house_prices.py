# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:18:17 2018

@author: ARLETTE
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn import linear_model



dataset = pd.read_csv('train2.csv', delimiter = ',', index_col='Id', header=0)
datatest = pd.read_csv('test.csv', delimiter = ',', index_col='Id', header=0)
print(dataset.head(3))
print(dataset.columns)
print(dataset['SalePrice'].describe())

sns.set_color_codes()
sns.distplot(dataset['SalePrice'], color='g')



f,ax=plt.subplots(3,2, figsize=(10,10)) 
price = dataset.SalePrice.values
ax[0, 0].scatter(dataset['YearBuilt'].values, price)
ax[0, 0].set_title('YearBuilt')
ax[0, 1].scatter(dataset['TotalBsmtSF'].values, price)
ax[0, 1].set_title('TotalBsmtSF')
ax[1, 0].scatter(dataset['LotFrontage'].values, price)
ax[1, 0].set_title('LotFrontage')
ax[1, 1].scatter(dataset.GrLivArea.values, price)
ax[1, 1].set_title('GrLivArea')
ax[2, 0].scatter(dataset.LotArea.values, price)
ax[2, 0].set_title('LotArea')
ax[2, 1].scatter(dataset.GarageArea.values, price)
ax[2, 1].set_title('GarageArea')


# =============================================================================
# numeric: 'MSSubClass', 'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond','1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath',
#        'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr',
#        'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF'
#        
# =============================================================================
# =============================================================================
# not numeric:'MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities',
#        'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2',
#        'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
#        'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation',
#        'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
#        'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'GarageCars',
#        'GarageArea', 'TotRmsAbvGrd', 'Fireplaces', 'WoodDeckSF', 'OpenPorchSF',
#        'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
#        'MoSold', 'KitchenQual', 'Functional', 'FireplaceQu', 'GarageType',
#        'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive', 'PoolQC',
#        'Fence', 'MiscFeature', 'SaleType', 'SaleCondition'
# =============================================================================
# =============================================================================
# date:'YearBuilt',
#        'YearRemodAdd', 'GarageYrBlt', 'YrSold'
# =============================================================================

#print(dataset.corr())
corr_dataset = dataset.corr()
plt.figure(figsize=(20,15))
sns.heatmap(corr_dataset, annot=True)
corr_saleprice = corr_dataset['SalePrice'].sort_values(ascending = False)
#print(corr_saleprice)
dataset['YearBuilt']=pd.to_datetime(dataset.YearBuilt, format='%Y')
dataset['YrSold']=pd.to_datetime(dataset.YrSold, format='%Y')
dataset['YearRemodAdd']=pd.to_datetime(dataset.YearBuilt, format='%Y')
dataset['GarageYrBlt']=pd.to_datetime(dataset.YearBuilt, format='%Y')
dataset['YearRemodAdd']=pd.to_datetime(dataset.YearBuilt, format='%Y')

datatest['YearBuilt']=pd.to_datetime(dataset.YearBuilt, format='%Y')
datatest['YearRemodAdd']=pd.to_datetime(dataset.YearBuilt, format='%Y')
datatest['GarageYrBlt']=pd.to_datetime(dataset.YearBuilt, format='%Y')
datatest['YearRemodAdd']=pd.to_datetime(dataset.YearBuilt, format='%Y')


print("jgdkhkhgfhik", dataset['YrSold'].dtype)

current_day = pd.to_datetime('today')
    
    
def convert_data(dataset):
    current_day = pd.to_datetime('today')
    print(current_day)
    le = preprocessing.LabelEncoder()
    
    for col in dataset.columns:
        if dataset[col].dtype==object:
            #print(col, "object")
            dataset[col].fillna(value='None', inplace=True)
            dataset[col] = le.fit_transform(dataset[col])
        elif dataset[col].dtype==np.int64 or dataset[col].dtype==float:
            #print(col, "numeric")
            dataset[col].fillna(value =dataset[col].median() , inplace=True)
            dataset[col] = le.fit_transform(dataset[col])
        else :
            print(dataset[col].dtype)#==np.datetime:
            print("aaaaaaaaaaaaaaa", col, type(current_day), dataset[col].dtype)
            dataset[col] = current_day - dataset[col]
            #pd.cut(dataset[col],5)
            dataset[col] = le.fit_transform(dataset[col])
    return dataset
            

datatrain=convert_data(dataset)
print(datatrain)
                

            
                
        
      

