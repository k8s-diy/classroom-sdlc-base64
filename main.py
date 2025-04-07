import base64

# TODO: Реалізуйте функцію encode_base64(text: str) -> str
def encode_base64(text: str) -> str:
    pass  # замініть цю строчку своєю реалізацією

# TODO: Реалізуйте функцію decode_base64(encoded: str) -> str
def decode_base64(encoded: str) -> str:
    pass  # замініть цю строчку своєю реалізацією

# TODO: Реалізуйте функцію для виводу етапів SDLC у форматі base64
def print_encoded_steps(steps: list):
    pass  # замініть цю строчку своєю реалізацією

# Автоматизований тест — не змінюйте!
def test_base64_encoding():
    steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]
    for step in steps:
        encoded = encode_base64(step)
        decoded = decode_base64(encoded)
        assert decoded == step, f"Test failed: {step} -> {encoded} -> {decoded}"
    print("✅ All tests passed.")

# Точка входу
if __name__ == "__main__":
    steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]
    print_encoded_steps(steps)
    print()
    test_base64_encoding()
