FROM python:3.11

WORKDIR /app

# Copy app files and requirements
COPY app.py example_data.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Flask environment
ENV FLASK_APP=app.py

# Start Flask app on port 4999
CMD ["flask", "run", "--host=0.0.0.0", "--port=4999"]

EXPOSE 4999