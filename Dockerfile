FROM python:3.9-slim

# install require OS packages
# we use apt-get instead of apt because of the stable CI
RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential gcc curl && apt-get install ffmpeg libsm6 libxext6  -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    pip3 install --upgrade pip

# define and create working directory
WORKDIR /usr/application

# install required python packages
# copy step is done separately to not reinstall the python packages when the code changes
COPY /requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# specify command to start the container
ENV PYTHONUNBUFFERED=TRUE

# copy the files inside the working directory (the .gitignore file ignores the not necessary files)
COPY / .

# Specify command to start the container
CMD ["python3", "rest_api.py"]
