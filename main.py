#!/usr/bin/python
# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from xbmcswift2 import Plugin

IRIB_CHANNEL_STREAMS = (
  {'name': 'IRIB Nasim',
  'logo': 'nasim.jpg',
  'stream_url': 'rtmp://live.video.asandl.com/devices//nasim-1000k.stream',
  })

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
    is_playable: True,
  } for channel in IRIB_CHANNEL_STREAMS]
  return plugin.finish(items)

def get_logo(logo):
  addon_id=plugin._addon.getAddonInfo('id')
  return 'special://home/addons/%s/resources/%s' % (addon_id, logo)

def log(text):
  plugin.log.info(text)

if __name__ == 'main':
  plugin.run()
