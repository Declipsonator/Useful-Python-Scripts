"""
    This is a simple GUI app that allows you to send HTTP requests.
    It's useful for testing APIs.
    We can remove it, but I didn't know of any good apps for this type of thing,
    so I just had chatgpt do it. (:
"""

import tkinter as tk
import requests


def parse_text_input(input_str):
    lines = input_str.strip().split("\n")
    headers = {}
    for line in lines:
        parts = line.split(":")
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
            headers[key] = value
    return headers


def do_request(url, method="POST", headers=None, body=None, params=None):
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=body, params=params)
        else:
            response = requests.post(url, headers=headers, data=body, params=params)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)


class RequestApp:
    def __init__(self, master):
        self.master = master
        master.title("HTTP Request App")

        # URL input
        self.url_label = tk.Label(master, text="URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack()

        # Headers input
        self.headers_label = tk.Label(master, text="Headers:")
        self.headers_label.pack()
        self.headers_text = tk.Text(master, width=50, height=5)
        self.headers_text.pack()
        self.headers_text.insert(tk.END, "Content-Type: application/json\nAuthorization: Bearer my_token")

        # Body input
        self.body_label = tk.Label(master, text="Body:")
        self.body_label.pack()
        self.body_text = tk.Text(master, width=50, height=5)
        self.body_text.pack()
        self.body_text.insert(tk.END, "{\n\n}")

        # Parameters input
        self.params_label = tk.Label(master, text="Parameters:")
        self.params_label.pack()
        self.params_text = tk.Text(master, width=50, height=5)
        self.params_text.pack()
        self.params_text.insert(tk.END, "{\n\n}")

        # Method selection
        self.method_label = tk.Label(master, text="Method:")
        self.method_label.pack()
        self.method_var = tk.StringVar(value="POST")
        self.method_radio_post = tk.Radiobutton(master, text="POST", variable=self.method_var, value="POST")
        self.method_radio_post.pack()
        self.method_radio_get = tk.Radiobutton(master, text="GET", variable=self.method_var, value="GET")
        self.method_radio_get.pack()
        self.method_radio_put = tk.Radiobutton(master, text="PUT", variable=self.method_var, value="PUT")
        self.method_radio_put.pack()

        # Button to send request
        self.send_button = tk.Button(master, text="Send Request", command=self.send_request)
        self.send_button.pack()

        # Response output
        self.response_label = tk.Label(master, text="Response:")
        self.response_label.pack()
        self.response_text = tk.Text(master, width=50, height=10)
        self.response_text.pack()

    def send_request(self):
        # Get inputs
        global response
        url = self.url_entry.get()
        headers = parse_text_input(self.headers_text.get("1.0", "end"))
        body = self.body_text.get("1.0", "end").strip()
        params = parse_text_input(self.params_text.get("1.0", "end"))

        # Determine request method
        if self.method_var.get() == "POST":
            # Send POST request
            response = do_request(url, headers=headers, body=body, params=params)
        elif self.method_var.get() == "GET":
            # Send GET request
            response = do_request(url, headers=headers, params=params)
        elif self.method_var.get() == "PUT":
            # Send PUT request
            response = do_request(url, headers=headers, data=body, params=params)

        # Display response
        self.response_text.delete("1.0", "end")
        self.response_text.insert("1.0", response)


root = tk.Tk()
app = RequestApp(root)
root.mainloop()
