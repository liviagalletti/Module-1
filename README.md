# Overview

This software is designed to help me deepen my skills as a software engineer by building a simple inventory management system that interacts with a cloud database. The program integrates with Google Firebase Firestore to perform basic operations such as adding, listing, updating, and deleting products and categories.

The system allows management of products that are related to categories stored in Firestore, demonstrating how to model and interact with related data in a NoSQL cloud database.

To use the program, simply run the Python script and use the interactive command-line menu to manage products and categories.

[Software Demo Video](https://youtu.be/muFiv3AQxh8)

---

# Cloud Database

This project uses **Google Firebase Firestore** as the cloud database service. Firestore is a NoSQL document database that stores data in collections and documents, providing scalable and flexible cloud storage accessible via API.

The database structure consists of two main collections:

- `categories`: stores category documents with a `name` field.
- `products`: stores product documents with fields for `name`, `price`, `stock`, and `category_id` which references the related category document ID.

This structure demonstrates a simple one-to-many relationship from categories to products.

---

# Development Environment

The software was developed using:

- **Python 3.x** as the programming language.
- The **firebase-admin** library to interact with Firestore from Python.
- The **python-dotenv** library to load environment variables including Firebase service account credentials.
- Firebase Console to create the project, Firestore database, and download the service account JSON key.

---

# Useful Websites

- [Firebase Official Documentation](https://firebase.google.com/docs/firestore)
- [Python Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
- [Firestore Data Modeling](https://firebase.google.com/docs/firestore/data-model)
- [python-dotenv GitHub](https://github.com/theskumar/python-dotenv)

---

# Future Work

- Implement user authentication to secure database access.
- Add real-time listeners to receive notifications when data changes.
- Develop a graphical user interface (GUI) or web frontend.
- Improve error handling and input validation in the CLI.
- Expand product data with more attributes like description or images.
"""
