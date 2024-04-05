#Python Version
FROM python:3.9

#Creating a working directory
WORKDIR /user_app

#Adding the requirement.txt file
COPY ./requirements.txt /user_app 

#Installing all the requirements
RUN pip install --no-cache-dir -r requirements.txt

#Adding all the files into docker
COPY . .

#Setting flask ENV
ENV FLASK_APP=app.py

#Running the file
CMD ["python", "app.py", "--host", "0.0.0.0"]