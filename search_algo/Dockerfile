# Use official Python 3.13 slim image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies if needed (currently none)
# RUN pip install -r requirements.txt

# Default command to run benchmark
CMD ["python", "search_algo/benchmark_sol.py"]
