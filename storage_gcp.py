from google.cloud import storage

name = 'ATI_DenialsSummaryReport_20210428.xlsx'   
storage_client = storage.Client()
bucketName = 'pms-extract'
bucket = storage_client.bucket(bucketName)
stats = storage.Blob(bucket=bucket, name=name).exists(storage_client)
print()

#KYW_DenialsSummaryReport_20210428.xlsx
#ATI_DenialsSummaryReport_20210428.xlsx

'''
    bucketName = 'pms-extract'
    bucketFolder = 'PMS/Revinate/'
    localFolder = 'D:/PMS/Revinate/'

    localFile = 'D:/PMS/Revinate/'+name
    storage_client = storage.Client.from_service_account_json('D:/PMS/All_Credentials/Remington.json')
    bucket = storage_client.get_bucket(bucketName)
    blob = bucket.blob(bucketFolder + name)
    blob.upload_from_filename(localFile)

'''