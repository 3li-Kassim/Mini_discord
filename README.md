# Mini Discord

A real-time chat application built with Python that enables multiple users to communicate over a local network. Features a GUI interface and supports concurrent connections using socket programming and threading.

## Features

- **Real-time messaging** - Send and receive messages instantly
- **Multi-client support** - Multiple users can connect and chat simultaneously
- **User identification** - Custom usernames for each chat participant
- **Clean GUI** - Built with Tkinter for an intuitive chat interface
- **Thread-safe messaging** - Uses queues to handle concurrent message receiving

## Tech Stack

- **Python 3.13**
- **Socket Programming** - For network communication
- **Threading** - Handles multiple client connections
- **Tkinter** - GUI framework
- **Queue** - Thread-safe message handling

## How It Works

The application uses a client-server architecture:

1. **Server** - Listens for incoming connections and broadcasts messages to all connected clients
2. **Client** - Connects to the server, sends messages, and displays incoming messages in real-time

## Installation & Setup

### Prerequisites
- Python 3.x installed on your system

### Running the Application

1. **Start the Server**
   ```bash
   python server.py
   ```

2. **Start Client(s)** (in separate terminal windows)
   ```bash
   python client.py
   ```

3. **Enter your username** when prompted

4. **Start chatting!**

## Project Structure

```
Mini_Discord/
├── server.py       # Server-side socket handling and message broadcasting
├── client.py       # Client connection and message sending
└── client_gui.py   # Tkinter GUI interface
```

## Current Limitations

- Currently supports **local network only** (localhost: 127.0.0.1)
- Requires manual server startup before clients can connect

## Future Improvements

- [ ] Internet connectivity via port forwarding or tunneling service
- [ ] Message history persistence
- [ ] Private messaging between users
- [ ] User status indicators (online/offline)
- [ ] File sharing capabilities
- [ ] Emoji support

## Learning Outcomes

This project helped me understand:
- Socket programming and network protocols
- Multi-threading and concurrency
- Thread-safe data structures
- Client-server architecture
- GUI development with Tkinter
- Real-time communication systems

## Author

Built as a portfolio project to demonstrate backend development skills and understanding of networked applications.

---

*Note: This is a learning project built to understand networking concepts. For production use, additional security measures and error handling would be required.*
