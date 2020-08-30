# vim:fileencoding=utf-8
#  Plugin ytdl para matebot: Devolve vídeo/áudio a partir de link.
#  Copyleft (C) 2020 Desobediente Civil, 2020 Matehackers
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, random, youtube_dl

def cmd_y(args):
  try:
    if len(args['command_list']) > 0:
      response = u"#youtubedl"
      debug = u"[#youtubedl]: [debug] chat_id: %s, from_id: %s, message_id: %s, command_list: %s" % (
        str(args['chat_id']),
        str(args['from_id']),
        str(args['message_id']),
        str(args['command_list']),
      )
      url = ''.join(args['command_list'])
      video_temp = '%030x' % random.randrange(16**30)
      video_file = '/tmp/ytdl_%s.mp4' % video_temp
      options = {
        'outtmpl' : video_file,
        #'format': 'worstvideo+worstaudio/worst',
        'format': 'mp4',
        #'merge_output_format': 'mp4',
        #'postprocessor_args': [
          #'-an',
          #'-c:v libx264',
          #'-crf 26',
          #'-vf scale=640:-1',
        #],
      }
      args['bot'].sendMessage(
        args['chat_id'],
        u"Acho que encontrei o vídeo. Aguarde...",
        reply_to_message_id = args['message_id'],
      )
      youtube_dl.YoutubeDL(options).download([url])
      args['bot'].sendMessage(
        args['chat_id'],
        u"Vídeo extraído. Enviando...",
        reply_to_message_id = args['message_id'],
      )
      args['bot'].sendVideo(
        args['chat_id'],
          open(video_file, 'rb'),
#        duration=None,
#        width=None,
#        height=None,
#        caption=None,
#        parse_mode=None,
#        supports_streaming=None,
#        disable_notification=None,
        reply_to_message_id=args['message_id'],
#        reply_markup=None
      )
      os.remove(video_file)
      return {
        'status': True,
        'type': 'video',
        'response': response,
        'debug': debug,
        'multi': False,
        'parse_mode': None,
        'reply_to_message_id': args['message_id'],
      }
    else:
      response = u"O comando vós já achardes. Agora me envia o comando mais um link, um URL, alguma coisa que está na world wide web e que eu possa salvar. Por exemplo:\n\n/y https://www.youtube.com/watch?v=EqSQ3mnmQ6s"
      debug = u"[#youtubedl]: [nenhum link]"
  except Exception as e:
    response = u"Não consegui extrair o vídeo por problemas técnicos. Os desenvolvedores devem ter sido avisados já, eu acho."
    debug = u"[#yotubedl]: [exception] %s" % (e)
    #raise
  return {
    'status': False,
    'type': 'erro',
    'response': response,
    'debug': debug,
    'multi': False,
    'parse_mode': None,
    'reply_to_message_id': args['message_id'],
  }

## Aliases
def cmd_youtube(args):
  return cmd_y(args)
def cmd_ytdl(args):
  return cmd_y(args)
def cmd_yt(args):
  return cmd_y(args)
def cmd_baixar(args):
  return cmd_y(args)

