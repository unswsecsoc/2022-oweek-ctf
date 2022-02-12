# Title

## Authors
- @joooooooooooooooooooooooooooooooooooosh

## Category
- Binary Exploit

## Description
Legend has it this program contains a flag that is impossible to access, but someday there will come a chosen one who has a name powerful enough to unlock its hidden secrets...

## Difficulty
- Easy

## Points
50

## Files
- vuln: the binary to pwn
- vuln.c: source code for `vuln`

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Whenever you accept user input, if the user gives more input than you expected and you don't check for that/allocate space for it then the user input can overwrite other parts of memory.

### Walkthrough
1. Looking at the source code, we can see that there is a 20 byte buffer to store our input as well as a variable that stores our permissions.
2. Our user input is read by scanf(), but crucially there's no kind of length check or enforcement, so we can give as much data as we want and start writing into other areas of memory. [LiveOverflow has some great videos explaining this in detail](https://www.youtube.com/watch?v=T03idxny9jE).
3. If we give a name that is longer than 20 bytes, we'll overwrite the value of is_admin and it will no longer have a value of 0, which causes the if statement to be entered and gives us the flag!
4. However, if we are truthful about how long our name is, the program will exit before we can enter a name! Fortunately, it doesn't check that we actually give a name with the same length that we entered earlier, so we can just lie about the name length being less than 20 bytes and subsequently enter a name with length >20.

### Flag
`OWEEK{n3v3r_tru5t_us3r_inputtttt}`
</details>
