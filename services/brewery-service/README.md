# Brewery Service
A FastAPI service to get and create information about breweries and beers.

# Library Overview
## /libs
This contains common utilities and data models that are or could be shared by multiple routes

## /routes
Contains endpoints and methods specific to each route in the API

## /models
Contains specific request and response models organized by route

# Testing
This uses pytest. To run from this directory:
```
pytest tests/
```