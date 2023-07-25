FROM python:3.11-slim as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install dependencies
FROM base as py-deps

# install python dependices
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM py-deps as runtime

# Create and switch to a new user
RUN useradd --create-home appdev
WORKDIR /home/appdev/appbackend
USER appdev

# copy over source code
COPY . .

EXPOSE 8000

# Run the application
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "app.main:app"]