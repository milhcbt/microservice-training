FROM consul:latest

# Copy the configuration file
COPY ./config.json /config.json

# Copy a script that will run consul and import configuration
COPY ./start.sh start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
