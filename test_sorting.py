import requests

def test_sort_tasks():
    url = "http://localhost:5000/sort"

    tasks = [
        {"title": "Do programming"},
        {"title": "Attend group meeting 31"},
        {"title": "Clean your room"}
    ]

    # Test default task order
    print("Default order:", tasks, "\n")

    # Test ascending
    ascending_order = {
        "tasks": tasks,
        "sort_field": "title",
        "order": "asc"
    }
    response = requests.post(url, json=ascending_order)
    print("Ascending sort response:", response.json(), "\n")

    # Test descending
    descending_order = {
        "tasks": tasks,
        "sort_field": "title",
        "order": "desc"
    }
    response = requests.post(url, json=descending_order)
    print("Descending sort response:", response.json())


if __name__ == "__main__":
    test_sort_tasks()