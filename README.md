# Book Recommendation Application

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [API Usage](#api-usage)
5. [Local Setup](#local-setup)
6. [Testing the API](#testing-the-api)
7. [Model Execution](#model-execution)
8. [Project Structure](#project-structure)
9. [Contributors](#contributors)
10. [License](#license)

---

## Introduction

This project is a Book Recommendation System designed to suggest books based on the title provided by the user. The project has been hosted on the cloud platform Render, and the API is accessible for public use. The project leverages machine learning techniques to recommend books to the user based on what type of book the user reads.

## Features

- Recommend books based on a given book title.
- Hosted on Render for easy access.
- Modular code structure following coding standards.
- Comprehensive logging and test cases.
- Portable and maintainable codebase.

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
