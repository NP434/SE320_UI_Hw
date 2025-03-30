FROM python:3.11
WORKDIR /SE320_UI_Hw
COPY requirements.txt /SE320_UI_Hw/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /SE320_UI_Hw/
EXPOSE 8501
ENV API_KEY=JH0VtLf0h1f09mfXTbCyNRooHKLWQZIVmjHXmCG1
CMD ["streamlit","run","app/NEA_Tracker.py"]