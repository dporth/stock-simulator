# Design
This stock simulator will allow users to simulate stock purchases based off the real stock market. 
Users will be able to set how many shares of a specific stock they wish to purchase and the price they wish to purchase those shares at.
Then users will have access to end of day stock market data which shows the actual value of their investment based off the real stock market prices.

![](./assets/data_model.png)  

## ETL
To obtain the data that allows users to access end of day stock market data which shows the acutal value of their investment based off the real stock market prices, the python script under /src/etl needs to be scheduled to run daily. This script leverages the Market Stack stock market API. So you will have to create an account on Market Stack and obtain a personal access token. This token needs to be set in an environment variable called MARKET_STACK_API_KEY.

# Getting Started
## Security
This API is secured using Auth0. You will need to create an account at Auth0 and register a native API application. After doing so you will need to obtain the auth0 domain (aka tenant url) and the api audience for the native API application. The value of these two fields will need to be set in environment variables called AUTH0_DOMAIN and API_AUTH0_AUDIENCE, respectively. Futher, this API enables users to be deleted using your Auth0 Management API. You need to obtain the client id, client secret, and api audience for the management API and store the values in the environment variables AUTH0_MGT_CLIENT_ID, AUTH0_MGT_CLIENT_SECRET, AUTH0_MGT_API_AUDIENCE.

## Database
This program depends on a SQL Server backend. A instance of a SQL Server database must be running. The DDL to set up the schema and tables that this application depends on is located under /assets. Run this SQL before running the API. Next update DATABASE_SERVER, DATABASE_ACCOUNT, DATABASE_NAME, DATABASE_SCHEMA, and DATABASE_PASSWORD environment variables on your host machine with your SQL server details.
## Docker
This project is containerized using Docker. You can create a Docker image for the application and spin up a container with the web service running inside the container. To do so run the following commands from within /src/:
1) `sudo docker build --build-arg database_server=${DATABASE_SERVER} --build-arg database_account=${DATABASE_ACCOUNT} --build-arg database_password=${DATABASE_PASSWORD} --build-arg api_auth0_audience=${API_AUTH0_AUDIENCE} --build-arg auth0_domain=${AUTH0_DOMAIN} --build-arg auth0_mgt_client_id=${AUTH0_MGT_CLIENT_ID} --build-arg auth0_mgt_client_secret=${AUTH0_MGT_CLIENT_SECRET} --build-arg auth0_mgt_api_audience=${AUTH0_MGT_API_AUDIENCE} --build-arg database_name=${DATABASE_NAME} --build-arg database_schema=${DATABASE_SCHEMA} -t stock-simulator-api .` 
2) `docker run -p 5000:5000 stock-simulator-api`

At this point the API is running and available on port 5000.

## API
### Swagger
The docs for this API are generated with Swagger. If an instance of this program is running inside a container, you can visit http://localhost:5000/apidocs/#/ to see the docs. This will work as long as you followed the section "Getting Started".

## Deploying to AWS BeanStalk
### Commands
1) create .ebextensions/setup.config
packages:
  yum:
    gcc-c++: []
    unixODBC-devel: []
2) eb init -p python-3.6 simustock --region us-east-2
3) eb create simustock
4) eb open

## Auth0 Native App Implementation 
### OAuth2 Authorization Flow
1) Omitt client secret from native app
2) Authorization requests made from native app are only made through external user-agents (user's browser)
