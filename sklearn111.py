from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
x,y =make_blobs(n_samples=10, n_features=2, centers=2,random_state=0)
#import sklearn
print(x)
print(y)

# scikit-learn 機器學習的套件，包含內建的分群分類計算、回歸、統計等功能
from sklearn import datasets

# 載入我們會用到的模型，線性回歸模型
from sklearn.linear_model import LinearRegression

# 載入切分資料集成訓練集及測試集的套件，train_test_split   將訓練集和測試集分開
from sklearn.model_selection import train_test_split

# 載入驗證模型的套件，mean_square_error
# 均方誤差（Mean squared error，簡稱:MSE），數值越小，說明預測模型具有更好的精確度
from sklearn.metrics import mean_squared_error