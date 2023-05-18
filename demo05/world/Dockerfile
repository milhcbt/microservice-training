# Dockerfile
FROM gradle:8.1-jdk17-alpine AS build

WORKDIR /home/gradle/src

# Copy local code to the container image.
COPY . .

# Build a release artifact.
RUN gradle clean shadowJar --no-daemon

FROM eclipse-temurin:17-jdk-jammy

WORKDIR /app

# Copy the jar to the production image from the builder stage.
COPY --from=build /home/gradle/src/app/build/libs/*.jar /app/app.jar

# Run the web service on container startup.
CMD ["java", "-jar", "/app/app.jar"]
