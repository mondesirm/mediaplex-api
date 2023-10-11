# Using python 3.9 as base image
FROM python:3.9

# Set the application directory
WORKDIR /api

# Copy dependencies file
COPY ./requirements.txt /api/requirements.txt

# Install requirements
RUN pip install psycopg2
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy necessary files (prone to change)
COPY ./.env /api/.env
COPY ./assets /api/assets
COPY ./main.py /api/main.py
COPY ./mediaplex /api/mediaplex

# Expose server port
EXPOSE 8000

# Define our command to be run when launching the container
CMD ["python", "main.py"]