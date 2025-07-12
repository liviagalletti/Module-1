import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()
cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred)
db = firestore.client()

# 2. References to collections
products_ref = db.collection('products')
categories_ref = db.collection('categories')

# 3. CRUD Functions for Categories
def add_category(name):
    doc_ref = categories_ref.document()
    doc_ref.set({'name': name})
    print(f"✅ Category '{name}' added.")

def list_categories():
    docs = categories_ref.stream()
    print("📁 Categories List:")
    for doc in docs:
        data = doc.to_dict()
        print(f"{doc.id}: {data['name']}")

def update_category(doc_id, new_name):
    categories_ref.document(doc_id).update({'name': new_name})
    print(f"🔁 Category '{doc_id}' updated.")

def delete_category(doc_id):
    categories_ref.document(doc_id).delete()
    print(f"❌ Category '{doc_id}' deleted.")

# 4. CRUD Functions for Products
def add_product(name, price, stock=0, category_id=None):
    doc_ref = products_ref.document()
    doc_ref.set({
        'name': name,
        'price': price,
        'stock': stock,
        'category_id': category_id
    })
    print(f"✅ Product '{name}' added.")

def list_products():
    docs = products_ref.stream()
    print("📦 Product List:")
    for doc in docs:
        data = doc.to_dict()
        category_name = "-"
        if data.get('category_id'):
            cat_doc = categories_ref.document(data['category_id']).get()
            if cat_doc.exists:
                category_name = cat_doc.to_dict().get('name', '-')
        print(f"{doc.id}: {data['name']} - ${data['price']} | Stock: {data['stock']} | Category: {category_name}")

def update_product(doc_id, **fields):
    if not fields:
        print("⚠️ No fields to update.")
        return
    products_ref.document(doc_id).update(fields)
    print(f"🔁 Product '{doc_id}' updated.")

def delete_product(doc_id):
    products_ref.document(doc_id).delete()
    print(f"❌ Product '{doc_id}' deleted.")

# 5. Interactive CLI
if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1 - Add product")
        print("2 - List products")
        print("3 - Update product")
        print("4 - Delete product")
        print("5 - Add category")
        print("6 - List categories")
        print("7 - Update category")
        print("8 - Delete category")
        print("0 - Exit")

        op = input("Option: ")
        if op == "1":
            name = input("Name: ")
            price = float(input("Price: ").replace(",", "."))
            stock = int(input("Stock: "))
            print("Select category ID (or leave empty):")
            list_categories()
            category_id = input("Category ID: ") or None
            add_product(name, price, stock, category_id)
        elif op == "2":
            list_products()
        elif op == "3":
            list_products()
            doc_id = input("ID of the product to update: ")
            field = input("Field to update (name, price, stock, category_id): ")
            value = input("New value: ")
            if field == "price":
                value = float(value.replace(",", "."))
            elif field == "stock":
                value = int(value)
            update_product(doc_id, **{field: value})
        elif op == "4":
            list_products()
            doc_id = input("ID of the product to delete: ")
            delete_product(doc_id)
        elif op == "5":
            name = input("Category name: ")
            add_category(name)
        elif op == "6":
            list_categories()
        elif op == "7":
            list_categories()
            doc_id = input("ID of the category to update: ")
            new_name = input("New category name: ")
            update_category(doc_id, new_name)
        elif op == "8":
            list_categories()
            doc_id = input("ID of the category to delete: ")
            delete_category(doc_id)
        elif op == "0":
            print("Exiting... 👋")
            break
        else:
            print("❗ Invalid option.")
