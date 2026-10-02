# Simple SSH Credential Capture Server

A minimal SSH server built with **Python** and **Paramiko** that logs attempted username/password credentials.

## Usage

```bash
python3 server.py
```

The server listens on **port 2222** and prints authentication attempts as:

```text
username:password
```
