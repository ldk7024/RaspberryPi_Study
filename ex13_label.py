#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def detect_labels_local_file(photo):


    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    
    check = True
    print('Detected labels in ' + photo)    
    for label in response['Labels']:
        if label['Name'] == 'Dog':
            print('강아지일 확률은 {:.2f}% 입니다.'.format(label['Confidence']))
            check = False
#        print (label['Name'] + '일 확률은 '+ str(label['Confidence'])+ '입니다.')
      
    if check == True:
        print('강아지가 아닙니다.')
    return len(response['Labels'])
        
def main():
    photo='../Downloads/KakaoTalk_20210707_154312482.jpg'

    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()



