# SimpleToDoList

This is a learning project for me. I am wanting to gain experience setting up every step of a full stack app with CI/CD workflows, testing, and tracking.

## Building

First create an env file or 2, depending on if you want to do development (hot reloads active) or just generate production code. Required fields are:  
POSTGRES_USER=  
POSTGRES_PASSWORD=  
POSTGRES_DB=\<name of postgres dabase>  
DB_VOLUME=\<docker volume name/label>  
DB_HOST=\<hostname for db>  
DB_PORT=\<port for db>  
PGADMIN_DEFAULT_EMAIL=\<pgadmin username for managing db>  
PGADMIN_DEFAULT_PASSWORD=\<pgadmin password for managing db>  
