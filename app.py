from flask import Flask, render_template, request
from scanner import scan_ports
import socket

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    results = None
    target = ""
    error = ""

    if request.method == "POST":

        target = request.form.get("target", "").strip()

        try:
            start_port = int(request.form.get("start_port"))
            end_port = int(request.form.get("end_port"))

            # Validate IP / hostname
            try:
                socket.gethostbyname(target)

            except:
                error = "Invalid IP address or hostname."

            # Validate port range
            if not error:

                if start_port < 1 or end_port > 65535:
                    error = "Ports must be between 1 and 65535."

                elif start_port > end_port:
                    error = "Start port cannot be greater than end port."

                elif (end_port - start_port) > 10000:
                    error = "Please scan smaller ranges."

                else:
                    # Start scanning
                    results = scan_ports(
                        target,
                        start_port,
                        end_port
                    )

        except ValueError:
            error = "Please enter valid port numbers."

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template(
        "index.html",
        results=results,
        target=target,
        error=error
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )