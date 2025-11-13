# Lab 01: Mapping Cyber Threat & Attacks

## 🔗 Sources

* [Google Cloud Blog: UNC6040 – Proactive Hardening Recommendations](https://cloud.google.com/blog/topics/threat-analysis/unc6040-proactive-hardening-recommendations)
* [MITRE ATT&CK Campaigns: C0059](https://attack.mitre.org/campaigns/C0059/)

---

## 📝 Description and Schema

**UNC6040** is a **financially motivated threat actor** that uses spearphishing by voice to gain access to sensitive data. With the stolen data, they perform **extortion** on several victims.

The attack pattern typically involves:
1.  **Calling employees** of large organizations.
2.  **Impersonating IT staff** for initial access.
3.  **Manipulating victims** into downloading an unauthorized application into the organization portal (e.g., a data loader app).
4.  Using the **exfiltrated data** to perform extortion, forcing victims to take certain actions.

**Attack Path Diagram:**

![Diagram showing the UNC6040 attack path: Social Engineering Phone Call -> Request user credentials & Approve Salesforce Connect code -> Data Loader application added -> Data export from Salesforce environment.](https://github.com/MikiTsegaye/Cyber_AI_Enhanced_Labs/blob/main/lab01/attack-flow-unc6040-hardening.max-1700x1700.png?raw=true)

---



---

## 🛡️ Tactics and Techniques Used (MITRE ATT&CK)

| Tactic | Technique | Description |
| :--- | :--- | :--- |
| **Initial Access** | **Spearphishing Voice (T1566.004)** | Impersonation of IT/helpdesk staff targeting English-speaking branches of multinational corporations to gain trust and instruct actions in real time. |
| **Initial Access** | **Spearphishing Link (T1566.002)** | Social engineering: Getting users to authorize a malicious or spoofed Salesforce connected app (e.g., Data Loader or devicecode flow), granting OAuth tokens without exploiting a Salesforce vulnerability. |
| **Data Exfiltration** | **Exfiltration Over Web Service (T1567)** | High-volume API extraction from Salesforce using REST query/queryMore bursts and Bulk API result downloads to drain CRM objects. |
| **Lateral Movement** | **Valid Accounts (T1078)** | Using the same public egress IP, then attempting logins to Okta/Entra/M365 within minutes to an hour to broaden access and pull mail/files via Graph. |
| **Lateral Movement** | **Use Alternate Authentication Material (T1550)** | Reuse of harvested credentials or session context to reach other cloud services after the Salesforce drain. |
| **Evasion** | **Valid Accounts - Cloud Accounts (T1078.004)** | Use of privacy VPN egress (commonly Mullvad) and hosting that mimics internal tooling to obscure origin and reduce detection fidelity. |
| **Impact** | **Exfiltration Over Web Service (T1567)** | Large-scale theft of customer and business data from Salesforce instances, followed by delayed extortion. Actors sometimes claim affiliation with ShinyHunters to increase pressure on victims. |
