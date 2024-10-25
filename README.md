## Backend Project Template
This project is a template for creating backend applications using Python and the repository pattern. It provides a scalable and maintainable structure for developing APIs with a clean separation between business logic, data access, and API controllers. The project uses FastAPI as the web framework and PostgreSQL as the database. Note that the database can be changed if you want to but its currently based on Postgresql.

### Project Structure
```sh
├── .vscode/                   # VS Code-specific settings for the workspace
│   ├── settings.json          # Workspace-specific editor and extension settings
│   ├── launch.json            # Debugging configurations for the project
│   ├── tasks.json             # Custom tasks for running scripts or tests
│   └── extensions.json        # Recommended extensions for VS Code
├── .dockerignore              # Docker ignore file to exclude files from Docker builds
├── .gitignore                 # Git ignore file to exclude files from version control
├── Dockerfile                 # Dockerfile to build the project image
├── docker-compose.yml         # Docker Compose configuration for the entire stack
├── docker-compose.debug.yml   # Docker Compose configuration for debugging purposes
├── init-data.sql              # SQL script for creating tables and initial data
├── main.py                    # Entry point for the FastAPI application
├── requirements.txt           # Python dependencies for the project
├── setup.sh                   # Script to set up PostgreSQL and Web API using Docker Compose
├── destroy.sh                 # Script to tear down Docker Compose setup
├── test_users_service.py      # Unit tests for users service
├── .README.md                 # A Readme file with instructions on using the template
├── src/                       # Source code directory
│   ├── services/              # Business logic and service classes
│   ├── controllers/           # API controllers for routing and handling requests
│   ├── repository/            # Data access layer for interacting with PostgreSQL
│   └── dto/                   # Data Transfer Objects (DTOs)
│       ├── base/              # Base DTOs
│       ├── read/              # DTOs for reading operations
│       └── write/             # DTOs for writing operations
```

### Prerequisites
* Docker
* Docker Compose
* Python 3.12
* pip
* python3 -m venv

### Installation
1. Clone the repository

* git clone <your-repo-url>
* cd <your-repo-folder>

2. Build and run the Docker containers:
```sh
./setup.sh
```
Access the API: Once the containers are up, the API should be accessible at http://localhost:8000

3. To stop and remove the containers, run:

```sh
./destroy.sh
```

### Testing
```sh
python -m unittest test_users_service.py

# Or

pytest -v -s
```

### Development
* Create python environment
```sh
python3.12 -m venv .venv
```

* Add Database Credentials as Environment Variables

```sh
#In .venv > bin > activate add the following
export DATABASE=""
export DATABASE_PWD=""
export DATABASE_USER=""
export DATABASE_HOST=""
```

* Activate environment
```sh
source venv/bin/activate
```

* Install packages
```sh
pip install -r requirements.txt
```

* Run Application
```sh
uvicorn main:app --reload
```