# Minimal DevOps App

A simple web application designed to practice DevOps workflows including Docker, CI/CD pipelines, and container verification. This project is perfect for learning Docker, GitHub Actions, and container-based deployments.

---
#Archutectural diagram
flowchart LR
    User[User / Browser]

    Host[Host Machine<br/>Port 8080]

    Docker[Docker Engine]

    Compose[Docker Compose]

    Container[Application Container<br/>Port 5000]

    App[Minimal DevOps App<br/>Flask<br/>APP_PORT=5000]

    User -->|HTTP Request| Host
    Host -->|Port Mapping 8080:5000| Docker
    Docker --> Compose
    Compose --> Container
    Container --> App
## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Getting Started](#getting-started)  
- [Docker Setup](#docker-setup)  
- [Running the Application](#running-the-application)  
- [CI/CD Pipeline](#cicd-pipeline)  
- [Health Check](#health-check)  
- [Contributing](#contributing)  
- [License](#license)

---

## Project Overview

This project demonstrates:

- Building a Docker image for a web application.
- Pushing the Docker image to Docker Hub.
- Running and testing containers locally.
- Automating CI/CD with GitHub Actions.

It is a minimal setup designed for learning and practicing DevOps principles.

---

## Features

- Dockerized web application  
- CI/CD pipeline for automated build and push  
- Health check for container verification  
- Easy to extend for more DevOps experiments

---

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed  
- [GitHub Account](https://github.com/) with repository access  
- Docker Hub account  
- GitHub Actions enabled for the repository

---

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/minimal-devops-app.git
cd minimal-devops-app
2. Make sure your Docker is running.

---

## Docker Setup

Build the Docker image locally:

```bash
docker build -t minimal-devops-app:latest .
docker run -d -p 5000:5000 --name minimal-devops-app minimal-devops-app:latest
http://localhost:5000
curl http://localhost:5000/health



