"""
Copyright 2014-2016 Jiří Janoušek <janousek.jiri@gmail.com>

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from collections import OrderedDict

BUILD_JSON = {
	"icons": [
		"icons/icon.svg SCALABLE 64 128 256",
		"icons/icon-xs.svg 16 22 24",
		"icons/icon-sm.svg 32 48"
	]
}

GITIGNORE = "Makefile\nmetadata.json\nicons\n"

METADATA_IN_JSON = OrderedDict((
    ("id", "happy_songs"), 
    ("name", "Happy Songs"), 
    ("home_url", "http://www.happy_songs.com"), 
    ("maintainer_name", "FIXME"), 
    ("maintainer_link", "https://github.com/FIXME"), 
    ("version_major", 1), 
    ("version_minor", 0), 
    ("api_major", 3), 
    ("api_minor", 0), 
    ("categories", "AudioVideo;Audio;"), 
    ("license", "2-Clause BSD-license; CC-BY-SA 3.0"),
    ("build", BUILD_JSON)
))

CONFIGURE_SCRIPT = "#!/usr/bin/env python3\nimport nuvolasdk\nnuvolasdk.gen_makefile()\n"
