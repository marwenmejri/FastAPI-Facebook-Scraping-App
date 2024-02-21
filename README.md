# FastAPI - Facebook Scraping App

This project demonstrates a FastAPI application designed to scrape data from public Facebook pages, save the scraped data into a PostgreSQL database, and dockerize the entire application for easy deployment and scalability.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose
- Python 3.9 or higher

### Installation

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/marwenmejri/FastAPI-Facebook-Scraping-App.git

2. Navigate to the project directory:
    ```sh
   cd yourrepositoryname

3. Create a .env file in the root of the project directory and fill in your PostgreSQL database credentials and other environment variables as described in this .env.example:
    ```sh 
    DB_USER=postgres
    DB_PASSWORD=20759232
    DB_NAME=scraping_app
    DB_HOST=localhost
    DB_PORT=5432

4. Build and start the containers:
    ```sh 
   docker-compose up --build

![Alt text](demo_images/Screenshot from 2024-02-21 17-14-35.png)

![Alt text](demo_images/Screenshot from 2024-02-21 17-14-47.png)

![Alt text](demo_images/Screenshot from 2024-02-21 17-21-41.png)

### Using the Application
- Once the application is running, you can access it at http://localhost:8000.

![Alt text](demo_images/Screenshot from 2024-02-21 17-16-41.png)

![Alt text](demo_images/Screenshot from 2024-02-21 22-25-25.png)

### Endpoints
- GET /: The home page with a welcome message.

- Scrape And Save Posts
![Alt text](demo_images/Screenshot from 2024-02-21 17-20-21.png)

- Get Post By Page Name
![Alt text](demo_images/Screenshot from 2024-02-21 17-20-46.png)

- Get Post By Id
![Alt text](demo_images/Screenshot from 2024-02-21 17-21-08.png)

- List Posts
![Alt text](demo_images/Screenshot from 2024-02-21 17-21-24.png)

### Postgres DB

![Alt text](demo_images/Screenshot from 2024-02-21 17-23-02.png)


## Authors
Marwen Mejri - Data Engineer - https://github.com/marwenmejri