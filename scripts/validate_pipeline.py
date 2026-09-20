import json
import sys
import urllib.request
import urllib.error

OWNER = "lu-sclzo"
REPO = "secure-devops-migration-challenge"

API_URL = (
    f"https://api.github.com/repos/{OWNER}/{REPO}/"
    "actions/runs?per_page=1"
)


def get_latest_workflow_run():
    request = urllib.request.Request(
        API_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "secure-devops-validation-script"
        }
    )

    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode())

    except urllib.error.HTTPError as error:
        print(f"ERROR: GitHub API returned HTTP {error.code}")
        sys.exit(1)

    except urllib.error.URLError as error:
        print(f"ERROR: Could not connect to GitHub: {error.reason}")
        sys.exit(1)


def main():
    data = get_latest_workflow_run()
    runs = data.get("workflow_runs", [])

    if not runs:
        print("ERROR: No GitHub Actions workflow runs found.")
        sys.exit(1)

    run = runs[0]

    print("=== Secure DevOps Migration Validation ===")
    print(f"Repository: {OWNER}/{REPO}")
    print(f"Workflow:   {run.get('name')}")
    print(f"Branch:     {run.get('head_branch')}")
    print(f"Status:     {run.get('status')}")
    print(f"Conclusion: {run.get('conclusion')}")
    print(f"Run ID:     {run.get('id')}")
    print(f"Run URL:    {run.get('html_url')}")

    if run.get("status") == "completed" and run.get("conclusion") == "success":
        print("\nVALIDATION PASSED: Latest pipeline completed successfully.")
        sys.exit(0)

    print("\nVALIDATION FAILED: Latest pipeline did not complete successfully.")
    sys.exit(1)


if __name__ == "__main__":
    main()
