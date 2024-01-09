from app import storage

def uploadFile(file, bucket, filename):
  if not storage.bucket_exists(bucket):
    storage.make_bucket(bucket)
  storage.put_object(bucket, filename, file, file.content_length)

def deleteFile(bucket, filename):
  error = storage.remove_object(bucket, filename)
  if error:
    print(f"Error deleting file {filename} from bucket {bucket}: {error}")

def getFile(bucket, filename):
  return storage.get_object(bucket, filename)

def getFileUrl(bucket, filename):
  return storage.presigned_get_object(bucket, filename)

def updateFile(file, bucket, filename, oldFilename):
  deleteFile(bucket, oldFilename)
  uploadFile(file, bucket, filename)