FROM ubuntu
RUN apt update && apt install python3 -y
COPY jab.py .
CMD python3 jab.py
