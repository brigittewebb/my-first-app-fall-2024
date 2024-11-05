# my-first-app-fall-2024

## Setup

Create and activate a virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment (whenever you come back to this project):

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

TODO include instructions here for signing up for email sending platform (e.g. Sendgrid). Obtain sendgrid API Key, and set the key and your sender address as environment variables.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."

# optionally:
SENDGRID_API_KEY="_______________"
SENDGRID_SENDER_ADDRESS="_________"
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
# ALPHAVANTAGE_API_KEY="..." python app/unemployment.py <- do not need to prefix the run command with the variable any more since it is defined in the .env file

python app/unemployment.py
```

Run the stocks report:

```sh
python app/stocks.py
```

Run the example email sending file:

```sh
python app/email_service.py
```