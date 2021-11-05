# Python and Snyk API

Learn how to use Python by learning how to talk to the Snyk API!

Things you need to use this script:

1. A virtual environment
2. Python 3.7+
3. A `.env` file

Inside of the `.env` file, you need two keys (and you can add more if you want to based on what you're doing with the Snyk API):

```
SNYK_TOKEN=""
ORG_ID=""
USER_ID=""
PROJECT_ID=""
```

Do NOT checkin the `.env` file to GitHub or any other SCM. This holds your secrets, and they're safer on your workstation rather than on the cloud.

Turn on your virtualenv and run `python main.py`, and you should get results. If not, please let me know, and we'll go over what is going on.

Make sure to turn on all feature flags for the Snyk v3 API for your org.
