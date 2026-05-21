ARG AIRFLOW_VERSION="3.2.1"
ARG PYTHON_VERSION="3.11"
ARG AIRFLOW_IMAGE="apache/airflow:slim-${AIRFLOW_VERSION}-python${PYTHON_VERSION}"

FROM ${AIRFLOW_IMAGE}

USER root

RUN apt-get update -qq && \
    ACCEPT_EULA=Y apt-get upgrade -y && \
    ACCEPT_EULA=Y apt-get install -q=2 --yes --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH" && \
    mkdir -p /home/airflow/repositories && \
    /root/.local/bin/uv sync --no-dev --python "${PYTHON_VERSION}"
