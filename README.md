# Hyperparameter-tuning-LIBSVM
LIBSVM is a c++ library developped by Chih-Chung Chang and Chih-Jen Lin that allows to do support vector machine (aka SVM) classification and regression. It solves C-SVM classification, nu-SVM classification, one-class-SVM, epsilon-SVM regression, and nu-SVM regression. It also provides an automatic model selection tool for C-SVM classification.

+ [You can have a look at the practical guide of LIBSVM here](https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf)
+ [You can download the LIBSVM software from here](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)

The intended use to show that SVM can acquire results rapidly, when compared to neural networks. So, in this program, we used the sotware in solving machine learning data-set problems like: 
+ Two Spiral Problem (classification)
+ [Abalone Age Problem (Regression)](http://archive.ics.uci.edu/ml/datasets/Abalone)
+ [SPECT Heart Diagnosis Problem (classification)](https://archive.ics.uci.edu/ml/datasets/spect+heart)

The data-sets can be obtained in dataset file.

## A glimpse of LIBSVM usage:

#### \windows>svm-scale -l -1 -u 1 data3-AMTrain.txt > data3-AMTrain.scale
#### \windows>svm-scale -l -1 -u 1 data3-AMTest.txt > data3-AMTest.scale
#### \windows>svm-train -s 0 -t 2 -c 1 -g 1 data3-AMTrain.scale data3.model
optimization finished, #iter = 325 \
nu = 0.394987
obj = -77.856661, rho = -0.912130
nSV = 242, nBSV = 75
Total nSV = 242
#### \windows>svm-predict data3-AMTest.scale data3.model data3.output
Accuracy = 40% (20/50) (classification)
