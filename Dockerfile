#Using the base image with python 3.7
 FROM python:3.7
 
 WORKDIR /app 
  
 RUN pip install pandas scikit-learn==0.21.3 flask gunicorn datetime numpy requests sklearn
 
 ADD ./models ./models
 
 ADD server.py server.py
 
 EXPOSE 5000 
 
 CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"] 
