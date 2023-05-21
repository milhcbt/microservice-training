# Start from the latest golang base image
FROM golang:1.20

# Add Maintainer Info
LABEL maintainer="iman <iman4hakim@gmail.com>"

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy go mod and sum files
COPY go.mod go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source from the current directory to the Working Directory inside the container
COPY . .

# Build the Go app
RUN go build -o main .

# Expose port 5002 to the outside
EXPOSE 5002

# Command to run the executable
CMD ["./main"]
