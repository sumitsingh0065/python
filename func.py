# Dataset: lesser-known women who were "firsts" after 1950
women_firsts = [
    {
        "name": "Anna Rajam Malhotra",
        "country": "India",
        "year": 1951,
        "field": "Public Service",
        "achievement": "First woman Indian Administrative Service officer"
    },
    {
        "name": "Mary Kenneth Keller",
        "country": "USA",
        "year": 1965,
        "field": "Science & Education",
        "achievement": "First woman to earn a PhD in Computer Science"
    },
    {
        "name": "Fatima Beevi",
        "country": "India",
        "year": 1989,
        "field": "Judiciary",
        "achievement": "First woman judge of the Supreme Court of India"
    },
    {
        "name": "Mary Jackson",
        "country": "USA",
        "year": 1958,
        "field": "Science",
        "achievement": "First Black female engineer at NASA"
    }
]

# Function to filter by field
def filter_by_field(data, field_name):
    return [entry for entry in data if entry["field"].lower() == field_name.lower()]

# Function to display all entries nicely
def display_entries(data):
    for person in data:
        print(f"{person['name']} ({person['year']})")
        print(f"  Field: {person['field']}")
        print(f"  Achievement: {person['achievement']}")
        print("-" * 40)

# Example usage
print("All pioneers:\n")
display_entries(women_firsts)

print("\nScience-related pioneers:\n")
science_pioneers = filter_by_field(women_firsts, "Science")
display_entries(science_pioneers)
