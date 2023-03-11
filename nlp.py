import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Load data from CSV
df = pd.read_csv('interview_scripts.csv')

# Split data into input (interview script) and output (win/loss)
texts = df['text'].values.astype('U')
labels = df['label'].values.astype('int32')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42)

# Preprocess input data
tfidf = TfidfVectorizer(lowercase=True, stop_words='english', max_df=0.7)
X_train_tfidf = tfidf.fit_transform(X_train).toarray()
X_test_tfidf = tfidf.transform(X_test).toarray()

# Build Keras sequential model
model = Sequential()
model.add(Dense(128, input_shape=(X_train_tfidf.shape[1],), activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])

# Train model
history = model.fit(X_train_tfidf, y_train, epochs=5,
                    batch_size=32, validation_data=(X_test_tfidf, y_test))
