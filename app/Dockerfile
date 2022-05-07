FROM tiangolo/uvicorn-gunicorn-fastapi:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /code
# Install Poetry
RUN apt clean && apt update && apt install libsndfile1 ffmpeg libgstreamer1.0-0 libsndfile1 libgirepository1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-ugly -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \    
    poetry config virtualenvs.create false

# Copy poetry.lock.valid.invalid.invalid* in case it doesn't exist in the repo
COPY . /code/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"


ENV PYTHONPATH=/code
EXPOSE 8000
