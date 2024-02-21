FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r ./requirements.txt

# Install system dependencies for Chrome and xvfb
RUN apt-get update && \
    apt-get install -y wget xvfb gnupg gnupg2 gnupg1 && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Copy project
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Run the application
CMD ["uvicorn", "scraping_app.main:app", "--host", "0.0.0.0", "--port", "80"]