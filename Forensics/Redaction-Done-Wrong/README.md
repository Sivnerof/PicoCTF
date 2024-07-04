# Redaction Gone Wrong

## Description

Now you DON’T see me. This [report](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf "Pico CTF link to download financial report in PDF format") has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

## Hints

* How can you be sure of the redaction?

## Walkthrough

If we open the [Financial Report for ABC Labs](./Financial_Report_for_ABC_Labs.pdf "Link to Financial Report for ABC Labs PDF") we'll see what appears like a redacted report.

```
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
_________ - Just painted over in MS word.
Cost Benefit Analysis
__________
Credit Debit
________________________
Expenses from the ________________
_____________________
Redacted document.
```

But if you read the comment that redactions were done by simply painting over the text in MS Paint, you'll know that the text still exists underneath. No matter the paint splashed over it, let's copy and paste the text over into a text editor and see that what is hidden is brought to light.

```
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.
Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.
```

Pasting the text into an editor has revealed the flag hidden beneath.

```picoCTF{C4n_Y0u_S33_m3_fully}```
