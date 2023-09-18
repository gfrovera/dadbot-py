FROM ubuntu:20.04

ENV LANG=C.UTF-8

#updating and installing packages
RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        --no-install-recommends \
        software-properties-common \
    && add-apt-repository ppa:deadsnakes \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        --no-install-recommends \
        python3.11 \
        python3.11-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && :

# Config of workdir and project files

COPY requirements-dev.txt /tmp/
ENV PATH=/venv/bin:$PATH
RUN : \
    && python3.11 -m venv /venv \
    && pip install --no-cache-dir -r /tmp/requirements-dev.txt \
    && rm -rf /tmp/requirements-dev.txt \
    && :


# Config of workdir and project files
WORKDIR /dadbot

COPY . .

# When prod ready, implement and test this user config
# RUN : \
#     && useradd -ms /bin/bash user \
#     && chown -R user:user /dadbot \
#     && chmod +x main.py \
#     && :
# USER user