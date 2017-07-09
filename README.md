# APG - A Passphrase Generator

Create passphrases with high entropy that are easy to remember.

Add here description of passphrase format. Advertise easily-remembered
passphrases vs entropy (128 bit of entropy is achieved with 6 words, while
it would require 22 random case-sensitive alphanumeric characters.)

# Usage

~~~python
import apg
p = apg.PassphraseGenerator('wordlist.txt', words=6)
print('passphrase:', p())
print('entropy:', p.entropy())
~~~


# License

Copyright (C) 2017  Gabriel Pelouze

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

See <http://www.gnu.org/licenses/>.
