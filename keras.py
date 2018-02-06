from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils


countries = data['country'].unique()
data['country'] = pd.Categorical(data['country'], categories=countries)
data['country'] = data['country'].cat.codes

data.drop(['drop_column_name'], axis=1)

from sklearn import cross_validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.3, random_state=42)

X_train.sample(frac=1)

Y_train = np_utils.to_categorical(y_train, len(y.unique()))
Y_test = np_utils.to_categorical(y_test, len(y.unique()))


from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
from keras.callbacks import EarlyStopping

%%time

early_stopping_monitor = EarlyStopping(patience=5)
X_train_, X_val, y_train_, y_val = cross_validation.train_test_split(X_train, y_train, test_size=0.2, random_state=42)
Y_train = np_utils.to_categorical(y_train_, len(y.unique()))
Y_val = np_utils.to_categorical(y_val, len(y.unique()))

model = Sequential()
model.add(Dense(400, input_dim=X_train_.shape[1], activation="relu", kernel_initializer="normal"))
model.add(Dropout(0.4))
model.add(Dense(400, activation="relu", kernel_initializer="uniform"))
model.add(Dense(400, activation="relu", kernel_initializer="uniform"))
model.add(Dropout(0.4))
model.add(Dense(400, activation="relu", kernel_initializer="uniform"))
model.add(Dense(400, activation="relu", kernel_initializer="uniform"))
model.add(Dense(400, activation="relu", kernel_initializer="uniform"))
model.add(Dropout(0.4))
model.add(Dense(400, activation="relu", kernel_initializer="uniform"))
model.add(Dense(400, activation="relu", kernel_initializer="uniform"))
model.add(Dense(400, activation="relu", kernel_initializer="uniform"))

model.add(Dense(len(y.unique()), activation="softmax", kernel_initializer="uniform"))
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(numpy.array(X_train_), numpy.array(Y_train), batch_size=1500, epochs=400, validation_split=0.2, verbose=0, callbacks=[plot,early_stopping_monitor])


scores = model.evaluate(numpy.array(X_val), numpy.array(Y_val), verbose=0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))


predict = model.predict_proba(numpy.array(X_val))

tp = 0
fp = 0
tn = 0
fn = 0
for i in zip(predict, y_val):
    if i[1] == 1:
        if i[0][1] > 0.5:
            tp += 1
        else:
            fn += 1
    else:
        if i[0][1] > 0.5:
            fp += 1
        else:
            tn += 1
print("good", tp)
print("error first type", fp)
print("bad", tn)
print("error second type", fn)
len(y_val)


model_json = model.to_json()
# Записываем модель в файл
json_file = open("sale_model.json", "w")
json_file.write(model_json)
json_file.close()
model.save_weights("sale_model.h5")


from keras.models import model_from_json
# Загружаем данные об архитектуре сети из файла json
json_file = open("sale_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
# Создаем модель на основе загруженных данных
loaded_model = model_from_json(loaded_model_json)
# Загружаем веса в модель
loaded_model.load_weights("sale_model.h5")

# Компилируем модель
loaded_model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
# Проверяем модель на тестовых данных
scores = loaded_model.evaluate(X_test, Y_test, verbose=0)
print("Точность модели на тестовых данных: %.2f%%" % (scores[1]*100))