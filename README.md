# Documentation for Docker Commands

## Build Docker Image

- **Command**: `docker build -t hv .`
- **Description**: Builds a Docker image with the tag `hv` using the Dockerfile in the current directory.

## Run Docker Container

- **Command**:
  ```bash
  docker run -d -p 5000:5000 --env-file .env --volume=C:\Users\edils\OneDrive\Python\api_hv_elaverde:/app --name hv_elaverde hv
  ```
- **Description**: Runs a Docker container in detached mode (`-d`) with the following configurations:
  - Maps port `5000` of the host to port `5000` of the container.
  - Loads environment variables from the `.env` file.
  - Mounts the directory `C:\Users\edils\OneDrive\Python\api_hv_elaverde` on the host to `/app` in the container.
  - Names the container `hv_elaverde`.
  - Uses the `hv` image.

## Stop Docker Container

- **Command**: `docker stop hv_elaverde`
- **Description**: Stops the running container named `hv_elaverde`.

## Start Docker Container

- **Command**: `docker start hv_elaverde`
- **Description**: Starts the previously stopped container named `hv_elaverde`.
