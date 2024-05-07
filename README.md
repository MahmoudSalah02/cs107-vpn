# Developing and Improving a Virtual Private Network (VPN)

By: Xianmai Liang, Ao Chan, Mahmoud Salah

## Overview

This repository contains Python server files for a project that integrates an HTTP server with OpenVPN. The OpenVPN setup is required for secure communication and must be configured internally following these steps:

## OpenVPN Configuration

1. **Server Installation**: Install OpenVPN using `apt-get install openvpn`.
2. **Certificates and Keys**: Generate CA, server, and client certificates and keys using OpenSSL.
3. **Server Configuration**: Set up the `server.conf` with directives like `ca`, `cert`, `key`, `dh`, and `AES-256-CBC` encryption.
4. **Client Configuration**: Distribute `client.conf` files with the necessary certificates and keys.
5. **Connection Establishment**: Start the server with `systemctl start openvpn@server` and connect clients using their configuration files.

## Running the Python Server

Ensure the VPN is configured and active. Run the Python server with:

```bash
python3 server.py
```

This will start the HTTP server, handling requests based on predefined IP restrictions and custom error responses.

