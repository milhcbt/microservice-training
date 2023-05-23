package main

import (
	"context"
	"fmt"
	"time"

	"github.com/segmentio/kafka-go"
)

func main() {
	// Set up the Kafka writer.
	writer := kafka.NewWriter(kafka.WriterConfig{
		Brokers: []string{"kafka:9092"},
		Topic:   "test",
	})

	// Loop forever.
	for {
		// Send the current time to the Kafka topic.
		currentTime := time.Now().Format(time.RFC3339)
		err := writer.WriteMessages(context.Background(), kafka.Message{
			Key:   []byte("key"),
			Value: []byte(currentTime),
		})
		if err != nil {
			fmt.Printf("failed to write message: %v\n", err)
		}

		// Wait for one second before sending the next message.
		time.Sleep(10 * time.Second)
	}

	// Close the Kafka writer.
	err := writer.Close()
	if err != nil {
		fmt.Printf("failed to close writer: %v\n", err)
	}
}
