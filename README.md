## Password Combination Generator

This repository contains the program for generating keyboard combinations using walks and skipping characters.

* To generate <strong>horzontal and vertical</strong> combinations run the following command:
```
python3 password.py <direction> <no_of_chars> <no_of_chars_skip>
```
For example
```
python3 password.py h 6 3
```
* The below table illustrates the options used for `<direction>`
<table>
    <tr>
        <th>
            Option for direction
        </th>
        <th>
            Meaning/Full form
        </th>
    </tr>
    <tr>
        <td>h</td>
        <td>horizontal parsing</td>
    </tr>
    <tr>
        <td>h_s</td>
        <td>horizontal-shift parsing</td>
    </tr>
    <tr>
        <td>v</td>
        <td>vertical parsing</td>
    </tr>
    <tr>
        <td>v_s</td>
        <td>vertical-shift parsing</td>
    </tr>
</table>

* In order to match the passwords with a dataset, you can download the "RockYou" Dataset link is given here - <a href="https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt">Download Here!</a>

* Mention the path on request by the program.

* To generate password combinations across all directions run the following command:
```
python3 generate_random_combinations.py
```
* The input must be given at `keyboard.txt` file where you have to mention the starting characters without spaces, i.e.
    * If input is "ab" - all combinations starting with "a" and "b" will be generated.
    * If input is "a" - all combinations starting with "a" will be generated.
* The output will be a folder generated storing the password combinations for the given input character ranging from 3 to 7/8 characters.



