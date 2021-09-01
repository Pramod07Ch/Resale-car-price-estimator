#Using the base image with python 3.7
 FROM python:3.7
 
 WORKDIR /ML_flask_app 
  
 RUN pip install pandas scikit-learn flask gunicorn datetime numpy requests
 
 ADD ./models ./models
 
 ADD app.py app.py
 
 EXPOSE 5000 
 
 CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
