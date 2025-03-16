FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONUNBUFFERED 1

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

RUN <<EOF
apt-get update 
apt-get install -y \
    build-essential \
    locales \
    libpq-dev \
    git \
    make \
    vim \
    sudo \
    net-tools \
    inetutils-ping \
    iproute2 \
    python3-setuptools \
    wget \
    sqlite3

locale-gen --purge C
dpkg-reconfigure --frontend noninteractive locales
EOF

COPY ../requirements.txt .

RUN <<EOF
pip install --upgrade pip
pip install -r requirements.txt
EOF


