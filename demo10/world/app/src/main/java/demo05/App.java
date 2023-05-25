package demo05;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.util.Collections;
import java.util.Properties;
import java.util.concurrent.Executors;

import static spark.Spark.*;

public class App {
    private static final String BOOTSTRAP_SERVERS = "kafka:9092";
    private static final String GROUP_ID = "test";
    private static final String ENABLE_AUTO_COMMIT = "true";
    private static final String AUTO_COMMIT_INTERVAL_MS = "1000";

    private static String currentTime = "unknown";

    public static void main(String[] args) {
        port(5001);
        before((request, response) -> 
            System.err.println(request.requestMethod() + " " + request.url()));

        Executors.newSingleThreadExecutor().submit(() -> {
            Properties props = new Properties();
            props.put("bootstrap.servers", BOOTSTRAP_SERVERS);
            props.put("group.id", GROUP_ID);
            props.put("enable.auto.commit", ENABLE_AUTO_COMMIT);
            props.put("auto.commit.interval.ms", AUTO_COMMIT_INTERVAL_MS);
            props.put("key.deserializer", StringDeserializer.class.getName());
            props.put("value.deserializer", StringDeserializer.class.getName());

            KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
            consumer.subscribe(Collections.singletonList("test"));

            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(100);
                for (ConsumerRecord<String, String> record : records) {
                    currentTime = record.value();
                }
            }
        });

        get("/world/:name", (req, res) -> "world/" + req.params(":name") + " " + currentTime);
        get("/:name", (req, res) -> req.params(":name") + " " + currentTime);
        get("/", (req, res) -> "world" + " " + currentTime);
    }
}
