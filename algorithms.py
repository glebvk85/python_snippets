from sklearn import cross_validation, svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import pylab as pl

%pylab inline


model_rfc = RandomForestClassifier(n_estimators=70, class_weight='balanced', random_state=42, n_jobs=-1, max_features= 'sqrt', max_depth=10, oob_score = True)
#model_rfc = RandomForestClassifier(n_estimators = 100, class_weight='balanced', max_features= 'sqrt') #в параметре передаем кол-во деревьев
model_knc = KNeighborsClassifier(n_neighbors = 5) #в параметре передаем кол-во соседей
model_lr = LogisticRegression(penalty='l2', tol=.01, C=1) 
model_svc = svm.SVC() #по умолчанию kernel='rbf'


%%time
pl.clf()
pl.figure(figsize=(8,6))

#SVC
#model_svc.probability = True
#probas = model_svc.fit(X_train, y_train).predict_proba(X_test)
#fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
#roc_auc  = auc(fpr, tpr)
#pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('SVC', roc_auc))

RandomForestClassifier
probas = model_rfc.fit(X_train, y_train).predict_proba(X_test)
fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
roc_auc  = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('RandomForest',roc_auc))

#KNeighborsClassifier
#probas = model_knc.fit(X_train, y_train).predict_proba(X_test)
#fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
#roc_auc  = auc(fpr, tpr)
#pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('KNeighborsClassifier',roc_auc))

#LogisticRegression
probas = model_lr.fit(X_train, y_train).predict_proba(X_test)
fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
roc_auc  = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('LogisticRegression',roc_auc))

pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.legend(loc=0, fontsize='small')
pl.show()