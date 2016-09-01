from django.http import HttpResponse, HttpResponseBadRequest
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import logging
from pprint import pformat

import ujson
from linebot.client import LineBotClient


client = LineBotClient(**settings.LINE_BOT_SETTINGS)
logger = logging.getLogger('django')


@csrf_exempt
def reply(request):
    # Check signature
    try:
        if not client.validate_signature(request.META['HTTP_X_LINE_CHANNELSIGNATURE'],
                                         request.body.decode('utf-8')):
            logger.warning(('Invalid request to callback function.\n'
                            'Not valid signature'
                            'request: \n {req}').format(req=request))
            return HttpResponseBadRequest()
    except KeyError as ke:
        logger.exception(('Invalid request to callback function.\n'
                          'Does not contain X-Line-Channelsignature\n'
                          'request: {req}\n'
                          'exception: {e}').format(req=request,
                                                   e=ke))
        return HttpResponseBadRequest()

    req_json = ujson.loads(request.body.decode('utf-8'))
    logger.info('Request Received: {req}'.format(req=pformat(req_json, indent=4)))
    req_content = req_json['result'][0]['content']

    # TODO: Reply
    return HttpResponse()
