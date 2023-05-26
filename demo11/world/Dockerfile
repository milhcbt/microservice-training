# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Update the package list and install curl for testing
RUN apt-get update && apt-get install -y --no-install-recommends curl

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV NAME World
ENV FLASK_APP world.py

# Run app.py when the container launches
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5001"]
