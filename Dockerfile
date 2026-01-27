FROM eclipse-temurin:17-jdk-jammy

WORKDIR /app

COPY java/SearchAlgorithmsComparison.java .

RUN javac SearchAlgorithmsComparison.java

CMD ["java", "SearchAlgorithmsComparison"]
