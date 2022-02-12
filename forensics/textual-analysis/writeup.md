# textual analysis

## Authors
- @XenocidePC

## Category
- Forensics

## Description
I'm pretty sure NESA doesn't distribute their exams as text files, but the author of this HSC English prompt must have chosen the format for a reason. Apparently the meaning is obvious to those who are familiar with Extension.

## Difficulty
- Easy

## Points
30

## Files
- [textual_analysis.txt](_ctfd/files/textual_analysis.txt)

## Solution
<details>
<summary>Spoiler</summary>

### Idea
PDF document with .txt extension (and some filler text)

### Walkthrough
1. Open the text file and scroll down to see the `%PDF-1.5` file signature, indicating that it is actually a PDF file
2. Change the extension to .pdf and open it with a PDF viewer of your choice, revealing the flag

### Flag
`OWEEK{d0nT_juDge_a_bOok_by_iTs_Cov3r}`
</details>
