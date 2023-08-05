## Getting Started

Install `docker` and `docker-compose` and have the **docker application running** before attempting to run commands with `docker`, `docker-compose`, or spinning up a development environment

Make sure to clone this repo an `cd` into the **root directory** of this project before running any commands

## Development
docker-compose.dev.yml will spin up the frontend development server, backend development server and a mysql database locally.
Both frontend and backend servers will automatically detect code changes and auto reload server when developing. Doing this will allow us to not have to install each dependency for the frontend, backend, and db locally.

Default development mysql container info:

default MYSQL_ROOT_PASSWORD: `my-secret-pw`

default MYSQL_DATABASE: `apiDB`

default mysql port: `3306`

Once all containers are running the following URLs will give you access to the frontend and backend local servers:

Frontend

`http://localhost:4200/`

Backend

`http://localhost:8000/`

### Visual Studio code (vscode) & Docker (Recommended)

This method requires vscode to be installed as this method will attach to running local development containers using vscode. Futhermore, in vscode, two extension are **needed** `Dev Containers` and the `Docker` extension. These can be found and installed in vscode under the *Extensions* tab. Specificity, Dev Containers will allow us to to attach a vscode instance to a running container. Dev Containers can also spin up the containers too if they are not running already when attaching. 

This setup will have two vscode instances (windows) running one for frontend development and the other for backend development.

First, open vscode in the root directory of this project. This is the directory where `docker-compose.dev.yml` is in.

Then open the Command Palette under View

the shortcut is as follows

Windows: `f1`

Mac: `Shift` + `Command` + `P`

1. Run Dev Containers: Open Folder in Container... from the Command Palette and select the backend folder

2. VS Code will then start up all 3 containers and connect this window to service backend.

3. Next, start up a new window using File > New Window.

4. In the new window, run Dev Containers: Open Folder in Container... from the Command Palette and select the frontend folder.

5. Since all the services are already running (step 1), VS Code will then connect to frontend.

You are now ready to start coding!!

### Manually using docker-compose

This method will require installing all dependencies locally if one does not connect to the respective containers. Using vscode locally to develop with the running containers will run into dependencies not found until they are install unless we use vscode's `Dev Containers` to connect to a running container which already has these dependencies installed.

Open your terminal in the root directory of this project.

Then, In your terminal run:

1. `docker-compose build`

2. `docker-compose up`

`docker-compose down` then `docker-compose build` to rebuild docker images

You are now ready to start coding!!

### Local app set up without docker

spinning up the frontend and backend locally without docker will require installing all dependencies locally. This is not recommended as it will require installing all dependencies for the frontend, backend, and db locally. This can be a pain to do and can cause issues with different versions of dependencies. This is why docker is recommended.

However, if one wants to spin up the frontend and backend locally without docker, follow the steps below.

#### Frontend

The frontend uses React with TypeScript and Vitejs. "Vite.js is a build tool and development server that is designed to enhance the development experience for modern web applications."

Pre-requisites:

1. **Nodejs version 18.16.1** or higher*

* Specificity Nodejs version 18.16.1 was used to develop the frontend. Other versions of Node.js may work but are not guaranteed to work. Nodejs can be downloaded and install [HERE](https://nodejs.org/)
* Download Nodejs and install the appropriate version for your OS.
* to check nodejs version run `node -v` in your terminal

After installing the appropriate version of Nodejs, run the following commands in your terminal in root directory of this project:

1. `cd frontend`
2. `npm install`
3. `npm run dev`

- `npm install` will install all dependencies for the frontend
- `npm run dev` will spin up the frontend development server
- After running `npm run dev` the frontend development server will be running on `http://localhost:4200/`

#### Backend

The backend uses Python with FastAPI. "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints."

Pre-requisites:
1. **Python version 3.11** or higher*

* Specificity Python version 3.11 was used to develop the backend. Other versions of Python may work but are not guaranteed to work. Python can be downloaded and install [HERE](https://www.python.org/downloads/)

After installing the appropriate version of Python, run the following commands in your terminal in root directory of this project:

1. `cd backend`
2. `python -m venv venv`
3. `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac)
4. `pip install -r requirements.txt`
5. `uvicorn --host 0.0.0.0 app.main:app --reload`

- `python -m venv venv` will create a virtual environment for the backend
- `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac) will activate the virtual environment
- `pip install -r requirements.txt` will install all dependencies for the backend
- `uvicorn main:app --reload` will spin up the backend development server
- After running `uvicorn --host 0.0.0.0 app.main:app --reload` the backend development server will be running on `http://localhost:8000/`

#### Database

The database uses MySQL.

Pre-requisites:
1. **MySQL version 8.0.26** or higher*

* Specificity MySQL version 8.0.26 was used to develop the database. Other versions of MySQL may work but are not guaranteed to work. MySQL can be downloaded and install [HERE](https://www.mysql.com/downloads/)

After installing the appropriate version of MySQL, run the following commands in your terminal in root directory of this project:

1. `mysql < source DDL.sql`

- `mysql < source DDL.sql` will create the database and tables needed for the backend to run
- `DDL.sql` is located in **/backend/app/schemas/SQL**

### Environment Variables

These are required for the backend to run.

| Variable                      | Description                                     | Values                                                                              | 
| -------------                 | -------------                                   |  -------------                                                                      |
| PROJECT_NAME                  | The name of the project                         | rentalServiceAPI                                                                    |
| SECRET_KEY                    | The secrete encryption key                      | SecretDevKey                                                                        |
| BACKEND_CORS_ORIGINS          | Allowed CORS urls                               | ["http://localhost","http://localhost:4200","http://localhost:3306"]                |
| ACCESS_TOKEN_EXPIRE_MINUTES   | Access Token default expiration time            | 30                                                                                  |
| MYSQL_HOST                    | The host name or IP address of the MySQL serve  | db                                                                                  |
| MYSQL_PORT                    | Mysql port                                      | 3306                                                                                |
| MYSQL_USER                    | Mysql user                                      | root                                                                                |
| MYSQL_PASSWORD                | Mysql password                                  | my-secret-pw                                                                        |
| MYSQL_DB                      | The name of the database being used             | apiDB                                                                               |

- These environment variables are used in the backend to connect to the MySQL database
- These environment variables are used in the backend to set the allowed CORS urls

- NOTE: The Mysql environment variables such as `MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, and MYSQL_DB` are used in the backend to connect to the MySQL database. These variables must match the values for **YOUR** mysql database. If you are using docker, these variables are already set in the docker-compose.yml file. If you are not using docker, these variables must be set so the backend and Mysql can communicate properly.

- Windows 10 environment variables can be set by following these instructions [HERE](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0)



## Notes
Docker desktop can be used to view detailed log output of the frontend, backend, and mysql db servers when they are running. This can be useful for getting quick debugging info.
1. open Docker desktop
2. click on the 3 ellipses icon
3. click view details

This will show output logs of all 3 containers. This can also be done for each container separately, if one wants to view only a specific container's output logs.

Docker desktop also has the option to connect to a running container's terminal. This can be very useful for debugging and running commands inside of a container. For example, if one wants to connect to the mysql db container to inspect or run commands in the mysql shell.