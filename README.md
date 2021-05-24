# Design
This stock simulator will allow users to simulate stock purchases based off the real stock market. 
Users will be able to set how many shares of a specific stock they wish to purchase and the price they wish to purchase those shares at.
Then users will have access to end of day stock market data which shows the actual value of their investment based off the real stock market prices.

# Stocks
The stocks supported by this application are found in the stockmarket.stock table. Every stock being used by a user in a stock account will have its current market price updated at end of day. This end of day price for a stock represents a single share and the data will be found in the stockmarket.stock_price_history table (which also is a type 2 table storing the history of stock prices). The stock simulator application relys on the free tier of a stock market api. As so, it cannot update all of the stocks at once, rather only 5 stocks per minute. In addition, stock accounts that are created for a stock that does not have a end of day price in the stock price history table are added to the stockmarket.stock_price_queue table. A program is responsible for polling the queue table and obtaining the lastest end of day price for those stocks in the queue. This logic is set up to work around the free stock tier limitations.

# Getting Started
## Security
This API is secured using Auth0. You will need to create an account at Auth0 and register a native API application. After doing so you will need to obtain the auth0 domain (aka tenant url) and the api audience for the native API application. The value of these two fields will need to be set in environment variables called AUTH0_DOMAIN and API_AUTH0_AUDIENCE, respectively. Futher, this API enables users to be deleted using your Auth0 Management API. You need to obtain the client id, client secret, and api audience for the management API and store the values in the environment variables AUTH0_MGT_CLIENT_ID, AUTH0_MGT_CLIENT_SECRET, AUTH0_MGT_API_AUDIENCE.

## Database
This program depends on a SQL Server backend. A instance of a SQL Server database must be running. The DDL to set up the schema and tables that this application depends on is located under /assets. Run this SQL before running the API. Next update DATABASE_SERVER, DATABASE_ACCOUNT, DATABASE_NAME, DATABASE_SCHEMA, and DATABASE_PASSWORD environment variables on your host machine with your SQL server details.

## ETL
To provide users with end of day stock market data which will show the acutal value of their investment stock accounts, the python scripts under /src/etl need to be scheduled.

### load_queue_stock_prices.py
This script leverages the Polygon stock market API. So you will have to create an account on Polygon.io and obtain a personal API access token. This token needs to be set in an environment variable called POLYGON_QUEUE_API_KEY.

## load_account_values.py
This script leverages the Polygon stock market API. So you will have to create an account on Polygon.io and obtain a personal API access token. This token needs to be set in an environment variable called POLYGON_STOCK_PRICE_UPDATER_KEY.

## Docker
This project is containerized using Docker. It includes a docker-compose.yml to faciliate the different builds, whether that be building the API image or the ETL images. 
You can create a Docker image for the API with the following command from within /src/:
1) `sudo docker-compose build --build-arg database_server=${DATABASE_SERVER} --build-arg database_account=${DATABASE_ACCOUNT} --build-arg database_password=${DATABASE_PASSWORD} --build-arg api_auth0_audience=${API_AUTH0_AUDIENCE} --build-arg auth0_domain=${AUTH0_DOMAIN} --build-arg auth0_mgt_client_id=${AUTH0_MGT_CLIENT_ID} --build-arg auth0_mgt_client_secret=${AUTH0_MGT_CLIENT_SECRET} --build-arg auth0_mgt_api_audience=${AUTH0_MGT_API_AUDIENCE} --build-arg database_name=${DATABASE_NAME} --build-arg database_schema=${DATABASE_SCHEMA} --build-arg polygon_queue_api_key=${POLYGON_QUEUE_API_KEY} api` 

You can create a Docker image for the ETL Queue Stock Prices with the following command from within /src/:
1) `sudo docker-compose build --build-arg database_server=${DATABASE_SERVER} --build-arg database_account=${DATABASE_ACCOUNT} --build-arg database_password=${DATABASE_PASSWORD} --build-arg api_auth0_audience=${API_AUTH0_AUDIENCE} --build-arg auth0_domain=${AUTH0_DOMAIN} --build-arg auth0_mgt_client_id=${AUTH0_MGT_CLIENT_ID} --build-arg auth0_mgt_client_secret=${AUTH0_MGT_CLIENT_SECRET} --build-arg auth0_mgt_api_audience=${AUTH0_MGT_API_AUDIENCE} --build-arg database_name=${DATABASE_NAME} --build-arg database_schema=${DATABASE_SCHEMA} --build-arg polygon_queue_api_key=${POLYGON_QUEUE_API_KEY} queue_etl`

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
