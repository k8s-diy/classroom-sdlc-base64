import base64

# Список етапів SDLC
steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

# Функція кодування у base64
def encode_base64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

# Функція декодування з base64
def decode_base64(encoded: str) -> str:
    return base64.b64decode(encoded.encode()).decode()

# Основна логіка: виведення етапів
def print_encoded_steps(steps):
    for i, step in enumerate(steps, 1):
        encoded = encode_base64(step)
        print(f"{i}. {step} -> {encoded}")

# Автоматизований тест
def test_base64_encoding():
    for step in steps:
        encoded = encode_base64(step)
        decoded = decode_base64(encoded)
        assert decoded == step, f"Test failed: {step} -> {encoded} -> {decoded}"
    print("✅ All tests passed.")

# Точка входу
if __name__ == "__main__":
    print_encoded_steps(steps)
    print()  # Порожній рядок для зручності
    test_base64_encoding()
