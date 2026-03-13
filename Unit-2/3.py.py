import logging

# Configure logging
logging.basicConfig(filename="error_log.txt",
                    level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError as e:
    print("Arithmetic Exception Occurred:", e)
    logging.error("Exception occurred", exc_info=True)
