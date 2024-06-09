# Book Recommendation Application

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [API Usage](#api-usage)
5. [Local Setup](#local-setup)
6. [Testing the API](#testing-the-api)

---

## Introduction

This project is a Book Recommendation System designed to suggest books based on the title provided by the user. The project has been hosted on the cloud platform Render, and the API is accessible for public use. The project leverages machine learning techniques to recommend books to the user based on what type of book the user reads.

## Features

- Recommend books based on a given book title.
- Hosted on Render for easy access.
- Modular code structure following coding standards.
- Comprehensive logging and test cases.
- Portable and maintainable codebase.
- High level design of the system is in the file HLD.txt

## Technologies Used

- Python
- Flask
- Machine Learning
- Render (for cloud hosting)
- pandas, seaborn, matplotlib (for data analysis)
- Cassandra (as the database)

## API Usage

### Endpoint

- `https://vervebridge-bookrecommender.onrender.com/recommend`

### Method

- POST

### Request Body

The request body should be in raw JSON format. Example:

```json
{
  "title": "Data Smart"
}
```

Here in place of Data Smart we can put name of the book(from the dataset) for which we want recommendations. (Note: The alphabets in book name are case sensitive)

### Response

The response will be a JSON array of recommended book titles. Example:

```json
[
    "Python for Data Analysis",
    "Data Mining Handbook",
    "Data Scientists at Work",
    "Data Analysis with Open Source Tools",
    "Fundamentals of Wavelets",
    "Statistical Decision Theory",
    "Moon is Down, The",
    "Once There Was a War",
    "Journal of a Novel",
    "Grapes of Wrath, The"
]

```
## Local Setup
To set up the project locally, follow these steps:

1. Clone the repository from GitHub:
   ``` 
    git clone https://github.com/Ramakantsahoo/Vervebridge-BookRecommender.git
    cd Vervebridge
   ```
2. Create a virtual environment:
   ``` 
    python -m venv venv
   ```
3. Activate the virtual environment:
  . On Windows:
       ``` 
          venv\Scripts\activate
       ```
  . On macOS/Linux:
       ``` 
          source venv/bin/activate
       ```
   
4. Install the required dependencies:

   ``` 
    pip install -r requirements.txt
   ```

5. Run the application:   

  ``` 
    python main.py
  ```
4. During execution, if an image appears on the screen (due to pyplot and seaborn for exploratory data analysis), close the image to proceed with the model execution.


## Testing the API
You can test the API using tools like Postman or by making a curl request.

### Using Postman
1. Open Postman.
2. Set the request type to POST.
3. Enter the URL: https://vervebridge-bookrecommender.onrender.com/recommend
4. In the Body tab, select raw and JSON.
5. Enter the JSON request body:

   ```json
     {
      "title": "Data Smart"
     }
   ```

   Here in place of Data Smart we can put name of the book(from the dataset) for which we want recommendations. (Note: The alphabets in book name are case sensitive)

6. Click Send and observe the response.

### Using curl

  ```bash
     curl -X POST https://vervebridge-bookrecommender.onrender.com/recommend -H "Content-Type: application/json" -d '{"title": "Data Smart"}'
   ```
  Here in place of Data Smart we can put name of the book(from the dataset) for which we want recommendations. (Note: The alphabets in book name are case sensitive)

