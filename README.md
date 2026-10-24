<div align="center">

<img width ="100%" src ="https://capsule-render.vercel.app/api?type=waving&color=0:f1f3f6,50:e3e8ee,100:d3dbe5&height=230&section=header&text=infosec-modulo&fontColor=0e1621&fontSize=46&fontAlignY=40&desc=Classical+and+Modern+Ciphers+%E2%80%94+Built+From+Scratch+in+Python&descAlignY=63&descColor=0b721e&animation=fadeIn&fontFamily=Georgia"/>

<br/>

![Language](https://img.shields.io/badge/Language-Python_3-0b7285?style=for-the-badge&logo=python&logoColor=white&labelColor=0e1621)
![Focus](https://img.shields.io/badge/Focus-Ciphers_%26_Modular_Arithmetic-5b6b7d?style=for-the-badge&labelColor=0e1621)
![Semester](https://img.shields.io/badge/Semester-4-0b7285?style=for-the-badge&labelColor=0e1621)
![Ciphers](https://img.shields.io/badge/Ciphers-5_Implemented-5b6b7d?style=for-the-badge&labelColor=0e1621)
![Status](https://img.shields.io/badge/Status-🔨_Actively_Growing-0b7285?style=for-the-badge&labelColor=0e1621)

<br/><br/>

> *"The enemy knows the system."*
> — **Claude Shannon** *(so every cipher here has to survive that assumption — and the classical ones don't)*

<br/>

</div>

---

## ◈ What Lives Here

Classical and modern ciphers, implemented from scratch in **Python** for my Information Security lab — Semester 4, Fall 2026. Each one a self-contained script that both **encrypts and decrypts**.

Reading about a cipher and implementing it are very different things. So there are no cryptography libraries doing the work here — just the logic, the key handling, and the modular arithmetic underneath. That's also where the name comes from: nearly every classical cipher is, at its core, arithmetic **modulo** n.

Every script is built to answer three questions: how does the cipher turn plaintext into ciphertext, how does the key shape that transformation, and how do you reverse it — and why is it (or isn't it) secure?

Not archived. One cipher lands per lab, and this repo grows with the course.

---

## ◈ Vault Structure

```
infosec-modulo/
│
└── 🔤 substitution/
        └── caesar/
            └── caesar.py
```

Ciphers are grouped by **type**, one folder per cipher. New labs go into the matching group — a new group only appears when a genuinely new category of cipher shows up.

## ◈ Chapter Breakdown

<details>
<summary><b>🔤 Substitution &nbsp;|&nbsp; Swap Every Symbol</b></summary>
<br/>

Ciphers that replace each plaintext symbol with another symbol. The key decides which one.

| Cipher | Type | Key | Core Idea |
|---|---|---|---|
| **Caesar** | Monoalphabetic | An integer shift `k` | Shift every letter by a fixed number of positions: `E(x) = (x + k) mod 26` |

> *The whole chapter is one escalating argument: fix the shift, scramble the alphabet, then change the shift every letter — each step exists because the one before it was easy to break.*

</details>

---

## ◈ The Math Behind the Name

| Concept | Where It Shows Up |
|---|---|
| **Addition mod 26** | Caesar |

---

## ◈ The Idea in Code

```python
# The whole repo, in one line of arithmetic (Caesar):
#   encrypt:  E(x) = (x + k) mod 26
#   decrypt:  D(y) = (y - k) mod 26

# ...and the contract every script here keeps:
from substitution.caesar.caesar import encrypt, decrypt

cipher = encrypt("HELLO WORLD", 3)    # KHOOR ZRUOG
plain  = decrypt(cipher, 3)           # HELLO WORLD

assert plain == "HELLO WORLD"         # round-trip, always
```

Every script exposes the same pair — **`encrypt(plaintext, key)`** and **`decrypt(ciphertext, key)`**.

---

## ◈ Ground Rules

| Rule | What It Means |
|---|---|
| **One cipher, one folder, one script** | Each file stands alone and is easy to find |
| **Docstring header** | Every script opens with the cipher, its key format, and how it works |
| **Round-trip verified** | Decrypting an encrypted message must return the original text |

---

## ◈ How to Explore

```bash
# Clone the repo
git clone https://github.com/MuhammadAhmadHamim/infosec-modulo.git

# Every script runs standalone from the repo root
python substitution/caesar/caesar.py

```

> **Requirement:** Python 3 &nbsp;|&nbsp; **Dependencies:** standard library only, unless a script's header says otherwise

---

## ◈ Skills Being Forged

<div align="center">

![](https://img.shields.io/badge/Python-Cryptography_From_Scratch-0b7285?style=flat-square&logo=python&logoColor=white)
![](https://img.shields.io/badge/Math-Modular_Arithmetic-0e1621?style=flat-square&logoColor=white)
![](https://img.shields.io/badge/Practice-Round--Trip_Verification-5b6b7d?style=flat-square&logoColor=white)
![](https://img.shields.io/badge/Practice-Key_Handling-d3dbe5?style=flat-square&logoColor=0e1621)

</div>

---

## ◈ A Note on Security

> [!WARNING]
> These implementations exist **for learning**. Classical ciphers like Caesar are broken and must never be used to protect real data. Even the modern constructions here are written to understand how they work, not to be dropped into production systems. For real applications, use a vetted cryptography library.

---

## ◈ A Note on This Work

Cryptography has a reputation for being untouchable math until you've written a Caesar shift in three lines and watched it fall apart in three more. This repository is the record of taking that reputation apart, one cipher at a time.

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:d3dbe5,50:e3e8ee,100:f1f3f6&height=120&section=footer&animation=fadeIn"/>

*Shifted by k. Reversed by k. Never trusted with a secret.*

</div>