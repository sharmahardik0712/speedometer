# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code into the container
COPY . .

# Copy the speed_data.db into the container
COPY speed_data.db /app/speed_data.db

# Expose the port on which your Flask app runs (e.g., 5000)
EXPOSE 5000

# Command to run the Flask app when the container starts
CMD ["python", "app.py"]
