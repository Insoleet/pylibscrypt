#!/usr/bin/env python

# Copyright (c) 2014-2015, Jan Varho
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import ctypes.util
import platform
import sys

if '-p' in sys.argv:
    platform.python_implementation = lambda:'PyPy'

def unimport():
    del sys.modules['pylibscrypt']
    sys.modules.pop('pylibscrypt.common', None)
    sys.modules.pop('pylibscrypt.mcf', None)
    sys.modules.pop('pylibscrypt.libsodium_load', None)

tmp1 = ctypes.util.find_library
tmp2 = ctypes.cdll.LoadLibrary
ctypes.util.find_library = lambda *args, **kw: None
ctypes.cdll.LoadLibrary = lambda *args, **kw: None
import pylibscrypt
ctypes.util.find_library = tmp1
ctypes.cdll.LoadLibrary = tmp2

unimport()
sys.modules['pylibscrypt.pylibscrypt'] = None
import pylibscrypt

unimport()
sys.modules['pylibscrypt.pyscrypt'] = None
import pylibscrypt

unimport()
sys.modules['pylibscrypt.pylibsodium'] = None
import pylibscrypt

unimport()
sys.modules['pylibscrypt.pylibsodium_salsa'] = None
import pylibscrypt

