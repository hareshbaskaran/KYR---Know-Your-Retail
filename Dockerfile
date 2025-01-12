FROM ubuntu:latest
LABEL authors="haresh"

ENTRYPOINT ["top", "-b"]