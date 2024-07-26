# AI Recipe Generator

This project is a Django-based web application that integrates a machine learning model for generating recipes based on a list of ingredients. The model is fine-tuned from the T5-small model using the Hugging Face Transformers library.

## Features

- **Recipe Generation**: Generate recipe titles, ingredients, and directions based on a list of ingredients provided by the user.
- **Model Training**: Fine-tunes the T5-small model on a custom dataset of recipes.
- **GPU Acceleration**: Utilizes GPU acceleration for efficient model training in Google Colab.
- **Google Drive Integration**: Load and save model checkpoints directly from Google Drive.

## Installation

### Prerequisites

- Python 3.7 or higher
- Django 3.2 or higher
- Libraries:
  - `transformers`
  - `datasets`
  - `pandas`
  - `sentencepiece`
  - `accelerate`
  - `torch`

### Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
