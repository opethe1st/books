# Use Python 3.12 as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install the project and its dependencies
RUN pip install .

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
