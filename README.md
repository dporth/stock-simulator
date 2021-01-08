# Design
This stock simulator will allow users to simulate stock purchases based off the real stock market. 
Users will be able to set how many shares of a specific stock they wish to purchase and the price they wish to purchase those shares at.
Then users will have access to end of day stock market data which shows the actual value of their investment based off the real stock market prices.

![](./assets/data_model.png)  

## Features
### Database
- [x] Data model
- [x] Create ETL jobs from data model

### Backend
Currently, the backend is programmed with Python

- [x] Implement database connection design
- [x] Create table dao's
- [x] Create Flask application
- [x] Flask application endpoints
- [ ] Purchase stock at today's real-time price
- [ ] Last updated date
- [ ] Next update countdown

### Frontent
- [ ] Frontend (TBD)
- [ ] Purchase stock at today's real-time price
- [ ] Last updated date
- [ ] Next update countdown


## Auth0 Implementation
### Facilate storing of user data
1) Frontend shows the Lock, user signs up.
2) Configure a post-registration hook on Auth0 which calls POST /users on my backend. This call will generate my db's userId and send it back to Auth0.
3) Put this userId into Auth0's user_metadata.
4) This user_metadata will be included in the JWT, so that all calls to my backend to fetch resources will include the db's userId (no need for additional lookup).