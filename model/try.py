import pickle

model = pickle.load(open('model.pkl', 'rb'))

test = [0.03551,25.0,4.86,0,0.426,6.167,46.7,5.4007,4,281.0,19.0,390.64,7.51]

prediction = model.predict([test])

print(prediction)