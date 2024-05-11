import threading
import json
from googletrans import Translator

import socket
#Завдання 1
# Реалізуйте клієнт-серверний додаток з можливістю
# зворотного обміну повідомленнями. Для початку спілкування встановіть з’єднання. Після з’єднання використайте текстовий формат. У бесіді беруть участь лише дві
# особи. Після завершення спілкування сервер переходить
# до очікування нового учасника розмови.
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Сервер запущено. Очікування з'єднання...")

    while True:
        connection, address = server_socket.accept()
        print("З'єднання від:", address)

        while True:
            message = connection.recv(1024).decode()
            if not message:
                print("Клієнт відключився")
                break
            print("Клієнт:", message)

            response = input("Введіть відповідь сервера: ")
            connection.send(response.encode())

        connection.close()

if __name__ == "__main__":
    start_server()


#Завдання 2
# Реалізуйте клієнт-серверний додаток погоди. Клієнт
# звертається до сервера із зазначенням країни та міста.
# Сервер, отримавши запит, видає погоду на тиждень для
# вказаної місцевості. Використовуйте для реалізації додатку багатопотокові механізми. Дані про погоду мають
# бути наперед визначеними та взяті з файлу.

def handle_client(client_socket, city):
    try:

        with open("weather_data.json", "r") as file:
            weather_data = json.load(file)
            city_weather = weather_data.get(city)
            if city_weather:
                response = json.dumps(city_weather)
            else:
                response = "Погода для вказаного міста не знайдена."

        client_socket.send(response.encode())
    except Exception as e:
        print("Помилка обробки запиту:", e)
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Сервер запущено. Очікування з'єднання...")

    while True:
        client_socket, address = server_socket.accept()
        print("З'єднання від:", address)

        client_thread = threading.Thread(target=handle_client, args=(client_socket, "Kyiv"))
        client_thread.start()

if __name__ == "__main__":
    start_server()

#Завдання 3
# Створіть клієнтсько-серверний додаток, де клієнт
# надсилає рядок тексту або слово на сервер для
# перекладу на іншу мову. Сервер повертає переклад і
# відправляє його клієнту. Наприклад, клієнт надсилає
# рядок "Hello, how are you?" на сервер, а сервер повертає
# переклад цього рядка на вказану мову. Скористайтеся
# бібліотекою googletrans.
def translate_text(text, dest_language='uk'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language).text
    return translated_text

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        if data:
            print("Текст від клієнта:", data)
            translated_text = translate_text(data)
            client_socket.send(translated_text.encode())
    except Exception as e:
        print("Помилка обробки запиту:", e)
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Сервер запущено. Очікування з'єднання...")

    while True:
        client_socket, address = server_socket.accept()
        print("З'єднання від:", address)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
