#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json
import random

def recognize_celebrities(photo):
    famous = ['홍승안', '박지훈', '뷔']

    
    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})

    print('Detected faces for ' + photo)
    check = True
    for celebrity in response['CelebrityFaces']:
        # print ('Name: ' + celebrity['Name'])
        print('닮은 연예인은 {}입니다.'.format(celebrity['Name']))
        check = False
    
    if check == True:
        print('닮은 연예인은 {}입니다.'.format(famous[random.randrange(3)]))
    

    # if len(response['CelebrityFaces']) >=1:
    #    print('닮은 연예인은 {}입니다.'.format(celebrity['Name']))
   # else:
    #    print('닮은 연예인은 {}입니다.'.format(famous[random.randrange(3)]))
#        print ('Id: ' + celebrity['Id'])
#        print ('Position:')
#        print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
#        print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
#        print ('Info')
        #for url in celebrity['Urls']:
         #   print ('   ' + url)
        #print
    return len(response['CelebrityFaces'])

def main():
    photo='../Downloads/KakaoTalk_20210708_074927753.jpg'

    celeb_count=recognize_celebrities(photo)
    print("Celebrities detected: " + str(celeb_count))


if __name__ == "__main__":
    main()