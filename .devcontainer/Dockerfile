FROM mcr.microsoft.com/devcontainers/universal:latest

# Copy requirements files from your project root to container
COPY req1.txt req2.txt /tmp/

# Install requirements during image build
RUN pip3 install -r /tmp/req1.txt && \
    pip3 install -r /tmp/req2.txt --no-deps && \
    rm /tmp/req1.txt /tmp/req2.txt
