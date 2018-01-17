import requests
import sys
url='https://vision.googleapis.com/v1/images:annotate?key='+sys.argv[1]
#print url
data='''{
  "requests": [
    {
      "features": [
        {
          "type": "LABEL_DETECTION"
        }
      ],
      "image": {
        "source": {
          "imageUri": "PUT_URL_HERE"
        }
      }
    }
  ]
} '''
data=data.replace("PUT_URL_HERE", sys.argv[2])
#print data
response = requests.post(url, data=data)
file_out = open(sys.argv[3],"w+")
output_str=""
response = response.json()
responses = response['responses']
#print response
for response in responses:
        labels = response['labelAnnotations']
        for label in labels:
                output_str+="#"
                output_str+=label['description'].replace(' ','')
                output_str+=" "
file_out.write(output_str)
