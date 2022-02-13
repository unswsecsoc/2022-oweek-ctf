# extremely important foto

## Authors
- @abiramen

## Category
- Forensics

## Description
What's the name of the suburb across the water?

**Format**: Replace spaces (if any) with underscores and wrap your answer with `OWEEK{}`. For example, if this were Wetherill Park, then the answer would be `OWEEK{wetherill_park}`.


## Difficulty
- Easy

## Points
50


## Files
- extremely important foto.jpg: a cool foto which happens to have some EXIF data

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Looking at the metadata of a file to find information.

### Walkthrough
1. Note that JPG files support storing a lot of metadata (or information about the photo itself) using a format called EXIF.
2. Check the EXIF data, which contains the location that the photo was taken at.
3. Use a tool like pic2map to visualise the location and find the suburb across the water.

### Flag
`OWEEK{ermington}`
</details>
