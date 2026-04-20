# HENNGE Backend Challenge – Solution

## 📌 Overview

This repository contains my solution for the **HENNGE Backend / DevSecOps / Internship Coding Challenge**.

The challenge consists of three missions:

1. Implement a program based on given constraints
2. Publish the solution as a secret GitHub Gist
3. Submit the solution via an authenticated API request

---

## 🧩 Mission 1: Problem Description

The program processes multiple test cases. For each test case:

* Read an integer `X`
* Read `X` space-separated integers
* Identify **negative integers only**
* Compute the **fourth power (n⁴)** of each negative integer
* Output the **sum of these values**

### ⚠️ Constraints

* No `for` loops
* No `while` loops
* No list/set/dictionary comprehensions
* Must use **recursion**
* Input is taken from **standard input**
* Output is printed to **standard output**

### ✅ Edge Case Handling

* If the number of integers does not match `X`, output `-1`

---

## 💡 Approach

* Used **recursion** to:

  * Process each test case
  * Traverse the list of integers
* Filtered only **negative values**
* Computed powers using `n ** 4`
* Ensured strict adherence to input/output format

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries Used:** Standard Library only (as required)

---

## ▶️ How to Run

1. Save the file as:

   ```
   main.py
   ```

2. Run the program:

   ```
   python main.py
   ```

3. Provide input via standard input:

   ```
   2
   4
   3 -1 1 10
   5
   9 -5 -5 -10 10
   ```

4. Expected output:

   ```
   1
   11250
   ```

---

## 🔐 Mission 2: GitHub Gist

* The solution is published as a **secret gist** to maintain confidentiality.
* Only a single file (`main.py`) is included as required.

---

## 🚀 Mission 3: API Submission

A JSON payload is created with:

* GitHub Gist URL
* Contact Email
* Solution Language

The request is sent via:

* **HTTP POST**
* **Basic Authentication**
* **TOTP (RFC6238) with SHA-512**

---

## 📎 Notes

* The solution strictly follows all constraints mentioned in the challenge.
* No global variables were used.
* Focus was on correctness, simplicity, and compliance with rules.

---

## 👤 Author

**Shivakrishna Merugu**
Aspiring Software Engineer | 2025 Graduate

---

## 📄 License

This project is part of a private coding challenge and is not intended for public distribution.
