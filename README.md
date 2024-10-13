# Sentiment Analysis Project

This project provides a sentiment analysis tool that uses three different libraries: **TextBlob**, **VADER**, and **BERT**. Users can input text feedback, and the script will analyze the sentiment and return results for each method.

## Features

-   **TextBlob**: Basic sentiment analysis using TextBlob's built-in functions.
-   **VADER**: A more nuanced analysis using the VADER sentiment analysis tool, particularly good for social media text.
-   **BERT**: Advanced sentiment analysis using a pre-trained BERT model that outputs sentiment as "Positive," "Neutral," or "Negative."

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2. Install Pipenv (if you haven't already): You can install Pipenv via pip:
    ```bash
    pip install pipenv
    ```
3. Create and activate a virtual environment:
    ```bash
    pipenv install
    pipenv shell
    ```
4. Install the required packages: The necessary packages will be installed automatically when you create the environment, but you can run:

    ```bash
    pipenv install textblob vaderSentiment transformers
    ```

## Usage

1. Run the script:

    ```python
    python main.py
    ```

2. When prompted, enter the feedback text for analysis. For example:

    ```vbnet
    Enter the feedback text: This is amazing but lacks the details.
    ```

3. The script will output the sentiment analysis results for each method:

    ```yaml
    TextBlob Sentiment: Positive | Score: 0.6000
    VADER Sentiment: Positive | Score: 0.3400
    BERT Sentiment: Neutral | Score: 0.4285
    ```

## Example Output

When you enter feedback like `"Shipping was fast, but the product broke after one day."`, the output will be:

    ```yaml
    TextBlob Sentiment: Positive | Score: 0.6000
    VADER Sentiment: Positive | Score: 0.3400
    BERT Sentiment: Neutral | Score: 0.42854285
    ```

## Acknowledgments

-   TextBlob: TextBlob Documentation
-   VADER: VADER Documentation
-   BERT: Transformers Documentation
