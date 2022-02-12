# Title

## Authors
- @joooooooooooooooooooooooooooooooooooosh

## Category
- Miscellaneous

## Description
I've created a program which gets the title of any webpage you want! I've restricted it to only get pages from our SecSoc website though - it's foolproof!! There's no accounts being used in the program but if you want the flag you're going to have to ["login" with a username (no password needed)](https://stackoverflow.com/a/21427515)...

## Difficulty
- Medium

## Points
100

## Hints
you're not going to find any titles with the word 'xkcd' on the SecSoc website! maybe you can get it to check another site instead...
https://youtu.be/FCjMoPpOPYI?t=838

## Files
- login.py: the program to pwn

## Solution
<details>
<summary>Spoiler</summary>

### Idea
URLs are more complicated than they seem...

### Walkthrough
1. If you look at the code inside `login.py` it's pretty simple - we take a URL as input from the user, check if it starts with 'unswsecurity.com' to "ensure" that we can only get pages from the SecSoc website, and fetch the title of that webpage - i.e. the text that appears at the top of your tab when you have the site loaded.

    Then if the page title happens to contain the strange word 'xkcd', the program prints a flag! But how can we find a page that has such a weird word in its title?? Surely none of the pages on `unswsecurity.com` contain that word..

2. If you've ever used `ssh`, you've probably seen and used URLs with a username and domain - we also linked an example in the challenge description. For example, when logging into CSE servers, you can run the command `ssh z5555555@login.cse.unsw.edu.au`

    This kind of URL with a username and domain can be used in any context - it's universal! The cool part is there's not many restrictions on what the username can be - for example, try entering the URL 'google.com@unswsecurity.com'. Your browser will probably give you a warning because it noticed that your username looks like a website and maybe someone's trying to trick you, but if you accept the warning it will take you to `unswsecurity.com` instead of `google.com`!

3. So from this we can skip past the url check in `login.py` by supplying a URL of the form 'unswsecurity.com@some_other_site.com' - all we need is to find a site that will have 'xkcd' in it's title! If you search for 'xkcd', the first result will be `xkcd.com`, a popular nerdy webcomic that posts about all kinds of topics. The home page for `xkcd.com` always displays the most recent comic, and the title always has the word 'xkcd' in it! 

    So all you need to do is supply the input `unswsecurity.com@xkcd.com`, and the program will load the home page of `xkcd.com` and subsequently give you the flag!

## The alternative - and much more complicated - solution
As you have probably seen in examples such as `docs.google.com` or `login.cse.unsw.edu.au`, sites can have many domain levels. If you *really* wanted, you could host a website of your own (e.g. for free through Github Pages), and then register a URL which starts with 'unswsecurity.com', for example you could set up 'unswsecurity.com.mycustomurl.me', and have this point to your site which serves a page with a title that contains the word 'xkcd'. Supplying `unswsecurity.com.mycustomurl.me` to `login.py` would also bypass the required checks - but I'd definitely recommend the first approach instead!

### Flag
`OWEEK{un1ver5aL_r3s0urc3_L0g1ns}`
</details>
