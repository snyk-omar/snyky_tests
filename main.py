import json
import requests
from dotenv import dotenv_values
from urllib.parse import urljoin


class SnykSession(requests.Session):
    """
    Class to create a session with Snyk API.
    """

    def __init__(self, prefix_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix_url = prefix_url

    def request(self, method, url, *args, **kwargs):
        """
        Override the request method to add the prefix_url.
        """
        url = urljoin(self.prefix_url, url)
        return super().request(method, url, *args, **kwargs)


def create_session(snyk_token: str) -> requests.Session:
    """
    Function to create a session with Snyk API.

    snyk_token: string
    return requests.Session
    """
    # Using the Snyk v3 API endpoints. Can be adjusted to previous versions.
    session = SnykSession(prefix_url="https://api.snyk.io/v3/")
    session.headers.update(
        {
            "Content-Type": "application/vnd.api+json",
            "Authorization": f"token {snyk_token}",
        }
    )
    return session


def convert_payload_to_json(payload: dict) -> str:
    """
    Function to convert the payload to JSON.

    payload: dict
    return string
    """
    return json.dumps(payload, indent=2)


def main() -> None:
    CONFIG = dotenv_values()
    SNYK_TOKEN = CONFIG["SNYK_TOKEN"]
    ORG_ID = CONFIG["ORG_ID"]
    USER_ID = CONFIG["USER_ID"]

    session = create_session(SNYK_TOKEN)
    test_uri = f"orgs/{ORG_ID}/users/{USER_ID}"

    # Get user details
    res = session.get(url=test_uri, params={"version": "2021-09-13~beta"})
    print(res.json())


if __name__ == "__main__":
    main()
