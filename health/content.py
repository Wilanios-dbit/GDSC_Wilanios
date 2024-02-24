import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def create_shortcut():
  """Create a third party shortcut

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  creds, _ = google.auth.default()

  try:
    # create drive api client
    service = build("drive", "v3", credentials=creds)
    file_metadata = {
        "name": "Project plan",
        "mimeType": "application/vnd.google-apps.drive-sdk",
    }

    # pylint: disable=maybe-no-member
    file = service.files().create(body=file_metadata, fields="id").execute()
    print(f'File ID: {file.get("id")}')

  except HttpError as error:
    print(f"An error occurred: {error}")
  return file.get("id")


if __name__ == "__main__":
  create_shortcut()