
import json
import socket
#Завдання 1
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Підключено до сервера.")

    while True:
        message = input("Введіть повідомлення: ")
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print("Сервер:", response)

        if message.lower() == 'exit':
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()

#Завдання 2

def get_weather(city):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    try:
        client_socket.send(city.encode())
        response = client_socket.recv(1024).decode()
        weather_data = json.loads(response)
        print(f"Погода в місті {city}:")
        for day, weather in weather_data.items():
            print(f"{day}: {weather}")
    except Exception as e:
        print("Помилка отримання погоди:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    city = input("Введіть місто: ")
    get_weather(city)

#Завдання 3
def send_text_to_server(text):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    try:
        client_socket.send(text.encode())

        translated_text = client_socket.recv(1024).decode()
        print("Переклад:", translated_text)
    except Exception as e:
        print("Помилка відправки тексту на сервер:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    text = input("Введіть текст для перекладу: ")
    send_text_to_server(text)