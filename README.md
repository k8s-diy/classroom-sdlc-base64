# 🧪 Завдання: Кодування етапів SDLC у Base64

## 📚 Опис

У цьому завданні ви попрактикуєтесь у роботі зі списками, циклами, функціями та кодуванням у форматі Base64.

Вам надано список етапів життєвого циклу розробки програмного забезпечення (SDLC):

```python
["plan", "code", "test", "delivery", "deploy", "monitor"]
```

## 🎯 Завдання

1. Напишіть функцію `encode_base64(text: str) -> str`, яка кодує текст у формат Base64 (тип повернення — **рядок**).
2. Напишіть функцію `decode_base64(encoded: str) -> str`, яка виконує зворотне декодування.
3. Виведіть кожен етап у форматі:

```
1. plan -> cGxhbg==
2. code -> Y29kZQ==
...
```

4. Створіть функцію `print_encoded_steps(steps: list)`, яка виводить список з кроками у зазначеному форматі.
5. Реалізуйте тест `test_base64_encoding()`, який перевіряє, що:
   ```python
   decode_base64(encode_base64(step)) == step
   ```
   для кожного етапу.

## ✅ Очікуваний результат

```bash
1. plan -> cGxhbg==
2. code -> Y29kZQ==
3. test -> dGVzdA==
4. delivery -> ZGVsaXZlcnk=
5. deploy -> ZGVwbG95
6. monitor -> bW9uaXRvcg==

✅ All tests passed.
```

## 📁 Файлова структура

Ваша структура репозиторію має виглядати так:

```
.
├── main.py            # основна логіка
├── README.md          # (цей файл)
```

## 🧪 Як запускати

Запустіть файл командою:

```bash
python3 main.py
```

## 💡 Порада

Використовуйте модуль `base64`, який вже є в стандартній бібліотеці Python.

```python
import base64

# Кодування
encoded = base64.b64encode("text".encode()).decode()

# Декодування
decoded = base64.b64decode(encoded.encode()).decode()
```
---

Успіхів! 🚀
