# owo

## Authors
- @abiramen

## Category
- Crypto


## Description
hellowo! i just learned about something called ascii. uwu!

## Difficulty
- Easy

## Points
50

## Files
- owo-uwu.txt: a bunch of owos and uwus


## Solution
<details>
<summary>Spoiler</summary>

### Idea
ASCII encoding, with binary sequences

### Walkthrough
We seem to have the strings owo and uwu as base units here - this seems very much like a binary system!

There also seems to be exactly 8 owos or uwus in a group, or exactly a byte! This suggests that the flag could be encoded in ASCII.

We know that all ASCII characters represented as a binary byte start with 0. Since all the groups start with owo, we can guess that owo is 0, and uwu is 1.

We can now perform a replacement, such that all owos become a 0, and uwus become a 1, and remove the slashes. This gives us a format that we can put into a binary to ASCII converter, giving us our flag.

### Flag
`OWEEK{oW0_uWu_iT_app3ArS_y0U_ow03d_mY_b1n4rY_uwU!}`
</details>
