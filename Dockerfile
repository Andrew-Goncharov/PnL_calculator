FROM python:3.9-alpine

WORKDIR PnL_calculator

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt