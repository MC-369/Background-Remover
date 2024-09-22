from transformers import pipeline

pipe = pipeline("image-segmentation", model="mattmdjaga/segformer_b2_clothes")