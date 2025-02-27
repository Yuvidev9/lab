# -*- coding: utf-8 -*-
"""08/01/25.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f2EhEvoQicXZvHDkoKIJN2ifjAEvkKML
"""

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

years = [[2015], [2016], [2017], [2018], [2019], [2020]]
values = [200, 220, 240, 260, 280, 300]

years_train, years_test, values_train, values_test = train_test_split(years, values, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(years_train, values_train)

future_year = [[2025]]
predicted_value = model.predict(future_year)
print(f"Predicted value for {future_year}: {predicted_value[0]}")

!sudo apt-get update && sudo apt-get upgrade -y

!pip install SpeechRecognition==3.10.0 pyttsx3==2.90 pyaudio==0.2.13

