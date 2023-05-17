package main

import (
	"fmt"
	"net/http"
	"time"
)

func timeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, time.Now().String())
}

func main() {
	http.HandleFunc("/", timeHandler)
	http.ListenAndServe(":5002", nil)
}
