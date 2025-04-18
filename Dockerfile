FROM python:3.11
WORKDIR /Near_Earth_Object_Tracker
COPY requirements.txt /Near_Earth_Object_Tracker//
RUN pip install --no-cache-dir -r requirements.txt
COPY . /Near_Earth_Object_Tracker//
EXPOSE 8501
ARG API_KEY
ENV API_KEY=$API_KEY
CMD ["streamlit","run","app/NEA_Tracker.py"]
