'''ref:https://www.hackerrank.com/challenges/predicting-house-prices/problem'''
from sklearn import linear_model
import numpy as np
from numpy.linalg import inv

def mathsmethod(x,y,t):
    xt=x.transpose()
    xtx=np.dot(xt,x)
    # print('xtx',xtx)
    xtx_1= inv(xtx)
    # print('xtx_1',xtx_1)
    xty= np.dot(xt,y)
    # print('xty',xty)
    beta= np.dot(xtx_1,xty)
    print('Coefficients',beta)
    prediction=np.dot(beta.transpose(),t.transpose())
    #shorter method
    # coef=inv( x.transpose ().dot ( x ) ).dot ( x.transpose () ).dot ( y )
    # print('coef',coef)
    for pred in prediction.transpose():
        print(pred[0])
    return
def sklearnmethod(x,y,t):
    model= linear_model.LinearRegression().fit(x,y)
    print(model.coef_)
    prediction=model.predict(t)
    for pred in prediction:
        print(pred[0])

    return


if __name__=='__main__':
    s=np.array([[0.18,0.89,109.85] ,[1.0,0.26,155.72 ],
               [0.92 ,0.11 ,137.66 ] ,[0.07 ,0.37, 76.17],[ 0.85 ,0.16 ,139.75],
                [0.99, 0.41 ,162.6], [0.87 ,0.47 ,151.77]])
    t=np.array([[0.49, 0.18], [0.57, 0.83 ], [0.56, 0.64] ,[0.76 ,0.18]])
    x= s[:,:2]
    y = np.reshape ( s[:, -1], (len ( x ), 1) )
    #mathematics
    mathsmethod(x,y,t)
    sklearnmethod(x,y,t)









