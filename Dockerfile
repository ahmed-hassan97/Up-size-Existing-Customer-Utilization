FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

RUN echo "uwsgi_read_timeout 600s;" > /etc/nginx/conf.d/custom_timeout.conf

COPY ./requirements.txt /var/www/requirements.txt

RUN pip install -r /var/www/requirements.txt
