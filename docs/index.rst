=========================
Demonstration API Client
=========================

This module provides classes and methods to interact with a demonstration API. The API allows you to fetch, create, and manage demonstrations and their organizers.

Modules
-------

1. :class:`Demonstration`
2. :class:`Organizer`
3. :class:`DemonstrationsClient`

Classes
--------

.. autoclass:: Demonstration
   :members:
   :undoc-members:

.. autoclass:: Organizer
   :members:
   :undoc-members:

.. autoclass:: DemonstrationsClient
   :members:
   :undoc-members:

Class Details
-------------

.. _Demonstration:

Demonstration
--------------

.. autoclass:: Demonstration
   :members:

**Attributes:**

- ``title`` (str): Title of the demonstration.
- ``date`` (str): Date of the demonstration in YYYY-MM-DD format.
- ``start_time`` (str): Start time of the demonstration in HH:MM format.
- ``end_time`` (str): End time of the demonstration in HH:MM format.
- ``topic`` (str): Topic of the demonstration.
- ``city`` (str): City where the demonstration takes place.
- ``address`` (str): Address where the demonstration takes place.
- ``type`` (str): Type of the demonstration.
- ``route`` (str, optional): Route of the demonstration, if applicable.
- ``organizers`` (list of :class:`Organizer`, optional): List of organizers for the demonstration.

**Methods:**

- ``to_dict()``: Converts the `Demonstration` instance into a dictionary.

.. _Organizer:

Organizer
---------

.. autoclass:: Organizer
   :members:

**Attributes:**

- ``name`` (str): Name of the organizer.
- ``email`` (str): Email address of the organizer.
- ``website`` (str, optional): Website of the organizer.

**Methods:**

- ``to_dict()``: Converts the `Organizer` instance into a dictionary.

.. _DemonstrationsClient:

DemonstrationsClient
--------------------

.. autoclass:: DemonstrationsClient
   :members:

**Attributes:**

- ``base_url`` (str): The base URL for the API. Default is ``https://mielenosoitukset.fi/api``.

**Methods:**

- ``get_demonstrations(search=None)``: Fetches all approved demonstrations, optionally filtering by a search term.
  - **Parameters:**
    - ``search`` (str, optional): A search term to filter demonstrations by title, city, topic, or address.
  - **Returns:** A list of demonstrations.
  - **Raises:** `requests.exceptions.RequestException` if the request fails.

- ``get_demonstration(demo_id)``: Fetch a specific demonstration by ID.
  - **Parameters:**
    - ``demo_id`` (str): The ID of the demonstration to fetch.
  - **Returns:** The details of the requested demonstration or a not found message.
  - **Raises:** `requests.exceptions.RequestException` if the request fails.

- ``create_demonstration(demonstration)``: Creates a new demonstration.
  - **Parameters:**
    - ``demonstration`` (:class:`Demonstration`): A `Demonstration` instance.
  - **Returns:** Server response on successful creation.
  - **Raises:** `requests.exceptions.RequestException` if the request fails.

Example Usage
-------------

Here is an example of how to use the `DemonstrationsClient` to create a demonstration and fetch a list of all demonstrations:

```python
from demonstration_api_client import DemonstrationsClient, Demonstration, Organizer

# Initialize the client
client = DemonstrationsClient()

# Create an organizer
organizer = Organizer(name="Jane Doe", email="jane.doe@example.com")

# Create a demonstration
demo = Demonstration(
    title="Climate Strike",
    date="2024-10-01",
    start_time="14:00",
    end_time="16:00",
    topic="Climate Change",
    city="Helsinki",
    address="Central Park",
    demo_type="Protest",
    organizers=[organizer]
)

# Post the demonstration
response = client.create_demonstration(demo)
print(response)

# Fetch all demonstrations
all_demos = client.get_demonstrations()
print(all_demos)

# Fetch a specific demonstration by ID
demo_details = client.get_demonstration(demo_id="12345")
print(demo_details)
```
