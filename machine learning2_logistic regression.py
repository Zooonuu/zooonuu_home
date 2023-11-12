import numpy as np
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print(cancer.keys())
print("="*25)
print(cancer['feature_names'])
print(len(cancer['feature_names']))
print(cancer['target_names'])
print("="*25)
print('data shape:' ,cancer['data'].shape)
print('target shape:',cancer['target'].shape)
print("="*25)
print(cancer['data'][-2:])
print(cancer['target'][-2:])
print("="*25)

x=cancer['data']
y=cancer['target']

index = [i for i in range(x.shape[0])]
np.random.shuffle(index)
x= x[index]
y= y[index]

x_train, y_train = x[:400], y[:400]
x_test , y_test =x[400:] , y[400:]

print('train data:',x_train.shape , 'test data:', x_test.shape)
print('train target:',y_test.shape , 'test target:',y_test.shape) 

print("="*25)

w= 0.001 * np.random.randn(30)
b= 0.01 * np.random.randn(1)

def linear(x):
    return x.dot(w) + b

def sigmoid(x):
    return 1/ (1+np.exp(-x))

print()
def cross_entropy_error(p,y):
    delta = 1e-7
    return -np.average(y*np.log(p+delta) + (1-y)*np.log(1-p+delta))
print()
def numerical_gradient(f,theta):
    h = 1e-4
    grad=np.zeros_like(theta)
    
    for idx in range(theta.size):
        tmp_val = theta[idx]
        
        theta[idx]=tmp_val + h
        fxh1 = f(theta)
        
        theta[idx]=tmp_val - h
        fxh2 = f(theta)
        
        grad[idx] = (fxh1- fxh2) / (2*h)
        
        theta[idx] =tmp_val 
        
    return grad 
print()
num_epoch= 22000
learning_rate= 0.00003

for epoch in range(num_epoch):
    w= w- learning_rate * numerical_gradient(lambda w: cross_entropy_error(sigmoid(linear(x_train)) , y_train),w)
    b= b- learning_rate * numerical_gradient(lambda b: cross_entropy_error(sigmoid(linear(x_train)) , y_train),b)

    pred= sigmoid(linear(x_train))
    loss=cross_entropy_error(pred, y_train)
    
    if epoch % 1000 == 0:
        print("{0} epoch, train_loss={1}".format(epoch,loss))
print("="*25)
pred = sigmoid(linear(x_test))
loss = cross_entropy_error(pred,y_test)
print("{0} epoch, test loss= {1}".format(epoch,loss))
print("="*25)


from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

pred = [0.0 if p<0.5 else 1.0 for p in pred]

conf_matrix  = confusion_matrix(y_test,pred)
print(conf_matrix)

class_report = classification_report(y_test,pred)
print(class_report) 
print()

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
print()
cancer = load_breast_cancer()
x=cancer['data']
y=cancer['target']

x_train, x_test , y_train,y_test = train_test_split(x,y,test_size=0.297)
print('train data:',x_train.shape , 'test data:',x_test.shape)
print('train target:',y_train.shape, 'test target:',y_test.shape)

print()
regression = LogisticRegression()
regression.fit(x_train, y_train)

pred = regression.predict(x_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

conf_matrix=confusion_matrix(y_test,pred)
print(conf_matrix)

class_report = classification_report(y_test, pred)
print(class_report)
print("="*25)
