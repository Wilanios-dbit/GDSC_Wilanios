file_metadata = {
    'name': 'FILE_NAME',
    'mimeType': 'text/plain'
}
file = drive_service.files().create(body=file_metadata, fields='id').execute()
print('File ID: %s' % file.get('id'))
shortcut_metadata = {
     'Name': 'SHORTCUT_NAME',
     'mimeType': 'application/vnd.google-apps.shortcut',
     'shortcutDetails': {
        'targetId': file.get('id')
     }
}
shortcut = drive_service.files().create(body=shortcut_metadata,
                                    fields='id,shortcutDetails').execute()
print('File ID: %s, Shortcut Target ID: %s, Shortcut Target MIME type: %s' % (
    shortcut.get('id'),
    shortcut.get('shortcutDetails').get('targetId'),
    shortcut.get('shortcutDetails').get('targetMimeType')))