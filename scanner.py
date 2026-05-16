import socket

PORT_INFO = {

    20: {
        "service": "FTP Data",
        "risk": "Medium",
        "explanation": "FTP data transfer service detected.",
        "suggestion": "Use secure alternatives like SFTP."
    },

    21: {
        "service": "FTP",
        "risk": "High",
        "explanation": "FTP sends usernames and passwords in plain text.",
        "suggestion": "Use SFTP or FTPS instead."
    },

    22: {
        "service": "SSH",
        "risk": "Medium",
        "explanation": "SSH remote login service is active.",
        "suggestion": "Use strong passwords and SSH keys."
    },

    23: {
        "service": "Telnet",
        "risk": "High",
        "explanation": "Telnet transfers data without encryption.",
        "suggestion": "Disable Telnet and use SSH."
    },

    25: {
        "service": "SMTP",
        "risk": "Medium",
        "explanation": "SMTP mail service detected.",
        "suggestion": "Enable authentication and secure mail configuration."
    },

    53: {
        "service": "DNS",
        "risk": "Medium",
        "explanation": "DNS service is running.",
        "suggestion": "Restrict external DNS queries if unnecessary."
    },

    80: {
        "service": "HTTP",
        "risk": "Medium",
        "explanation": "HTTP traffic is not encrypted.",
        "suggestion": "Use HTTPS instead of HTTP."
    },

    110: {
        "service": "POP3",
        "risk": "Medium",
        "explanation": "POP3 mail service detected.",
        "suggestion": "Use encrypted POP3S."
    },

    143: {
        "service": "IMAP",
        "risk": "Medium",
        "explanation": "IMAP mail service detected.",
        "suggestion": "Use secure IMAPS."
    },

    443: {
        "service": "HTTPS",
        "risk": "Low",
        "explanation": "Secure encrypted web traffic detected.",
        "suggestion": "Keep SSL/TLS certificates updated."
    },

    3306: {
        "service": "MySQL",
        "risk": "High",
        "explanation": "MySQL database service is exposed.",
        "suggestion": "Restrict access to trusted IPs only."
    },

    3389: {
        "service": "RDP",
        "risk": "High",
        "explanation": "Remote Desktop service detected.",
        "suggestion": "Use VPN and strong authentication."
    },

    4444: {
        "service": "Netcat Listener",
        "risk": "High",
        "explanation": "Port commonly used for listeners or testing.",
        "suggestion": "Close this port if not intentionally used."
    },

    5000: {
        "service": "Flask Development Server",
        "risk": "Medium",
        "explanation": "Flask development server is running.",
        "suggestion": "Do not expose development servers publicly."
    }
}


def scan_ports(target, start_port, end_port):

    results = []

    for port in range(start_port, end_port + 1):

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.settimeout(0.3)

            result = s.connect_ex((target, port))

            s.close()

            # OPEN PORT FOUND
            if result == 0:

                # Known port
                if port in PORT_INFO:

                    info = PORT_INFO[port]

                # Unknown port
                else:

                    try:
                        service_name = socket.getservbyport(port)

                    except:
                        service_name = "Unknown Service"

                    info = {
                        "service": service_name,
                        "risk": "Unknown",
                        "explanation": f"Port {port} is open.",
                        "suggestion": "Verify whether this service should be publicly accessible."
                    }

                results.append({

                    "port": port,
                    "service": info["service"],
                    "risk": info["risk"],
                    "explanation": info["explanation"],
                    "suggestion": info["suggestion"]

                })

        except:
            pass

    return results