# Interactive HabdWritten Digit Recognition Project

## Overview

This project demonstrates how to create a digit recognition system using Python, TensorFlow, OpenCV, and Pygame. The system includes three main parts: training a digit recognition model, creating a real-time video digit recognition application, and developing an interactive drawing application for digit recognition.

## Part 1: Training the Digit Recognition Model

### Libraries

- `numpy`
- `cv2`
- `tensorflow`
- `matplotlib`

### Dataset

Loaded the MNIST dataset of handwritten digits.

### Preprocessing

Applied thresholding and normalization to the images.

### Model

Built a sequential neural network model using TensorFlow's Keras API.

### Training

Trained the model on the preprocessed MNIST data.

### Evaluation

Evaluated the model on test data and displayed training/validation loss and accuracy plots.

### Saving

Saved the trained model for later use.

## Part 2: Real-time Video Digit Recognition

### Libraries

- `numpy`
- `cv2`
- `tensorflow`
- `math`

### Model Loading

Loaded the trained model from Part 1.

### Preprocessing Function

Defined a function to preprocess video frames by converting to grayscale, applying Gaussian blur, and thresholding.

### Prediction Function

Implemented a function to predict digits from preprocessed frames.

### Video Capture

Set up real-time video capture using OpenCV.

### Digit Prediction

Integrated the preprocessing and prediction functions into a loop that captures video frames and displays the predicted digit in real-time.

## Part 3: Interactive Drawing Application

### Libraries

- `pygame`
- `cv2`
- `numpy`
- `math`
- `tensorflow`

### Model Loading

Loaded the trained model from Part 1.

### Pygame Initialization

Set up Pygame for drawing and displaying the screen.

### Utility Functions

Created functions to save the screen, show the output image, and crop the drawing area.

### Image Processing

Implemented functions to refine images and predict digits using the model.

### Main Loop

Captured user input for drawing digits, predicted the drawn digits when a key is pressed, and displayed the results in a separate window.

## Requirements

To ensure the project runs smoothly, install the dependencies listed in the `requirements.txt` file:

```
numpy==1.24.2
opencv-python==4.7.0.72
tensorflow==2.12.0
matplotlib==3.7.1
pygame==2.1.0
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/aiBard101/computer_vision_projects/handwritten_digits_detection.git
   ```
2. Navigate to the project directory:
   ```sh
   cd handwritten_digits_detection
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

Run the script to train the digit recognition model:
```sh
python train_model.py
```

### Real-time Video Digit Recognition

Run the script to start real-time digit recognition from a video feed:
```sh
python realTimeDetection.py
```

### Interactive Drawing Application

Run the script to start the interactive drawing application:
```sh
python application.py
```

## Demonstration

Watch the [YouTube video](https://youtu.be/hbtTbjI_aaI) demonstrating the Real-time Video Digit Recognition.
Watch the [YouTube video](https://youtu.be/0GcZnx82ydI) demonstrating the Interactive Drawing Application.

## Conclusion

This project combines machine learning, computer vision, and interactive graphics to create a comprehensive digit recognition system. It showcases the entire workflow from data preprocessing and model training to real-time prediction and user interaction, making it a valuable learning experience for integrating multiple technologies.

Visit my Website[Website](https://aibard.code.blog/handwritten-digit-recognition/).