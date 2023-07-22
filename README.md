## Getting Started

Install `docker` and `docker-compose` and have the **docker application running** before attempting to run commands with `docker`, `docker-compose`, or spinning up a development environment

## Development
docker-compose.dev.yml will spin up the frontend development server, backend development server and a mysql database locally.
Both frontend and backend servers will automatically detect code changes and auto reload server when developing. Doing this will allow us to not have to install each dependency for the frontend, backend, and db locally.

Default development mysql container info:

default MYSQL_ROOT_PASSWORD: `my-secret-pw`

default MYSQL_DATABASE: `apiDB`

default mysql port: `3306`

### Visual Studio code (vscode) & Docker

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

Once all containers are running the following URLs will give you access to the frontend and backend local servers:

Frontend

`http://localhost:4200/`

Backend

`http://localhost:8000/`

You are now ready to start coding!!

### Manually using docker-compose

This method will require installing all dependencies locally if one does not connect to the respective containers. Using vscode locally to develop with the running containers will run into dependencies not found until they are install unless we use vscode's `Dev Containers` to connect to a running container which already has these dependencies installed.

Open your terminal in the root directory of this project.

Then, In your terminal run:

1. `docker-compose build`

2. `docker-compose up`

`docker-compose down` then `docker-compose build` to rebuild docker images

You are now ready to start coding!!

## Notes
Docker desktop can be used to view detailed log output of the frontend, backend, and mysql db servers when they are running. This can be useful for getting quick debugging info.
1. open Docker desktop
2. click on the 3 ellipses icon
3. click view details

This will show output logs of all 3 containers. This can also be done for each container separately, if one wants to view only a specific container's output logs.

Docker desktop also has the option to connect to a running container's terminal. This can be very useful for debugging and running commands inside of a container. For example, if one wants to connect to the mysql db container to inspect or run commands in the mysql shell.