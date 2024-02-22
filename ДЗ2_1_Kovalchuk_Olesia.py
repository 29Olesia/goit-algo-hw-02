import queue
import threading
import time
import random

request_queue = queue.Queue()

def generate_request():
    """Генерація нової заявки та додавання її до черги."""
    new_request = {"id": unique_id_generator(), "timestamp": time.time()}
    request_queue.put(new_request)
    print(f"Заявка {new_request['id']} додана до черги.")

def process_request():
    """Обробка заявок у черзі."""
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Обробка заявки {current_request['id']}...")
        print(f"Заявка {current_request['id']} успішно оброблена.")
    else:
        print("Черга порожня. Очікування нових заявок.")

def unique_id_generator():
    """Генерація унікального ідентифікатора."""
    return str(int(time.time() * 1000)) + str(random.randint(1, 1000))

def get_user_input():
    """Функція потоку для отримання вводу користувача."""
    global stop_flag
    while True:
        user_input = input("Введіть 'exit' та Enter, щоб завершити програму: ")
        if user_input.lower() == 'exit':
            stop_flag = True
            break

stop_flag = False

def main():
    global stop_flag
    user_input_thread = threading.Thread(target=get_user_input)
    user_input_thread.start()

    try:
        while not stop_flag:
            generate_request()
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")
    finally:
        user_input_thread.join()  

if __name__ == "__main__":
    main()
