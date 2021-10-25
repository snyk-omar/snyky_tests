import json
import requests
from dotenv import dotenv_values


def make_request(snyk_token: str, url: str) -> str:
    header = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"token {snyk_token}",
    }
    params = {"version": "2021-06-04~beta"}

    req = requests.get(url, headers=header, params=params)

    json_payload = json.loads(req.text)
    # Pretty printing the output to make it easier to read
    return json.dumps(json_payload, indent=2)


def main() -> None:
    CONFIG = dotenv_values()
    SNYK_TOKEN = CONFIG["SNYK_TOKEN"]
    ORG_ID = CONFIG["ORG_ID"]
    ALL_PROJECTS = f"https://api.snyk.io/v3/orgs/{ORG_ID}/projects"

    result = make_request(snyk_token=SNYK_TOKEN, url=ALL_PROJECTS)
    # printing to standard out to see the result
    print(result)


if __name__ == "__main__":
    main()
