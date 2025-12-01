This is a common feeling! Anomaly detection uses a lot of technical terms. Let's break this entire assignment down into simple, real-world concepts.

We basically setting up a simple, automated security guard system for email. 🛡️

***

## 1. The Goal: Find the Bad Guy (Anomaly)

The whole assignment is about teaching a computer what a **normal** email looks like, so it can spot the one **bad email** (the anomaly or the phishing attack) without having to tell it what an attack is.

**Data:** We created emails that simulate a **Phishing Attack (MITRE T1566)**.
* **Normal:** Business emails during the day, 1 or 2 links max.
* **Anomalous (Attack):** Emails at odd hours, with 10 to 15 links inside.

***

## 2. Part 1 & 2: Get to Know Your Data (EDA)

This is like taking a quick look at your security camera footage to learn the patterns.

* **What we did:** We looked at the stats (average, maximum) and created charts like the **Boxplot** 

[Image of box plot explanation diagram]
.
* **What we learned:** we proved that **"Number of Links"** is the **smoking gun**. Normal emails live in a safe, low-link area, and attack emails live in a completely different, high-link area. This is the **signal** the computer will use.

***

## 3. Part 3: Teach the Computer (Isolation Forest)

This is where we build the security guard. The guard is called **Isolation Forest**.

### A. Preprocessing (Cleaning the Data)
The computer only understands numbers, but our data has text (like `'celcom.il'`).
* **Scaling:** Makes the different number ranges equal (e.g., it makes 15 links and 15 hours look equally important to the computer).
* **Encoding:** Turns the domain names (text) into a series of `1`s and `0`s (numbers) so the Isolation Forest can use them.

### B. Training (Drawing Lines)
* **Isolation Forest** works by repeatedly drawing random lines (or "splits") through our data.
* Normal points are in a dense group, so it takes **many** random lines to isolate them.
* Anomalies are by themselves, so it takes **very few** lines to isolate them.
* **The Result: An Anomaly Score.**
    * **Negative Score (< 0):** Very few lines were needed to isolate it. **It's an anomaly!** (Your Phishing emails).
    * **Positive Score (> 0):** Many lines were needed. **It's normal!** (Your innocent emails).

***

## 4. Part 4: Show the World (PCA and Heatmap)

This is how we prove the security guard is working.

* **The Problem:** our data has too many dimensions (hours, links, 4+ domain categories) to draw.
* **The Solution (PCA):** **P**rincipal **C**omponent **A**nalysis (PCA) is like squashing a 3D ball (your high-dimensional data) down onto a 2D piece of paper (our plot) while keeping the most important separation intact.
* **The Heatmap:** We plotted the 2D squashed data.
    * The **Red Dots (Negative Scores)** are our anomalies—they live in their own little cluster away from the main group.
    * The **Blue Dots (Positive Scores)** are the normal emails, all bundled up in the middle.

**Final Conclusion:** We successfully showed that your simple guard (**Isolation Forest**) can perfectly separate the innocent emails from the suspicious phishing attacks using the difference in the number of links, which confirms the model works exactly as intended!
