import requests

class Demonstration:
    def __init__(self, title, date, start_time, end_time, topic, city, address, demo_type, route=None, organizers=None):
        self.title = title
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.topic = topic
        self.city = city
        self.address = address
        self.type = demo_type
        self.route = route
        self.organizers = organizers if organizers else []

    def to_dict(self):
        """
        Converts the Demonstration instance into a dictionary.
        
        :return: A dictionary representation of the demonstration.
        """
        return {
            "title": self.title,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "topic": self.topic,
            "city": self.city,
            "address": self.address,
            "type": self.type,
            "route": self.route,
            "organizers": [organizer.to_dict() for organizer in self.organizers]
        }


class Organizer:
    def __init__(self, name, email, website=""):
        self.name = name
        self.email = email
        self.website = website

    def to_dict(self):
        """
        Converts the Organizer instance into a dictionary.
        
        :return: A dictionary representation of the organizer.
        """
        return {
            "name": self.name,
            "email": self.email,
            "website": self.website
        }


class DemonstrationsClient:
    def __init__(self, base_url="https://mielenosoitukset.fi/api"):
        self.base_url = base_url

    def get_demonstrations(self, search=None):
        """
        Fetches all approved demonstrations, optionally filtering by a search term.
        
        :param search: A search term to filter demonstrations by title, city, topic, or address.
        :return: A list of demonstrations.
        """
        url = f"{self.base_url}/demonstrations"
        params = {}
        if search:
            params['search'] = search

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_demonstration(self, demo_id):
        """
        Fetch a specific demonstration by ID.
        
        :param demo_id: The ID of the demonstration to fetch.
        :return: The details of the requested demonstration.
        """
        url = f"{self.base_url}/demonstration/{demo_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return f"Demonstration with ID {demo_id} not found or not approved."
        else:
            response.raise_for_status()

    def create_demonstration(self, demonstration):
        """
        Creates a new demonstration.
        
        :param demonstration: A Demonstration instance.
        :return: Server response on successful creation.
        """
        url = f"{self.base_url}/demonstration"
        response = requests.post(url, json=demonstration.to_dict())
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()
