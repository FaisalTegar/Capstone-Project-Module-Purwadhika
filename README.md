
# 🏢 Employee Management System (Capstone Project)

This is a simple Python console program to manage employee data for a fictional company. Built as a capstone project, it focuses on fundamental Python skills including data structures, control flow, input validation, and basic user interaction.

---

## 🚀 Features

- 📋 Display employee list
- ➕ Add a new employee (with validation for name and position)
- ❌ Remove employee by NIP (employee ID)
- 📈 Promote employee (with salary increase requirement)

---

## 📌 Data Structure

The program uses a Python dictionary (`dk`) to store employee information:

```python
dk = {
  "NIP": [1001, 1002, ...],
  "Nama": ["Budi", "John", ...],
  "Umur": [35, 28, ...],
  "Jabatan": ["Manager", "Akuntan", ...],
  "Gaji": [10000000, 8000000, ...]
}
```

---

## 🧠 How It Works

1. **Main Menu Loop**: User selects from 5 options.
2. **Data Validation**:
   - Duplicate names and positions are restricted.
   - Age and salary inputs are validated as numbers.
3. **Formatting**: Gaji is formatted in Indonesian Rupiah.

---

## 📦 Requirements

No external libraries needed—just run it with Python 3:

```bash
python filename.py
```

---

## ✍️ Author

**Faisal Tegar Febrian**  
Capstone Project - Purwadhika Bootcamp  
LinkedIn: [faisal-tegar-febrian](https://www.linkedin.com/in/faisal-tegar-febrian-a46b13a0)

---

## 🧾 License

This project is for educational purposes only.
