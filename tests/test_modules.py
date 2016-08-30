import importlib
import glob
import os.path

from py3status.module_test import module_test

EXCLUDE = [
    '__init__',

    # cli related
    'arch_updates',  # needs arch distro
    'battery_level',  # needs acpi
    'bluetooth',
    'clementine',   # needs qdbus
    'dropboxd_status',  # needs dropbox-cli
    'fedora_updates',  # needs fedora distro
    'gpmdp',  # needs gpmdp-remote
    'graphite',  # config issues
    'hamster',  # needs hamster
    'icinga2',  # config issues
    'insync',  # needs insync
    'nvidia_temp',  # needs nvidia-smi
    'selinux',  #
    'taskwarrior',  # needs task
    'vnstat',  # config issues
    'wifi',
    'xsel',  # needs xsel
    'yandexdisk_status',  # needs yandex-disk

    # python module related
    'aws_bill',  # needs module boto
    'glpi',  # needs module MySQLdb
    'mpd_status',  # needs module mpd
    'ns_checker',  # needs module dns.resolver
    'rt',  # needs module MySQLdb
    'scratchpad_counter',  # needs module i3
    'window_title',  # needs module i3
    'wwan_status',  # needs module netifaces

    'netdata',  # fixed interface prevents testing


    'battery2',
    'battery3',
    'control',
    'multi',
    'service',
    'wifi2',
    'composite',
    'hello_world',
]

CONFIGS = {
    'weather_yahoo': {
        'woeid': 615702,
    }
}


module_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'py3status', 'modules'
)

def test_module():
    '''
    Try to load a run each module.

    Some modules are blacklisted
    '''
    good = True

    module_names = [os.path.basename(x)[:-3]
                    for x in glob.glob(os.path.join(module_path, '*.py'))
                    if os.path.basename(x)[:-3] not in EXCLUDE]

    module_names.sort()

    for module_name in module_names:
        try:
            module = importlib.import_module('py3status.modules.%s' % module_name)
        except Exception as e:
            print('Module %s could not be imported' % module_name)
            print(e)
            print('\n')
            good = False
            continue
        try:
            py3status = module.Py3status
        except:
            continue
        config = CONFIGS.get(module_name)
        try:
            output = module_test(py3status, config=config, test_mode=True)
            for item in output:
                if not ('full_text' in item or 'composite' in item):
                    print('Module %s output was incorrect' % module_name)
                    print(output)
                    print('\n')
                    good = False
        except Exception as e:
            print('Module %s failed on method call' % module_name)
            print(e)
            print('\n')
            good = False
    assert(good)
