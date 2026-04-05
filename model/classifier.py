"""
Produce Freshness Classifier

TODO: Implement the classifier using a pre-trained model.

Hints:
- Use torchvision.models.resnet50(pretrained=True) as a starting point
- You'll need to add a custom classification head for freshness levels
- For the MVP, you can use the ImageNet classes to identify produce type
  and add freshness logic on top

Steps:
1. Load a pre-trained ResNet50
2. Define freshness categories: ["Fresh", "Slightly Aged", "Expired"]
3. Preprocess input images (resize to 224x224, normalize)
4. Run inference and return classification + confidence
"""

from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models


class ProduceClassifier:
    def __init__(self):
        """
        TODO: Initialize the model.
        Load a pre-trained ResNet50 and set up the image transforms.
        """
        self.model = None  # TODO: Load model
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            ),
        ])
        self.freshness_levels = ["Fresh", "Slightly Aged", "Expired"]

    def classify(self, image: Image.Image) -> dict:
        """
        TODO: Classify the produce in the image.

        Args:
            image: PIL Image of produce

        Returns:
            dict with keys: item, freshness, confidence, tips
        """
        # YOUR CODE HERE
        return {
            "item": "unknown",
            "freshness": "Fresh",
            "confidence": 0.0,
            "tips": "Not implemented yet"
        }
