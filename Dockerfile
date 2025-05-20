# Use official Python base image
FROM python:3.10-slim

# thiết lập thư mục làm việc
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Start the app
CMD ["python", "app1.py"]




