FROM python:3

WORKDIR /usr/src/app

COPY . .
#COPY ./CMPTestAutomation/requirements.txt ./
#COPY ./CMPTestAutomation/setup.py ./
RUN ls 
WORKDIR /usr/src/app/CMPTestAutomation
RUN ls 
RUN python setup.py install
RUN pip install --no-cache-dir -r requirements.txt
