# -*- coding: utf-8 -*-
"""
Display static text.

Configuration parameters:
    format: text that should be printed

@author frimdo ztracenastopa@centrum.cz
"""


class Py3status:
    """
    """
    # available configuration parameters
    format = ''

    def static_string(self):
        response = {
            'cached_until': self.py3.CACHE_FOREVER,
            'full_text': self.format,
        }
        return response


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    config = {
        'format': 'Hello World!'
    }
    from py3status.module_test import module_test
    module_test(Py3status, config=config)
