FROM python:3.11.5-bullseye

RUN apt update -y && apt install -y git nano

RUN git clone https://github.com/hasan-kayan/Material_Fetch.git /Material_Fetch

WORKDIR /Material_Fetch

RUN pip install --no-cache-dir tqdm requests

CMD ["python", "main.py"]