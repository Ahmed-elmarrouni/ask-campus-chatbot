﻿
# AskCampus Chatbot

AskCampus is a dynamic chatbot built to answer questions about Ynov campuses, programs, and student services. The project is divided into a **backend** (FastAPI) and a **frontend** (React), making it modular and scalable.

This chatbot uses fuzzy matching to provide accurate answers based on a predefined FAQ (`faq_tree`), with a clean user interface for seamless interaction.

---

## Table of Contents

1. [General Info](#general-info)
2. [How to Run the Frontend](#how-to-run-the-frontend)
3. [How to Run the Backend](#how-to-run-the-backend)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [FAQ](#faq)

---

## General Info

- **Frontend**: Built with React and Vite.js for a fast and responsive user interface.
- **Backend**: Powered by FastAPI with a simple endpoint structure to handle user queries.
- **Purpose**: Simplify access to Ynov campus information, enabling students to interact with a chatbot instead of browsing multiple pages.
- **Key Features**:
  - Fuzzy query matching using `RapidFuzz`.
  - Predefined and customizable FAQ (`faq_tree`).
  - Dynamic suggestions for similar questions.

---

## How to Run the Frontend

The frontend is a React application managed by Vite.js.

1. **Navigate to the `front-end` directory**:

   ```bash
   cd front-end
   ```

2. **Install dependencies**:
   Use `npm` to install all required packages:

   ```bash
   npm install
   ```

3. **Run the development server**:
   Start the frontend server:

   ```bash
   npm run dev
   ```

4. **Access the frontend**:
   Open your browser and go to:
   [http://localhost:5173](http://localhost:5173)

---

## How to Run the Backend

The backend is a FastAPI application managed by Uvicorn.

1. **Navigate to the `back-end` directory**:

   ```bash
   cd back-end
   ```

2. **Set up a Python virtual environment**:
   Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**:
   Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Required Libraries**:
   Run the following commands to install the required Python libraries:

   ```bash
   pip install fastapi pydantic uvicorn rapidfuzz
   ```

5. **Run the backend server**:
   Start the FastAPI server using Uvicorn:

   ```bash
   uvicorn app:app --reload
   ```

6. **Access the backend**:
   The backend will be running at:
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Features

### Frontend

- **Responsive UI**: Modern design optimized for all devices.
- **Interactive Chat**: Users can type questions or select suggestions for instant responses.
- **Real-time Suggestions**: Dynamic suggestions based on user input.

### Backend

- **Fuzzy Matching**: Uses `RapidFuzz` for accurate query matching.
- **Expandable FAQ**: Easily add or modify questions in `faq_tree`.
- **Simple API Design**: Includes endpoints for querying FAQs and handling user input.

---

## Technologies Used

- **Frontend**: React, Vite.js
- **Backend**: FastAPI, Python, Uvicorn
- **Environment Management**: Virtualenv
- **Fuzzy Matching**: RapidFuzz

---

## FAQ

### How do I add new FAQs?

Edit the `faq_tree` in `back-end/tree.py` to include new questions and answers.

### How do I customize the chatbot's appearance?

Update the `App.css` file in `front-end/src` to modify the styles.

### What are the `.env` files for?

These files store sensitive keys (e.g., API keys) securely and should not be committed to Git. Use `.gitignore` to exclude them.
