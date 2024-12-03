import random
import json
import threading
from tkinter import Tk, Label, Entry, Button, StringVar, Text, END
from tkinter import ttk
from paho.mqtt import client as mqtt_client
import time
import tkinter as tk



class MyWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._name = StringVar()
        self._topic = StringVar()
        self._broker = StringVar(value='test.mosquitto.org')
        self._port = StringVar(value='1883')

        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill='both', expand=True)

        label_broker = ttk.Label(main_frame, text="Broker:")
        label_broker.grid(row=0, column=0, sticky='W', pady=5)
        
        broker_entry = ttk.Entry(main_frame, textvariable=self._broker)
        broker_entry.grid(row=0, column=1, pady=5)
        
        label_port = ttk.Label(main_frame, text="Port:")
        label_port.grid(row=1, column=0, sticky='W', pady=5)
        
        port_entry = ttk.Entry(main_frame, textvariable=self._port)
        port_entry.grid(row=1, column=1, pady=5)
        
        reconnect_button = ttk.Button(main_frame, text="Reconnect", command=self.reconnect)
        reconnect_button.grid(row=2, column=0, columnspan=2, pady=5)

        label_t = ttk.Label(main_frame, text="Topic:")
        label_t.grid(row=3, column=0, sticky='W', pady=5)
        
        topic_entry = ttk.Entry(main_frame, textvariable=self._topic)
        topic_entry.grid(row=3, column=1, pady=5)
        
        button_sub = ttk.Button(main_frame, text="Subscribe", command=self.doSubscribe)
        button_sub.grid(row=4, column=0, columnspan=2, pady=5)
        
        label = ttk.Label(main_frame, text="Message:")
        label.grid(row=5, column=0, sticky='W', pady=5)

        name_entry = ttk.Entry(main_frame, textvariable=self._name)
        name_entry.grid(row=5, column=1, pady=5)
        
        button = ttk.Button(main_frame, text="Publish", command=self.doSomething)
        button.grid(row=6, column=0, columnspan=2, pady=5)

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=7, column=0, columnspan=2, pady=10, sticky='NSEW')
        
        self.text_areas = {}  # Dictionnaire pour stocker les topics et leurs zones de texte

        self.geometry("500x500")
        self.title("MQTT Publisher and Subscriber")
        
        name_entry.bind("<Return>", self.doSomething)
        
        button_log = ttk.Button(main_frame, text="Save Logs", command=self.log)
        button_log.grid(row=8, column=0, columnspan=2, pady=5)

        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(7, weight=1)

    def reconnect(self):
        global client
        client.disconnect()
        client = connect_mqtt(self)
        mqtt_thread = threading.Thread(target=mqtt_loop)
        mqtt_thread.start()

    def doSubscribe(self):
        topic = self._topic.get()
        
        if topic and topic not in self.text_areas:
            self.add_tab(topic)
            client.subscribe(topic)  # Subscribe to the topic
            print(f"Subscribed to {topic}")

    def add_tab(self, topic):
        new_tab = ttk.Frame(self.notebook)
        self.notebook.add(new_tab, text=topic)
        text_area = Text(new_tab, height=10, width=50)
        text_area.pack(expand=True, fill='both')
        self.notebook.select(new_tab)
        self.text_areas[topic] = text_area  # stocke le topic et le text_area associé

    def doSomething(self, event=None):
        msg = {}
        msg["message"] = self._name.get()
        msg["heure"] = time.strftime("%H:%M:%S")
        message = json.dumps(msg)
        topic = self._topic.get()
        if topic in self.text_areas:
            self.text_areas[topic].see(END)  # Faire défiler jusqu'à la fin
            self._name.set("")
            publish(client, message, topic)
        
    def display_message(self, topic, msg):
        if topic in self.text_areas:
            text_area = self.text_areas[topic]
            self.text_areas[topic].insert(END, f"{msg['heure']}: {msg['message']}\n")
            text_area.see(END)  # Faire défiler jusqu'à la fin

    def log(self):
        topic = self._topic.get()
        if topic in self.text_areas:
            text_area = self.text_areas[topic]
            text = text_area.get("1.0", END)
            with open(f"{topic}_messages.txt", "w") as f:
                f.write(text)
            print(f"Saved logs to {topic}.txt")
################# CLIENT MQTT #################

def connect_mqtt(window):
    broker = window._broker.get()
    port = int(window._port.get())
    
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to {broker} at {port} !")
        else:
            print(f"Failed to connect, return code {rc}\n")

    def on_message(client, userdata, msg):
        try:
            message = json.loads(msg.payload)
            print(f"Received `{message}` from `{msg.topic}` topic")
            window.display_message(msg.topic, message)  # Afficher le message dans la fenêtre Tkinter
        except Exception as e:
            print(f"Error processing message: {e}")

    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client

def publish(client, msg, topic="/aparnaudeau"):
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def mqtt_loop():
    client.loop_forever()

window = MyWindow()
client = connect_mqtt(window)

# Démarrer la boucle MQTT dans un thread séparé
mqtt_thread = threading.Thread(target=mqtt_loop)
mqtt_thread.start()

window.mainloop()
