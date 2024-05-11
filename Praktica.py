import socket
server_socket = socket.socket(socket.AF_INET)
socket.SOCK_STREAM

#  це  метод який створює обьект сокету
# Він вимагає два параметри перший параметр
# Scket.AF_INET вказує на використання мережевого протоколу
# IPv4, а другий параметр socket.SOCK_STREAM
# вказує на використання ТСР (Transmission Control Protocol)
# для забезбечення зєднання з надійним потоком даних клієнтом і
# сервером

#Привязка сокету до IP-адреси та потоку
server_socket.bind(("127,0.0.1",8080))

#Чекаємо на підключення одго клієнта
server_socket.listen(1)
print("Чекаємо зяднання ...")

while True:
    #Приймаємо підключення від клієнта
    client_socket, address= server_socket.accept()
    print(f"Підключення з {address} було створено !")

    #Обмін повідомленнями
    while True:
#Очікуємо отримання повідомлення від кліента

    message = client_socket.recv(1024).decode()
    #Отримуємо дані через сокет від кліента
    #зчитуємо максимум 1024 байти а потіім
    #декодуємо отримані байти у вигляді рядка для
    #подальшого використаняя


    #перевірямо чи клієнт не хоче завершити розмову
    if message.lower() == "exit":
        break
    #виводимо отримане повідомлення від клієнта
    print(f"Client:{message}")

    #Отримаємо відповідь від сервера та надсилаємо клієнту
    responce = input("You:")
    client_socket.send(responce.encode())

    #Повідомлення про завершення розмови
    print("Conversation ended.")

    #Закриваємо зєднання з лієнтом
    client_socket.close()


import socket

#створення сокету клієнта
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Підключення до сервера за IP адрессою та портом
client_socket.connect(("127.0.0.1", 8080))
print("Connected to the server.")
while True:
    #Введення повідомлення для відправки серверу
    message = input("You:")
    #Надсилання повідомлення до сервера
    client_socket.send(message.encode())

    #Перевірка чи клієнт не хоче завершити розмову
    if message.lower() == "exit":
        break
    #Очікування отроимання відповіді від сервера
    response = client_socket.recv(1024).decode()

    #Виведення отриманої відповіді
    print(f"Server:{reponse}")

#Повідомлення про завершення розмови
print("Conversation ended.")

#Закриття зєднання з сервером
client_socket.close()

import multiprocessing
import time
#Функція для обробки завдань
def process_task(task_queue):
    while True:
        task = task_queue.get()
        #Отримати завдання з черги
        if task is None:
    #Якщо завдання закінчилося вийти з циклу
           break
        print(f"Виконуємо завдання:{task}")

        time.sleep(1) #Імітація обролбки завдань
if __name__  == "__main__":
   num_processes = 3 #Кількість процесів для обробки завдань
#Створення черги для завдань
task_queue = multiprocessing.Queue()
#Створення та запуск процесів для обробки завдань
processes = []
for _ in range(num_processes):
    processes = multiprocessing.Process(target=process_task, args=(task_queue,))
    processes.append(process)
    process.start()

    #Додавання черги до черги
    task = ["Завдання1", "Завдання 2",
            "Завдання 3", "Завдання 4", "Завдання 5"]
    for task in task:
        task_queue.put(task)

    #Повідомлення про завершення завдань та очищення черги
    for _ in range(num_processes):
        task_queue.put(None)

    #Очікування завершення процесів
    for process in processes:
        process.join()