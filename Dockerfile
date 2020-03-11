FROM myubuntu
ADD . ~
WORKDIR ~
# RUN pip install -r requirements.txt
EXPOSE 80
ENV FLASK_APP hellow.py
ENV FLACK_ENV development
CMD ["flask", "run"]
