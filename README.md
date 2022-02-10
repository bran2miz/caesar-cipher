# Caesar Cipher - Lab 18

## Author: Brandon Mizutani

Version: 1.0.0 (PR URL: [PR URL](https://github.com/bran2miz/caesar-cipher))

## Overview

This lab assignment required us to devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

## Getting Started

### Lab 18

This web scraper is able to:

1.Create an encrypt function that takes in a plain text phrase and a numeric shift.
-The phrase will then be shifted that many letters.
-Shifts that exceed 26 should wrap around.
-Shifts that push a letter out or range should wrap around.

2.Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

3.Create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

4.Devise a method for the computer to determine if code was broken with minimal human guidance.

## Architecture

Python, Poetry, Cipher, Encrypt

## Change Log

02-09-22 (8:40pm): 7 tests are passing and now onto the crack function.

02-09-22 (9:30pm): all unit tests are passing.

## Credit and Collaborations

Eddie Ponce

Alex Payne

Connor Boyce

Roger Huba
