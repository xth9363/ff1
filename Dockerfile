FROM myubuntu
WORKDIR ~
ADD requirements.txt requirements.txt
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
ADD ./ ./
EXPOSE 8000
ENV FLASK_APP hello.py
ENV FLASK_ENV development
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8000"]
