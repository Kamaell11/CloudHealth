# CloudHealth
CloudHealth is a cloud-based health and fitness monitoring platform. Record measurements, track progress and get personalized recommendations. It uses Kubernetes, Cosmos DB, GitHub Actions, Azure Monitor and AI.

## Project Overview

CloudHealth is an innovative platform that empowers users to monitor their health and fitness using cloud technologies. The application offers a wide range of features, including recording health metrics, tracking physical activity, analyzing health trends, and receiving personalized recommendations.

## Key Features

*   Record health metrics (heart rate, blood pressure, blood sugar, etc.)
*   Track physical activity and analyze trends
*   REST API for managing users, health data, and recommendations

## Cloud Technologies

The project leverages five key cloud technologies:

### 1. Kubernetes (AKS)

*   A Kubernetes cluster on Azure (AKS) manages containers and enables automatic application scaling.
*   Application deployment using `kubectl apply`.

### 2. Azure Cosmos DB

*   A NoSQL document database stores user information and their health metrics.
*   Data structure:
    *   Users – Partition Key: `/id`
    *   HealthMetrics – Partition Key: `/userId`
    *   Activities – Partition Key: `/userId`
    *   Recommendations – Partition Key: `/userId`

### 3. GitHub Actions

*   Automates the CI/CD process, including building the application image, testing, and deploying to AKS.

### 4. Azure Monitor + Prometheus

*   Monitors system and application metrics using Prometheus and Grafana.

### 5. Azure AI Services

*   Analyzes health data using AI to identify potential health issues and suggest preventive measures.

## Documentation

Complete project documentation, including architecture descriptions, diagrams, and source code, is available on the assignment platform. The project will be presented in the lab for final evaluation.

## Presentation

The project will be presented during the lab session for final grading.