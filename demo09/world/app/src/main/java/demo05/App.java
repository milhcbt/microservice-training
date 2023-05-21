package demo05;

import static spark.Spark.*;
import org.apache.kafka.clients.admin.AdminClient;
import org.apache.kafka.clients.admin.NewTopic;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Collections;
import java.util.Properties;

public class App {
    public static String kafkaServer = "kafka:9092";

    private static KafkaProducer<String, String> createProducer() {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,kafkaServer);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        return new KafkaProducer<>(props);
    }

    private static void createTopic(String topicName, int numPartitions, short replicationFactor) {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, kafkaServer);
        try (AdminClient client = AdminClient.create(props)) {
            client.createTopics(Collections.singletonList(new NewTopic(topicName, numPartitions, replicationFactor)));
        }
    }

    public static void main(String[] args) {
        final KafkaProducer<String, String> producer = createProducer();
        final String topicName = "test";
        createTopic(topicName, 1, (short)1);

        port(5001);
        before((request, response) -> 
            System.err.println(request.requestMethod() + " " + request.url()));

        get("/world/:name", (req, res) -> {
            String msg = req.params(":name");
            producer.send(new ProducerRecord<String, String>(topicName, msg));
            return msg;
        });

        get("/:name", (req, res) -> {
            String msg = req.params(":name");
            producer.send(new ProducerRecord<String, String>(topicName, msg));
            return msg;
        });

        get("/", (req, res) -> {
            String msg = "world";
            producer.send(new ProducerRecord<String, String>(topicName, msg));
            return msg;
        });

        // Close producer on application stop
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            producer.close();
        }));
    }
}
