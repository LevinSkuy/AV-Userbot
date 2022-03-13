FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Av-Userbot https://github.com/Yansensad/AV-Userbot /home/Av-Userbot/ \
    && chmod 777 /home/Av-Userbot \
    && mkdir /home/Av-Userbot/bin/
WORKDIR /home/Av-Userbot/
COPY ./sample_config.env ./config.env* /home/Av-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
