# Use the Python 3.9 base image
FROM python:3.9

# Copy the entire project into the Docker image
COPY . /app

# Set the working directory to the project directory
WORKDIR /app

# Install dependencies for each feature
RUN pip install -r crowd_analysis/requirements.txt
RUN pip install -r queue_management/requirements.txt
RUN pip install -r parking_analysis/requirements.txt
RUN pip install -r anomaly_detection/requirements.txt
RUN pip install -r heatmap/requirements.txt

# Expose any necessary ports
EXPOSE 8000

# Define the startup command for each feature
CMD ["python", "crowd_analysis/main.py"]
