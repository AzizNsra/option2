FROM python:3.8-slim-buster
WORKDIR /Python
COPY . .
RUN pip3 install -r requirement.txt
CMD ["python", "seeds_lda.py"]
