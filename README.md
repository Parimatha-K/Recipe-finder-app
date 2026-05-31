# Recipe Finder Application

A web application built with Python and Flask that allows 
users to search for recipes and view detailed information 
using the Spoonacular API.

## Features
- Search recipes by dish name
- View detailed recipe information
- Displays ingredients and cooking instructions
- Clean and user-friendly interface

## Tech Stack
- Python
- Flask
- Spoonacular API
- HTML/CSS

## Project Structure
recipe_project/
├── app.py
├── templates/
│   ├── index.html
│   └── recipe_detail.html

## How to Run
1. Install dependencies: pip install flask requests python-dotenv
2. Get your API key from https://spoonacular.com/
3. Create a .env file and add: API_KEY=your_api_key_here
4. Run the app: python app.py
5. Open browser: http://localhost:5000
