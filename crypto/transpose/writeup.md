# transpose

## Authors
- @XenocidePC

## Category
- Crypto

## Description
My singing teacher told me that I'll be able to hit the high note in Aha's "Take on Me" if I just change the key. Problem is, I'm not sure how I can do that. Maybe if I figure that out, I'll also be able to decode this message...

## Difficulty
- Easy

## Points
40

## Files
- [transpose.txt](_ctfd/files/transpose.txt)

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Simple transposition cipher 

### Walkthrough
1. Realise that the first 5 letters are just `OWEEK` rearranged, so the permutation for the transposition cipher is either `25143` or `25134` (correct)
2. Rearrange each block of 5 letters manually or use an [online transposition cipher decoder](https://www.dcode.fr/transposition-cipher) (Write by rows, read by rows)

### Flag
`OWEEK{jAva_pR0gr@mM3rs_CanT_CsHarP}`
</details>
