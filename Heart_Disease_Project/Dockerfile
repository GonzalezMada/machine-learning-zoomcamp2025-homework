FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install dependencies from Pipfile.lock
RUN pipenv install --system --deploy

# Copy application files
COPY predict.py train.py ./
COPY model.bin ./

# Expose port
EXPOSE 9696

# Run the application with gunicorn
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]
