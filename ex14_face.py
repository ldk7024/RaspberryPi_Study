#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json

def detect_faces(photo, bucket):

    client=boto3.client('rekognition')

    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])

    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        if faceDetail['Gender']:
            print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
                + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        
        age = (faceDetail['AgeRange']['High'] + faceDetail['AgeRange']['Low'])/2
        if faceDetail['Gender']['Value'] == 'male':
            print('성별은 남성입니다.')
        else:
            print('성별은 여성입니다.')
        
        print('나이는 {}세입니다.'.format(int(age)))
        print('현재 감정 상태는 {}입니다.'.format(faceDetail['Emotions'][0]['Type']))



        print('Here are the other attributes:')
#        print(json.dumps(faceDetail, indent=4, sort_keys=True))

		# Access predictions for individual face details and print them
        print("Gender: " + str(faceDetail['Gender']))
        print("Smile: " + str(faceDetail['Smile']))
        print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
        print("Emotions: " + str(faceDetail['Emotions'][0]))

    return len(response['FaceDetails'])
def main():
    photo='Screenshot_20210708-173740_KakaoTalk.jpg'
    bucket='daegyobucket'
    face_count=detect_faces(photo, bucket)
    print("Faces detected: " + str(face_count))


if __name__ == "__main__":
    main()

