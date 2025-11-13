Lab 01: Mapping Cyber Threat & Attacks
Links to sources
Google Cloud Blog: UNC6040 - Proactive Hardening Recommendations
MITRE ATT&CK Campaigns: C0059

Description and Schema
UNC6040 is a financially motivated threat actor that uses spearphishing by voice to gain access to sensitive data. With the stolen data, they perform extortion on several victims.
The attack pattern typically involves calling employees of large organizations, impersonating IT staff for initial access, and then manipulating victims into downloading an unauthorized application into the organization portal (e.g., a data loader app).
With the exfiltrated data, the attackers perform extortion, forcing victims to take certain actions.
Schema: 


Tactics and Techniques Used
Initial Access
* Voice phishing: Impersonation of IT/helpdesk staff targeting English-speaking branches of multinational corporations to gain trust and instruct actions in real time. Spearphishing Voice (T1566.004)

* Social engineering: Getting users to authorize a malicious or spoofed Salesforce connected app (e.g., Data Loader or devicecode flow), granting OAuth tokens without exploiting a Salesforce vulnerability. Spearphishing Link (T1566.002)
Data Exfiltration
* High-volume API extraction from Salesforce using REST query/queryMore bursts and Bulk API result downloads to drain CRM objects. Exfiltration Over Web Service (T1567)
Lateral Movement
* Using the same public egress IP, then attempting logins to Okta/Entra/M365 within minutes to an hour to broaden access and pull mail/files via Graph. Valid Accounts (T1078)
* Reuse of harvested credentials or session context to reach other cloud services after the Salesforce drain. Use Alternate Authentication Material (T1550)
Evasion
* Use of privacy VPN egress (commonly Mullvad) and hosting that mimics internal tooling to obscure origin and reduce detection fidelity. Valid Accounts - Cloud Accounts (T1078.004)
Impact
* Large-scale theft of customer and business data from Salesforce instances, followed by delayed extortion. Actors sometimes claim affiliation with ShinyHunters to increase pressure on victims. Exfiltration Over Web Service (T1567)

