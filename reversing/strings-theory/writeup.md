# Strings Theory

## Authors

- @Sequeli

## Category

- Reversing

## Description

Hello, doctor, in order to increase security to protect our new string theory research better,
top scientists in our IT department have made this program to store all your work.
It was made _specifically_ for you, and our experts assure us it is extremely secure.

## Difficulty

- Medium

## Points

90

## Files

- admin: binary you should take a look at

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Use `strings` to find the username and password "hidden" inside the binary

### Walkthrough

_Looking at a binary can be intmidating at first, especially if you haven't worked with them before.
But I hope I put in "strings" enough times in the challenge to be a clue_

For a Tl;dr solution/walkthrough, scroll down to point 4, but I would like to go over some ways to analyse any unknown binary. When you get a random binary file, its always a good idea to run basic analysis on it:

**_Some things to try out:_**

1. `file`: to find out what type of file it is  
   running it on the binary, we get:

   ```
   admin: ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=d540456874e608289134bc3c4664b11a05465935, not stripped
   ```

   It might look complicated, but the important part is: `ELF 32-bit LSB shared object`, which means its a 32-bit C program.

2. **Scan for Malware (Optional)**: _I mean, its a CTF challenge, so surely you can trust this stranger on the internet, right?_
   - Upload to virus total
   - scan with your antivirus
   - use tools like `lynis` or `rkhunter` on linux

When you're comfortable with trusting the binary (or you use a virtual machine), its time to run it.

3. **Run the Program:**

   - Since its a 32-bit binary, you might have needed the 32-bit libraries to run it. [Stack overflow help](https://stackoverflow.com/questions/49705309/cant-run-32-bit-binary-on-64-bit-debian)

   The program drops you into a login console, if you enter a random password, you can't get in.

   ```
   Welcome to the super secret admin console. Hope I don't need to remind you to keep the company's research on string theory secret
   To proceed, enter your username: sequeli
   Password: super_hackah
   Invalid password. Your mind just hasn't been the same since the electro-shock, has it??
   ```

   (Yes, that is a built-in linux insult)

4. **More Static Analysis**

   Next, you want to see if there is any data hidden inside the binary itself. The easiest way to do this is to use the `strings` program

   You should see some _totally-not-suspicious_ strings:

   ```
   > strings admin
   ...
   The_Admin
   tHis_-PaSSw0rD_iS_Super-sEcURe_I_swear
   ...
   ```

5. **Getting the flag**

   Using the strings you got in step 4 as your username and password logs you into the console and gives you the flag

   ```
   Welcome to the super secret admin console. Hope I don't need to remind you to keep the company's research on string theory secret
   To proceed, enter your username: The_Admin
   Password: tHis_-PaSSw0rD_iS_Super-sEcURe_I_swear
   Welcome back to your lab, professor: OWEEK{57R1rN95_15_N1C3_8U7_hav3-y0u_7R13d_radAR3}
   ```

6. **More ways you could have done this**

   - Since you know the console is actually a C program, you could check the _data section_ (where C programs store constants and global variables) directly using `radare`

     ```
     > rabin2 -qq -z admin
     The_Admin
     tHis_-PaSSw0rD_iS_Super-sEcURe_I_swear
     ...
     ```

   - Load up the file in a disassembler: Various options like `radare`, `binaryninja`, `cutter`, `ida` that make your life simpler by showing step 4 in a tui/gui and/or disassembling the functions to give you the flag directly

### Flag

`OWEEK{57R1rN95_15_N1C3_8U7_hav3-y0u_7R13d_radAR3}`

</details>
