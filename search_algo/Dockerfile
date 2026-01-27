# Use official lightweight Python 3.13 image
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from the local folder (search_algo) into the container
COPY . .

# Default command to run the benchmark
CMD ["python", "benchmark_sol.py"]
