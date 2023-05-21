package main

import (
	"context"
	"fmt"
	"log"
	"net/http"

	"github.com/segmentio/kafka-go"
)

func timeHandler(w http.ResponseWriter, r *http.Request) {
	kafkaReader := kafka.NewReader(kafka.ReaderConfig{
		Brokers:   []string{"kafka:9092"},
		Topic:     "test",
		Partition: 0,
		MinBytes:  10e3, // 10KB
		MaxBytes:  10e6, // 10MB
	})

	m, err := kafkaReader.ReadMessage(context.Background())
	if err != nil {
		log.Fatal(err)
	}
	fmt.Fprintf(w, string(m.Value))
	kafkaReader.Close()
}

func main() {
	http.HandleFunc("/", timeHandler)
	http.ListenAndServe(":5002", nil)
}
