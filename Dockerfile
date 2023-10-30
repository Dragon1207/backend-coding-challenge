# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies files to the working directory
COPY pyproject.toml poetry.lock /app/

# Install Poetry and project dependencies
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application code to the working directory
COPY ./gistapi ./gistapi
COPY setup.cfg ./

EXPOSE 9876

# Start the Flask server when the container launches
CMD ["poetry", "run", "python", "gistapi/gistapi.py"]