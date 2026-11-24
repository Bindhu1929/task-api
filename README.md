\# Task API



A simple CRUD REST API built using Python and FastAPI.



\## Features

\- Create a task

\- View all tasks

\- View a task by ID

\- Update a task

\- Delete a task

\- Health check endpoint



\## Technologies

\- Python 3.13

\- FastAPI

\- Uvicorn



\## Installation



```bash

pip install -r requirements.txt

```



\## Run the application



```bash

python -m uvicorn main:app --reload --port 8000

```



\## API Documentation



Open http://127.0.0.1:8000/docs



\## Endpoints



| Method | Endpoint | Description |

|---|---|---|

| GET | / | API information |

| GET | /health | Health check |

| GET | /tasks | Get all tasks |

| GET | /tasks/{task\_id} | Get one task |

| POST | /tasks | Create a task |

| PUT | /tasks/{task\_id} | Update a task |

| DELETE | /tasks/{task\_id} | Delete a task |



\## Storage



Tasks are stored in an in-memory Python list. Data resets when the server restarts.

