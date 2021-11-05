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
    config = dotenv_values()
    snyk_token = config["SNYK_TOKEN"]
    org_id = config["ORG_ID"]
    user_id = config["USER_ID"]
    project_id = config["PROJECT_ID"]

    session = create_session(snyk_token)
    test_uri = f"orgs/{org_id}/users/{user_id}"

    # # Get user details
    # res = session.get(url=test_uri, params={"version": "2021-09-13~beta"})
    # print(json.dumps(res.json(), indent=2))

    # Get a list of all issues from a Snyk Code project
    all_issues_url = f"orgs/{org_id}/issues"

    params = {
        "project_id": project_id,
        "version": "2021-08-20~experimental",
    }

    res = session.get(url=all_issues_url, params=params)

    # Iterate over the list of issue data and print the issue details
    data = res.json()["data"]
    for d in data:
        if d["attributes"]["severity"] == "high":
            print(d["attributes"]["title"])


if __name__ == "__main__":
    main()
