import random
import requests

def generate_code(length: int = 6) -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(length))

def read_from_sum(path: str = "test.txt") -> int:
    with open(path,"r") as f:
        lines = [int(line.strip()) for line in f]