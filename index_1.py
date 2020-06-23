import requests

print('Beginning file download with requests')

url = 'https://playment-data-uploads.s3.ap-south-1.amazonaws.com/clients/8a8a7fee-0446-4510-b5c4-9394bae3711c/projects/78a0b6c5-bdcc-4140-b0aa-19df99d13184/batch_export_result/5d7be6e2-f1e9-4fe5-ad9c-7b0b2f49d75a/Sample_data/9.png'
r = requests.get(url)

with open('C:/Users/nikun/Downloads/image1.jpg', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)