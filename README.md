# OWremote

OWremote is a Python-based tool designed for QA automation. It provides functionality similar to PsExec, allowing you to execute processes on remote systems using APIs and WebSockets for an interactive terminal experience on Windows.

## Features

- Execute commands on remote systems via RESTful API.
- Interactive terminal using WebSockets.
- Secure communication with authentication mechanisms.
- Built with Flask and Flask-SocketIO for real-time communication.
- Supports WebSocket transport for improved performance.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/OWremote.git
    cd OWremote
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Servers

1. **Run the Flask API Server**:
    ```bash
    # In a separate terminal
    python app.py
    ```

2. **Run the WebSocket Server**:
    ```bash
    # In a separate terminal
    python socket_server.py
    ```

### Running Clients

1. **WebSocket Client**:
    ```bash
    python ws_client.py
    ```

2. **API Client**:
    ```bash
    python api_client.py
    ```

## Project Structure

- `app.py`: Contains the Flask API server setup for executing commands via RESTful API.
- `socket_server.py`: Contains the WebSocket server setup for real-time command execution.
- `ws_client.py`: WebSocket client for interacting with the WebSocket server.
- `api_client.py`: API client for sending command execution requests to the Flask API server.
- `requirements.txt`: Lists the dependencies required for the project.

## Dependencies

- Flask
- Flask-SocketIO
- Paramiko
- python-socketio
- Requests
- websocket-client
- gevent
- gevent-websocket

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgements

Inspired by PsExec and built with Flask, Flask-SocketIO, and other open-source technologies.
