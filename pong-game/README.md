# Computer Vision Pong Arcade Game

## Overview

This project is a Pong arcade game that uses computer vision to control the paddle. The game is developed using Python 3.6, leveraging the `pygame` library for game development and `mediapipe` for hand tracking.

## Features

- Hand tracking using a webcam to control the paddle.
- Simple graphics using `pygame`.
- Score and life tracking.
- Fullscreen toggle and game reset functionality.

## Requirements

- Python 3.6
- `pygame`
- `opencv-python`
- `mediapipe`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/aiBard101/computer_vision_projects.git
    cd computer_vision_projects/pong-game
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements
    ```

## Usage

1. Run the game:

    ```bash
    python main.py
    ```

2. Control the paddle using your hand. The game uses the webcam to track hand movements. Ensure your hand is visible to the webcam for the best experience.

3. Use the following keys for additional controls:
    - `q`: Quit the game
    - `f`: Toggle fullscreen mode
    - `r`: Reset the game

## Code Structure

- `main.py`: The main script containing the game logic.
- `assets/`: Directory for game assets like images.

### Key Classes and Functions

- `AI_hands`: Class for handling hand tracking using `mediapipe`.
  - `__init__(self, width, height)`: Initializes the hand tracking with specified width and height for the webcam feed.
  - `hands(self, frame)`: Processes the webcam frame and returns the hand landmarks.

- `rec(x, w, h)`: Function to create a rectangular paddle.
- Main game loop: Handles events, updates game state, and renders the game.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgements

- `pygame` for game development.
- `mediapipe` for the hand tracking functionality.
- Inspiration from classic Pong games.

## Contact

For any questions or feedback, please contact:

- **Email**: [aibard.annonymousasquare@gmail.com](aibard.annonymousasquare@gmail.com)
- **GitHub**: [aiBard](https://github.com/aiBard101/)
- **X**: [aiBard001](https://x.com/aiBard001)
- **LinkedIn**: [aiBard](https://www.linkedin.com/in/george-junior-alainengiya-5b44b5251/)
- **WhatsApp**: [aiBard](https://%20https://wa.me/message/AL5IJZCUYD6LG1)
Visit my Website[Website](https://aibard.code.blog/computer-vision-pong-arcade-game/).

---
Watch the [YouTube video](https://youtu.be/O22W1Vvs37E) demonstrating the game.

---

Feel free to reach out if you have any questions or suggestions!