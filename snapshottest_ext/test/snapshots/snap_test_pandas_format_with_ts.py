# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_format 1'] = b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x02\x00\x00\x00\xff\xff\xff\xff\x80\x08\x00\x00\x10\x00\x00\x00\x00\x00\n\x00\x0c\x00\x06\x00\x05\x00\x08\x00\n\x00\x00\x00\x00\x01\x04\x00\x0c\x00\x00\x00\x08\x00\x08\x00\x00\x00\x04\x00\x08\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\xec\xf7\xff\xff\x00\x00\x01\x0e\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x0c\x08\x00\x00(\x00\x00\x00\x04\x00\x00\x00list\x00\x00\x00\x00\x80\xf8\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\xf8\xff\xff\x00\x00\x01\x0c\x14\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x0011\x00\x00$\xf8\xff\xffX\xf8\xff\xff\x00\x00\x01\r\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\xfc\x06\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00item\x00\x00\x00\x00T\xf8\xff\xff\x88\xf8\xff\xff\x00\x00\x01\x0e\x1c\x00\x00\x00$\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\xa8\x06\x00\x00T\x00\x00\x00,\x00\x00\x00\x04\x00\x00\x00vals\x00\x00\x00\x00 \xf9\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\xd4\xf8\xff\xff\x00\x00\x01\x05\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005\x00\x00\x00\xc4\xf8\xff\xff\xf8\xf8\xff\xff\x00\x00\x01\x0c\x14\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x0011\x00\x00\xec\xf8\xff\xff \xf9\xff\xff\x00\x00\x01\r\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x84\x05\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00item\x00\x00\x00\x00\x1c\xf9\xff\xffP\xf9\xff\xff\x00\x00\x01\x0e\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x000\x05\x00\x00(\x00\x00\x00\x04\x00\x00\x00vals\x00\x00\x00\x00\xe4\xf9\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x94\xf9\xff\xff\x00\x00\x01\x0c\x14\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x0010\x00\x00\x88\xf9\xff\xff\xbc\xf9\xff\xff\x00\x00\x01\x0e\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\xa0\x04\x00\x00(\x00\x00\x00\x04\x00\x00\x00item\x00\x00\x00\x00P\xfa\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\xfa\xff\xff\x00\x00\x01\x0c\x14\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x0011\x00\x00\xf4\xf9\xff\xff(\xfa\xff\xff\x00\x00\x01\r\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\xa8\x03\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00item\x00\x00\x00\x00$\xfa\xff\xffX\xfa\xff\xff\x00\x00\x01\x0e(\x00\x00\x000\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00T\x03\x00\x00\x1c\x03\x00\x00\xb8\x00\x00\x00\x90\x00\x00\x00`\x00\x00\x008\x00\x00\x00\x04\x00\x00\x00vals\x00\x00\x00\x00\xfc\xfa\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\xbc\xfa\xff\xff\x00\x00\x01\x05\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005\x00\x00\x00\xac\xfa\xff\xff\xe0\xfa\xff\xff\x00\x00\x01\x02\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x0016\x00\x00P\xfd\xff\xff\x00\x00\x00\x01 \x00\x00\x00\x0c\xfb\xff\xff\x00\x00\x01\x04\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x004\x00\x00\x00\xfc\xfa\xff\xff0\xfb\xff\xff\x00\x00\x01\x0c\x14\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x0011\x00\x00$\xfb\xff\xffX\xfb\xff\xff\x00\x00\x01\r\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x94\x01\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00item\x00\x00\x00\x00T\xfb\xff\xff\x88\xfb\xff\xff\x00\x00\x01\x0e\x1c\x00\x00\x00$\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00@\x01\x00\x00T\x00\x00\x00,\x00\x00\x00\x04\x00\x00\x00vals\x00\x00\x00\x00 \xfc\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\xd4\xfb\xff\xff\x00\x00\x01\x05\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005\x00\x00\x00\xc4\xfb\xff\xff\xf8\xfb\xff\xff\x00\x00\x01\x0c\x14\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x0012\x00\x00\xec\xfb\xff\xff \xfc\xff\xff\x00\x00\x01\x0e\x1c\x00\x00\x00$\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\x84\x00\x00\x00T\x00\x00\x00,\x00\x00\x00\x04\x00\x00\x00item\x00\x00\x00\x00\xb8\xfc\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00l\xfc\xff\xff\x00\x00\x01\x05\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005\x00\x00\x00\\\xfc\xff\xff\x90\xfc\xff\xff\x00\x00\x01\x02\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x0015\x00\x00\x00\xff\xff\xff\x00\x00\x00\x01 \x00\x00\x00\xbc\xfc\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00\xac\xfc\xff\xff\xe0\xfc\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00\xd0\xfc\xff\xff\x04\xfd\xff\xff\x00\x00\x01\x0e\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00P\x00\x00\x00(\x00\x00\x00\x04\x00\x00\x00keys\x00\x00\x00\x00\x98\xfd\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00H\xfd\xff\xff\x00\x00\x01\x05\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005\x00\x00\x008\xfd\xff\xffl\xfd\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00\\\xfd\xff\xff\x90\xfd\xff\xff\x00\x00\x01\x02\x10\x00\x00\x00\x1c\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x0015\x00\x00\x08\x00\x0c\x00\x08\x00\x07\x00\x08\x00\x00\x00\x00\x00\x00\x01 \x00\x00\x00\xc4\xfd\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00\xb4\xfd\xff\xff\xe8\xfd\xff\xff\x00\x00\x01\x0e\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00P\x00\x00\x00(\x00\x00\x00\x04\x00\x00\x00keys\x00\x00\x00\x00|\xfe\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00,\xfe\xff\xff\x00\x00\x01\x05\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005\x00\x00\x00\x1c\xfe\xff\xffP\xfe\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00@\xfe\xff\xfft\xfe\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00d\xfe\xff\xff\x98\xfe\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00\x88\xfe\xff\xff\xbc\xfe\xff\xff\x00\x00\x01\x0e\x18\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00P\x00\x00\x00(\x00\x00\x00\x04\x00\x00\x00keys\x00\x00\x00\x00P\xff\xff\xff\x00\x00\x01\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\xff\xff\xff\x00\x00\x01\x05\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005\x00\x00\x00\xf0\xfe\xff\xff$\xff\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00\x14\xff\xff\xffH\xff\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x008\xff\xff\xffl\xff\xff\xff\x00\x00\x01\x0e\x18\x00\x00\x00(\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00X\x00\x00\x000\x00\x00\x00\x04\x00\x00\x00keys\x00\x00\x00\x00\x08\x00\x0c\x00\x06\x00\x08\x00\x08\x00\x00\x00\x00\x00\x01\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xb8\xff\xff\xff\x00\x00\x01\x05\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x005\x00\x00\x00\xa8\xff\xff\xff\xdc\xff\xff\xff\x00\x00\x01\x01\x10\x00\x00\x00\x14\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00\xcc\xff\xff\xff\x10\x00\x14\x00\x08\x00\x06\x00\x07\x00\x0c\x00\x00\x00\x10\x00\x10\x00\x00\x00\x00\x00\x01\x01\x10\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x000\x00\x00\x00\x04\x00\x04\x00\x04\x00\x00\x00\xff\xff\xff\xff\x88\x07\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x16\x00\x06\x00\x05\x00\x08\x00\x0c\x00\x0c\x00\x00\x00\x00\x03\x04\x00\x18\x00\x00\x00\x90\x03\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x18\x00\x0c\x00\x04\x00\x08\x00\n\x00\x00\x00\x8c\x04\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00H\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00X\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00X\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x90\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x98\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\xb0\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xb8\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\xd0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00,\x00\x00\x00\x00\x00\x00\x00(\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x01\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00X\x01\x00\x00\x00\x00\x00\x00H\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\xb0\x01\x00\x00\x00\x00\x00\x00,\x00\x00\x00\x00\x00\x00\x00\xe0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x01\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\xf0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x01\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\xf8\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x01\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x08\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x02\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x18\x02\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00(\x02\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x000\x02\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x008\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x02\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00@\x02\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00H\x02\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00P\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x02\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00X\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00X\x02\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00`\x02\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00h\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00h\x02\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00p\x02\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00x\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x02\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x80\x02\x00\x00\x00\x00\x00\x00\xcf\x00\x00\x00\x00\x00\x00\x00P\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x03\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00X\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00X\x03\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00h\x03\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00x\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x03\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x80\x03\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00,\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00data_pytype_\x00\x00\x00\x00\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00blocksaxes\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x07\x00\x00\x00\t\x00\x00\x00\x0b\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x0e\x00\x00\x00\x17\x00\x00\x00\x1c\x00\x00\x00%\x00\x00\x00*\x00\x00\x000\x00\x00\x004\x00\x00\x00<\x00\x00\x00@\x00\x00\x00H\x00\x00\x00placementblockplacementblockplacementblockobjectdata_pytype_data_pytype_\x01\x01\x01\x02\x01\x03\x00\x04\x05\x04\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00data_pytype_\x00\x00\x00\x00\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00<M8[ns]\x00\x00\x00\x00\x00\x08\x00\x00\x00np.array\x00\x00\x00\x00\xcf\x00\x00\x00\x80\x04\x95\xc4\x00\x00\x00\x00\x00\x00\x00\x8c\x15numpy.core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94\x8c\x05numpy\x94\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x02K\x07\x86\x94h\x03\x8c\x05dtype\x94\x93\x94\x8c\x02O8\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01|\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK?t\x94b\x89]\x94(\x8c\t300676.SZ\x94h\x13h\x13h\x13h\x13\x8c\t000002.SZ\x94h\x14\x8c\x03BUY\x94\x8c\x04SELL\x94h\x15h\x15h\x16h\x15h\x16et\x94b.\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00pd.Indexpd.Index\x00\x00\x00\x00\x0c\x00\x00\x00pd.DataFrame\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff\xff\xb8\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1a\x00\x06\x00\x05\x00\x08\x00\x0c\x00\x0c\x00\x00\x00\x00\x04\x04\x00 \x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00(\x00\x07\x00\x08\x00\x0c\x00\x10\x00\x14\x00\x0e\x00\x00\x00\x00\x00\x00\x02`\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0c\x00\x00\x00\x08\x00\x14\x00\x08\x00\x04\x00\x08\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x0c\x00\x08\x00\x07\x00\x08\x00\x00\x00\x00\x00\x00\x01@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xf8\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1a\x00\x06\x00\x05\x00\x08\x00\x0c\x00\x0c\x00\x00\x00\x00\x04\x04\x00 \x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00(\x00\x07\x00\x08\x00\x0c\x00\x10\x00\x14\x00\x0e\x00\x00\x00\x00\x00\x00\x02\x90\x00\x00\x004\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x000\x00\x00\x00\x0c\x00\x00\x00\x08\x00\x10\x00\x08\x00\x04\x00\x08\x00\x00\x00\x0c\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x04\x00\x08\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x0c\x00\x08\x00\x07\x00\x08\x00\x00\x00\x00\x00\x00\x01@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdc\x05\x00\x00\x00\x00\x00\x00\xdc\x05\x00\x00\x00\x00\x00\x00\xa0\x0f\x00\x00\x00\x00\x00\x00\xe8\x03\x00\x00\x00\x00\x00\x00\xa0\x0f\x00\x00\x00\x00\x00\x00\xa0\x0f\x00\x00\x00\x00\x00\x00\xa0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xb8\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1a\x00\x06\x00\x05\x00\x08\x00\x0c\x00\x0c\x00\x00\x00\x00\x04\x04\x00 \x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00(\x00\x07\x00\x08\x00\x0c\x00\x10\x00\x14\x00\x0e\x00\x00\x00\x00\x00\x00\x02`\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0c\x00\x00\x00\x08\x00\x14\x00\x08\x00\x04\x00\x08\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x0c\x00\x08\x00\x07\x00\x08\x00\x00\x00\x00\x00\x00\x01@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xf8\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1a\x00\x06\x00\x05\x00\x08\x00\x0c\x00\x0c\x00\x00\x00\x00\x04\x04\x00 \x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00(\x00\x07\x00\x08\x00\x0c\x00\x10\x00\x14\x00\x0e\x00\x00\x00\x00\x00\x00\x02\x8c\x00\x00\x004\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x000\x00\x00\x00\x0c\x00\x00\x00\x08\x00\x10\x00\x08\x00\x04\x00\x08\x00\x00\x00\x0c\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x04\x00\x08\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x08\x00\x04\x00\x06\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Q\xd5n]\xe8\x15\x00\x00>\x89,I\xe9\x15\x00\x00>\x89,I\xe9\x15\x00\x00A\xea\xb7F\xed\x15\x00\x00j\xe3\xc7l\xef\x15\x00\x00\xb9t\\\xbb\xef\x15\x00\x00\x08\x06\xf1\t\xf0\x15\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xb8\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x1a\x00\x06\x00\x05\x00\x08\x00\x0c\x00\x0c\x00\x00\x00\x00\x04\x04\x00 \x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00(\x00\x07\x00\x08\x00\x0c\x00\x10\x00\x14\x00\x0e\x00\x00\x00\x00\x00\x00\x02`\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0c\x00\x00\x00\x08\x00\x14\x00\x08\x00\x04\x00\x08\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x0c\x00\x08\x00\x07\x00\x08\x00\x00\x00\x00\x00\x00\x01@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01\x00\x00\x00\x00\x00\x00\x80\x04\x95\xf7\x00\x00\x00\x00\x00\x00\x00\x8c\x18pandas.core.indexes.base\x94\x8c\n_new_Index\x94\x93\x94h\x00\x8c\x05Index\x94\x93\x94}\x94(\x8c\x04data\x94\x8c\x15numpy.core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94\x8c\x05numpy\x94\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x04\x85\x94h\n\x8c\x05dtype\x94\x93\x94\x8c\x02O8\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01|\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK?t\x94b\x89]\x94(\x8c\x04Date\x94\x8c\x06Symbol\x94\x8c\x05Order\x94\x8c\x06Shares\x94et\x94b\x8c\x04name\x94Nu\x86\x94R\x94.\x8d\x00\x00\x00\x00\x00\x00\x00\x80\x04\x95\x82\x00\x00\x00\x00\x00\x00\x00\x8c\x18pandas.core.indexes.base\x94\x8c\n_new_Index\x94\x93\x94\x8c\x19pandas.core.indexes.range\x94\x8c\nRangeIndex\x94\x93\x94}\x94(\x8c\x04name\x94N\x8c\x05start\x94K\x00\x8c\x04stop\x94K\x07\x8c\x04step\x94K\x01u\x86\x94R\x94.'
