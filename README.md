# Real-Time-Chat-Applications
A simple multi-client chat server built using Python’s socket and threading module

# Chat Server

A simple multi-client chat server built in Python using sockets and threading. This project allows multiple clients to connect simultaneously, exchange messages, and receive automatic replies from the server.

## Overview

This chat server accepts multiple client connections and broadcasts messages sent by one client to all others. It includes an auto-reply feature that responds to common user inputs like "hello", "bye", and "help". The server can handle client disconnections gracefully.

## Features

- **Multi-client Support**: Multiple clients can connect to the server and send messages simultaneously.
- **Broadcasting**: Messages sent by a client are broadcast to all other connected clients.
- **Auto-reply System**: The server replies with preset responses based on certain inputs from clients:
  - "hello" or "hi" → "Hello there! How can I help you today?"
  - "bye" → "Goodbye! Have a great day!"
  - "help" → "Sure! I'm here to help. Ask me anything."
  - Default reply for unrecognized messages.
- **Graceful Client Disconnection**: The server detects when a client disconnects and broadcasts the user's departure to all others.

## Technologies Used

- Python 3.x
- `socket` module for network communication
- `threading` module for handling multiple clients concurrently


server, sends messages, and displays replies.

Contributions

### Key Sections in This README:

1. **Overview**: A simple description of the project functionality and its purpose.
2. **Features**: Highlights key features, such as multi-client support, broadcasting, auto-reply, and graceful client disconnection.
3. **Technologies**: Lists the technologies used in the project.
4. **Setup Instructions**: A clear, step-by-step guide to cloning and running the server and client.
5. **Usage**: Explains how to interact with the server and client.
6. **Example**: Shows what you should expect in terms of output when running the server and client.
7. **Code Structure**: Describes the main scripts in the project.
8. **Contributions**: Encourages others to contribute to the project.
9. **License**: Provides a license (MIT License in this case).

