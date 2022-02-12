# Pixel Peeping

## Authors
- @XenocidePC

## Category
- Crypto

## Description
CSE let me borrow their Katana supercomputing cluster for a few hours and I decided to ask it for the answer to the ultimate question of life, the universe and everything. I was told the response would be in ASCII characters but to my surprise, it spit out an image with 42 pixels instead. They're all different shades of grey though, which is a little weird.

## Difficulty
- Medium

## Points
80

## Files
- [pixel_peeping.png](_ctfd/files/pixel_peeping.png)

## Solution
<details>
<summary>Spoiler</summary>

### Idea
ASCII letters encoded as decimal numbers, then stored as RGB greyscale values in an image

### Walkthrough
1. Upload the image to a [pixel value extractor](https://www.boxentriq.com/code-breaking/pixel-values-extractor) and use the `Greyscale` mode
1. Convert the output of decimal numbers to ASCII (manually or with an [online decoder](https://onlineasciitools.com/convert-decimal-to-ascii))

### Flag
`OWEEK{a_p1cTur3_iS_w0rth_a_tHous@nd_wOrDs}`
</details>
