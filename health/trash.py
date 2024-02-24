body_value = {'trashed': True}

response = drive_service.files().update(fileId="FILE_ID", body=body_value).execute()


body_value = {'trashed': False}

response = drive_service.files().update(fileId="FILE_ID", body=body_value).execute()


response = drive_service.files().emptyTrash().execute()

response = drive_service.files().delete(fileId="FILE_ID").execute()

