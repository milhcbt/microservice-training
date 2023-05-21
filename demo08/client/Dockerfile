FROM busybox:latest
COPY index.html /var/www/index.html
EXPOSE 5003
CMD ["httpd", "-f", "-h", "/var/www", "-p", "5003"]