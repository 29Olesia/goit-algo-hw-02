from collections import deque

def is_palindrome(input_str):
    """Перевіряє, чи є рядок паліндромом."""
    clean_str = ''.join(char.lower() for char in input_str if char.isalnum())  
    char_deque = deque(clean_str)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False 
    
    return True  

def main():
    while True:
        user_input = input("Введіть перевірку на паліндром (або 'exit' для виходу): ")
        
        if user_input.lower() == 'exit':
            print("Програма завершує роботу.")
            break
        
        if is_palindrome(user_input):
            print("Рядок є паліндромом.")
        else:
            print("Рядок не є паліндромом.")

if __name__ == "__main__":
    main()
