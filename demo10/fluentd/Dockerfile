# Use the official fluentd image
# FROM fluent/fluentd:v1.14-1

FROM fluent/fluentd
RUN gem install elasticsearch -v 7.10.1
RUN gem install fluent-plugin-elasticsearch
RUN gem install fluent-plugin-rewrite-tag-filter
RUN gem install fluent-plugin-multi-format-parser


# Copy the fluent.conf file to the container
COPY ./conf/fluent.conf /fluentd/etc/

# Install the fluent-plugin-elasticsearch gem
RUN fluent-gem install --user-install fluent-plugin-elasticsearch

# Expose port 24224 for forward protocol
EXPOSE 24224

# Run the fluentd command
CMD ["fluentd", "-c", "/fluentd/etc/fluent.conf"]
