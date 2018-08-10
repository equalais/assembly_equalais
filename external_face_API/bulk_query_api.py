'''
josh spec
input: API type, list of image objects in memory
required output: list where each element is probability of face (if many faces in image, max of probabilities)
current output: list where each element is the number of faces in image because google cloud does not provide probabilities of faces :(
'''

'''
IMPORTANT!!! make sure to configure export GOOGLE_APPLICATION_CREDENTIALS=pathtokeyfile
'''

import argparse
import io
import os

from google.cloud import vision
from google.cloud.vision import types

def detect_faces_single_image(image_object):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=image_object)
    response = client.face_detection(image=image)
    faces = response.face_annotations

    print('Num faces:', len(faces))
    return len(faces)


def bulk_query_api(list_images, API_type='tbd', ):
    results = []
    for image_object in list_images:
        num_faces_in_image = detect_faces_single_image(image_object)
        results.append(num_faces_in_image)
    print('results', results)
    return results

if __name__== "__main__":
    path_to_image_folder = 'images/'
    all_images = os.listdir(path_to_image_folder)
    list_images = []
    for image in all_images:
        print(image, 'read..')
        with io.open(os.path.join(path_to_image_folder, image), 'rb') as image_file:
            image_object = image_file.read()
        list_images.append(image_object)
        # list_images.append({'image_name': image, 'image_object': image_object})
    # print(len(list_images))
    bulk_query_api(list_images)

# # REFERNCE code from google API documentation: https://cloud.google.com/vision/docs/detecting-faces#vision-face-detection-python
# def detect_faces(path):
#     """Detects faces in an image."""
#     client = vision.ImageAnnotatorClient()
#
#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()
#
#     image = types.Image(content=content)
#
#     response = client.face_detection(image=image)
#     faces = response.face_annotations
#
#     # Names of likelihood from google.cloud.vision.enums
#     likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
#                        'LIKELY', 'VERY_LIKELY')
#     print('Faces:')
#
#     for face in faces:
#         print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
#         print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
#         print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
#
#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                     for vertex in face.bounding_poly.vertices])
#
#         print('face bounds: {}'.format(','.join(vertices)))
