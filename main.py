#!/usr/bin/python
# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 12.09.2016
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from xbmcswift2 import Plugin

IRIB_CHANNEL_STREAMS = (
  {'name': 'IRIB 1',
  'logo': 'channel1.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tv1-1000k.stream',
  },
  {'name': 'IRIB 2',
  'logo': 'channel2.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tv2-1000k.stream',
  },
  {'name': 'IRIB 3',
  'logo': 'channel3.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tv3-1000k.stream',
  },
  {'name': 'IRIB 4',
  'logo': 'channel4.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tv4-1000k.stream',
  },
  {'name': 'Tehran',
  'logo': 'channel5.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tehran-1000k.stream',
  },
  {'name': 'IRINN',
  'logo': 'irinn.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//irinn-1000k.stream',
  },
  {'name': 'Pooya',
  'logo': 'pooya.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//pooya-1000k.stream',
  },
  {'name': 'Namayesh',
  'logo': 'namayesh.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//namayesh-1000k.stream',
  },
  {'name': 'Varzesh',
  'logo': 'varzesh.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//varzesh-1000k.stream',
  },
  {'name': 'Mostanad',
  'logo': 'mostanad.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//mostanad-500k.stream',
  },
  {'name': 'Salamat',
  'logo': 'salamat.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//salamat-500k.stream',
  },
  {'name': 'Nasim',
  'logo': 'nasim.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//nasim-1000k.stream',
  },
  {'name': 'Kurdistan',
  'logo': 'kurdistan.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//kordestan-300k.stream',
  },
)

plugin = Plugin()

@plugin.route('/')
def show_root_menu():
  items = [{
    'label': channel['name'],
    'thumbnail': get_logo(channel['logo']),
    'path': channel['stream_url'],
    'is_playable': True,
  } for channel in IRIB_CHANNEL_STREAMS]
  return plugin.finish(items)

def get_logo(logo):
  addon_id=plugin._addon.getAddonInfo('id')
  return 'special://home/addons/%s/resources/media/%s' % (addon_id, logo)

def log(text):
  plugin.log.info(text)

if __name__ == '__main__':
  plugin.run()
