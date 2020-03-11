FROM myubuntu
ADD . ~
WORKDIR ~
RUN pip3 install -r requirements.txt
EXPOSE 80
ENV FLASK_APP hellow.py
ENV FLACK_ENV development
CMD ["flask", "run"]
