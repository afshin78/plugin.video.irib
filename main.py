#!/usr/bin/python
# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from xbmcswift2 import Plugin

IRIB_CHANNEL_STREAMS = (
  {'name': 'Channel 1',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tv1-1000k.stream',
  },
  {'name': 'Channel 2',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tv2-1000k.stream',
  },
  {'name': 'Channel 3',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tv3-1000k.stream',
  },
  {'name': 'Channel 4',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tv4-1000k.stream',
  },
  {'name': 'Tehran',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//tehran-1000k.stream',
  },
  {'name': 'IRINN',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//irinn-1000k.stream',
  },
  {'name': 'Pooya',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//pooya-1000k.stream',
  },
  {'name': 'Namayesh',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//namayesh-1000k.stream',
  },
  {'name': 'Varzesh',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//varzesh-1000k.stream',
  },
  {'name': 'Mostanad',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//mostanad-500k.stream',
  },
  {'name': 'Salamat',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//salamat-500k.stream',
  },
  {'name': 'Nasim',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//nasim-1000k.stream',
  },
  {'name': 'Kordestan',
  'logo': 'nasim.png',
  'stream_url': 'rtmp://live.video.asandl.com/devices//kordestan-300k.stream',
  },
)

plugin = Plugin()

@plugin.route('/')
def show_root_menu():
  items = [
    {'label': 'IRIB',
    'path': plugin.url_for('show_channels')},
  ]
  return plugin.finish(items)

@plugin.route('/IRIB/')
def show_channels():
  items = [{
    'label': channel['name'],
    'thumbnail': get_logo(channel['logo']),
    'path': channel['stream_url'],
    'is_playable': True,
  } for channel in IRIB_CHANNEL_STREAMS]
  return plugin.finish(items)

def get_logo(logo):
  addon_id=plugin._addon.getAddonInfo('id')
  return 'special://home/addons/%s/resources/%s' % (addon_id, logo)

def log(text):
  plugin.log.info(text)

if __name__ == '__main__':
  plugin.run()
