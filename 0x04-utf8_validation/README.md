# UTF-8 Validation

## Overview

This repository provides a simple implementation of a method to validate whether a given dataset represents a valid UTF-8 encoding. The method checks if a sequence of integers, each representing 1 byte of data, adheres to the rules of UTF-8 encoding.

## UTF-8

UTF-8 is a widely used character encoding that can represent every character in the Unicode character set. Each character can be 1 to 4 bytes long, and UTF-8 uses a specific pattern of leading and trailing bytes to represent characters of different lengths.

This repository contains a Python script that checks whether a given dataset follows the rules of UTF-8 encoding. The validation is done by examining the binary representation of each byte and ensuring it conforms to the UTF-8 pattern.
