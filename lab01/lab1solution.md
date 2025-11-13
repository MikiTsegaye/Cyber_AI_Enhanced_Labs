# Lab 01: Mapping Cyber Threat & Attacks

## 🔗 Sources

* [Google Cloud Blog: UNC6040 – Proactive Hardening Recommendations](https://cloud.google.com/blog/topics/threat-analysis/unc6040-proactive-hardening-recommendations)
* [MITRE ATT&CK Campaigns: C0059](https://attack.mitre.org/campaigns/C0059/)

---

## 📝 Description and Schema

[cite_start]**UNC6040** is a **financially motivated threat actor** that uses spearphishing by voice to gain access to sensitive data[cite: 1]. [cite_start]With the stolen data, they perform **extortion** on several victims[cite: 1].

The attack pattern typically involves:
1.  **Calling employees** of large organizations[cite: 1].
2.  [cite_start]**Impersonating IT staff** for initial access[cite: 1].
3.  [cite_start]**Manipulating victims** into downloading an unauthorized application into the organization portal (e.g., a data loader app)[cite: 1].
4.  [cite_start]Using the **exfiltrated data** to perform extortion, forcing victims to take certain actions[cite: 1].

**Attack Path Diagram:**

![Diagram showing the UNC6040 attack path: Social Engineering Phone Call -> Request user credentials & Approve Salesforce Connect code -> Data Loader application added -> Data export from Salesforce environment.](https://github.com/MikiTsegaye/Cyber_AI_Enhanced_Labs/blob/main/lab01/attack-flow-unc6040-hardening.max-1700x1700.png?raw=true)

---



---

## 🛡️ Tactics and Techniques Used (MITRE ATT&CK)

| Tactic | Technique | Description |
| :--- | :--- | :--- |
| **Initial Access** | **Spearphishing Voice (T1566.004)** | [cite_start]Impersonation of IT/helpdesk staff targeting English-speaking branches of multinational corporations to gain trust and instruct actions in real time[cite: 1]. |
| **Initial Access** | **Spearphishing Link (T1566.002)** | [cite_start]Social engineering: Getting users to authorize a malicious or spoofed Salesforce connected app (e.g., Data Loader or devicecode flow), granting OAuth tokens without exploiting a Salesforce vulnerability[cite: 1]. |
| **Data Exfiltration** | **Exfiltration Over Web Service (T1567)** | [cite_start]High-volume API extraction from Salesforce using REST query/queryMore bursts and Bulk API result downloads to drain CRM objects[cite: 1]. |
| **Lateral Movement** | **Valid Accounts (T1078)** | [cite_start]Using the same public egress IP, then attempting logins to Okta/Entra/M365 within minutes to an hour to broaden access and pull mail/files via Graph[cite: 1]. |
| **Lateral Movement** | **Use Alternate Authentication Material (T1550)** | [cite_start]Reuse of harvested credentials or session context to reach other cloud services after the Salesforce drain[cite: 1]. |
| **Evasion** | **Valid Accounts - Cloud Accounts (T1078.004)** | [cite_start]Use of privacy VPN egress (commonly Mullvad) and hosting that mimics internal tooling to obscure origin and reduce detection fidelity[cite: 1]. |
| **Impact** | **Exfiltration Over Web Service (T1567)** | [cite_start]Large-scale theft of customer and business data from Salesforce instances, followed by delayed extortion[cite: 1]. [cite_start]Actors sometimes claim affiliation with ShinyHunters to increase pressure on victims[cite: 1]. |
