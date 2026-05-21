ARG PYTHON_VERSION="3.11"

FROM python:${PYTHON_VERSION}-slim-trixie AS base

# Builder
FROM base AS builder

ARG OPENCVE_REPOSITORY="https://github.com/opencve/opencve.git"
ARG OPENCVE_VERSION="master"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update -qq && \
    apt-get upgrade -y && \
    apt-get install -q=2 --yes --no-install-recommends git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app

ENV PATH="/root/.local/bin:$PATH"
ENV PATH="/app/venv/bin:$PATH"

RUN git clone --depth 1 -b "${OPENCVE_VERSION}" --single-branch "${OPENCVE_REPOSITORY}" && \
    uv venv /app/venv && \
    uv sync --no-dev --python "${PYTHON_VERSION}"

# OpenCVE Image
FROM base

ARG OPENCVE_REPOSITORY
ARG GUNICORN_CMD_ARGS

LABEL name="opencve"
LABEL maintainer="dev@opencve.io"
LABEL url="${OPENCVE_REPOSITORY}"

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -q=2 --yes --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/ /app/

ENV PATH="/app/venv/bin:$PATH"
ENV GUNICORN_CMD_ARGS="${GUNICORN_CMD_ARGS}"

WORKDIR /app/opencve/web/

EXPOSE 8000

ENTRYPOINT ["gunicorn", "opencve.wsgi"]
CMD ["-b" ,"0.0.0.0:8000"]
