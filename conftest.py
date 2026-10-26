import pytest 
import os

@pytest.fixture(scope="function")
def create_file():
    path ="test.txt"
    with open(path, "w") as f:
        f.writelines(str(x) + "\n" for x in range(6))
    yield path
    os.remove(path)