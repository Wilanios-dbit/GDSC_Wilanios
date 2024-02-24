import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def share_file(real_file_id, real_user, real_domain):
  """Batch permission modification.
  Args:
      real_file_id: file Id
      real_user: User ID
      real_domain: Domain of the user ID
  Prints modified permissions

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  creds, _ = google.auth.default()

  try:
    # create drive api client
    service = build("drive", "v3", credentials=creds)
    ids = []
    file_id = real_file_id

    def callback(request_id, response, exception):
      if exception:
        # Handle error
        print(exception)
      else:
        print(f"Request_Id: {request_id}")
        print(f'Permission Id: {response.get("id")}')
        ids.append(response.get("id"))

    # pylint: disable=maybe-no-member
    batch = service.new_batch_http_request(callback=callback)
    user_permission = {
        "type": "user",
        "role": "writer",
        "emailAddress": "user@example.com",
    }
    batch.add(
        service.permissions().create(
            fileId=file_id,
            body=user_permission,
            fields="id",
        )
    )
    domain_permission = {
        "type": "domain",
        "role": "reader",
        "domain": "example.com",
    }
    domain_permission["domain"] = real_domain
    batch.add(
        service.permissions().create(
            fileId=file_id,
            body=domain_permission,
            fields="id",
        )
    )
    batch.execute()

  except HttpError as error:
    print(f"An error occurred: {error}")
    ids = None

  return ids


if __name__ == "__main__":
  share_file(
      real_file_id="1dUiRSoAQKkM3a4nTPeNQWgiuau1KdQ_l",
      real_user="gduser1@workspacesamples.dev",
      real_domain="workspacesamples.dev",
  )