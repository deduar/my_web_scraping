FROM python:3.9.4

RUN groupadd --gid 10100 deduar && \
    useradd --uid 10101 --system -m -d /home/deduar -g deduar deduar && \
    mkdir -p /app && \
    chown deduar:deduar /app

USER 10101

WORKDIR /app

RUN pip install --no-cache-dir --user -r requirements.txt

ENV PORT=9999 WORKERS=9 THREADS=3

# CMD gunicorn --log-file=- --access-logfile=- --bind 0.0.0.0:$PORT --chdir . launch:app -w $WORKERS --thread $THREADS --backlog 2048