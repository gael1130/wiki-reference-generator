# Step 1: Use an official Python runtime as a base image
FROM python:3.11-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Install Tkinter for GUI support
RUN apt-get update && apt-get install -y python3-tk

# Step 6: Run the GUI application
CMD ["python", "main.py"]
