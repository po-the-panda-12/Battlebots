import io
import os
from google.cloud import videointelligence_v1p3beta1
from google.cloud.videointelligence_v1p3beta1.types import Feature
from PIL import Image

# Set path to video file, output directory for frames, language hint for OCR, and path to output text file
video_file_path = 'test.mp4'
frames_output_dir = 'images_2'
language_hint = 'en'
text_output_file_path = 'script_2'

# Initialize Google Cloud Video Intelligence client
client = videointelligence_v1p3beta1.VideoIntelligenceServiceClient()

# Set video properties and features to extract
features = [Feature.LABEL_DETECTION, Feature.TEXT_DETECTION]
video_context = videointelligence_v1p3beta1.types.VideoContext(
    speech_transcription_config=videointelligence_v1p3beta1.types.SpeechTranscriptionConfig(
        language_code=language_hint,
        enable_automatic_punctuation=True,
        filter_profanity=True,
    ),
)
input_uri = f'gs://{bucket_name}/{file_name}'

# Perform video annotation and get text detection results
operation = client.annotate_video(
    input_uri=input_uri,
    features=features,
    video_context=video_context,
)
result = operation.result(timeout=90)
text_annotations = result.annotation_results[0].text_annotations

# Create list of unique captions from text detection results
captions = list(
    set([text_annotation.description for text_annotation in text_annotations]))

# Save captions to output file
with open(text_output_file_path, 'w') as output_file:
    for caption in captions:
        output_file.write(caption + '\n')

# Extract frames from video and perform OCR on each frame
os.makedirs(frames_output_dir, exist_ok=True)
frame_count = 0
with io.open(video_file_path, 'rb') as video_file:
    while True:
        frame_data = video_file.read(524288)
        if not frame_data:
            break
        image = Image.frombytes(
            'RGB', (320, 240), frame_data, 'raw', 'BGR', 0, 1)
        frame_path = os.path.join(
            frames_output_dir, f'frame_{frame_count:05}.jpg')
        image.save(frame_path)
        with io.open(frame_path, 'rb') as image_file:
            content = image_file.read()
        image = videointelligence_v1p3beta1.types.Image(content=content)
        image_context = videointelligence_v1p3beta1.types.ImageContext(language_hints=[
                                                                       language_hint])
        response = client.annotate_image(
            image=image,
            features=features,
            image_context=image_context,
        )
        text_annotations = response.text_annotations
        for text_annotation in text_annotations:
            caption = text_annotation.description.strip()
            if caption and caption not in captions:
                captions.append(caption)
                with open(text_output_file_path, 'a') as output_file:
                    output_file.write(caption + '\n')
        frame_count += 1
