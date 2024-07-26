# AI Recipe Generator

This project is a Django-based web application that integrates a machine learning model for generating recipes based on a list of ingredients. The model, fine-tuned from the T5-small architecture, is hosted on Hugging Face and utilizes the RecipeNLG dataset for training.

![Homepage](https://github.com/mihirr007/recipe-generation/blob/main/ecochefmain/appecochef/templates/appecochef/img/components/layout/CTA/ecochef_demo.png)
![Homepage](https://github.com/mihirr007/recipe-generation/blob/main/ecochefmain/appecochef/templates/appecochef/img/components/layout/CTA/Screenshot%20(126).png)
![Homepage](https://github.com/mihirr007/recipe-generation/blob/main/ecochefmain/appecochef/templates/appecochef/img/components/layout/CTA/Screenshot%20(127).png)
![Homepage](https://github.com/mihirr007/recipe-generation/blob/main/ecochefmain/appecochef/templates/appecochef/img/components/layout/CTA/Screenshot%20(128).png)
![Homepage](https://github.com/mihirr007/recipe-generation/blob/main/ecochefmain/appecochef/templates/appecochef/img/components/layout/CTA/Img%20(9).png)
![Homepage](https://github.com/mihirr007/recipe-generation/blob/main/ecochefmain/appecochef/templates/appecochef/img/components/layout/CTA/Img%20(10).png)



## Features

- **Recipe Generation**: Generate recipe titles, ingredients, and instructions based on a list of ingredients provided by the user.
- **Model Training**: Fine-tunes the T5-small model on a custom dataset of recipes.
- **GPU Acceleration**: Utilizes GPU acceleration for efficient model training in Google Colab.
- **Google Drive Integration**: Load and save model checkpoints directly from Google Drive.

## Hosted Model and Dataset

- **Fine-Tuned Model**: The output from the fine-tuned T5-small model is hosted on [Hugging Face](https://huggingface.co/raddus/ecochef-recipe-generation).
- **Training Dataset**: The T5-small model is trained on the RecipeNLG dataset, available at [RecipeNLG](https://recipenlg.cs.put.poznan.pl/) and [Kaggle Dataset](https://www.kaggle.com/datasets/paultimothymooney/recipenlg). The dataset provides diverse recipe data that enables the model to generate accurate and varied recipe outputs.

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
