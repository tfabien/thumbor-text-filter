#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import ImageDraw
from PIL import ImageFont
from thumbor.filters import BaseFilter, filter_method


class Filter(BaseFilter):
    @filter_method(
        BaseFilter.String,#word
        BaseFilter.PositiveNumber,#posX
        BaseFilter.PositiveNumber,#posY
        BaseFilter.String,#color name see: http://pillow.readthedocs.io/en/4.0.x/reference/ImageColor.html#color-names
        BaseFilter.PositiveNumber, #font-size
        BaseFilter.String, #font-family
		BaseFilter.String, #align
    )
    def text(self, word, x, y, color, font_size, font_family="Tahoma", align=""):
        image = self.engine.image
        usr_font = ImageFont.truetype(font_family, font_size)
        draw = ImageDraw.Draw(image)
        w, h = draw.textsize(word, font=usr_font)
        if align == 'center':
            draw.text((x - (w / 2), y - (h / 2)), word, fill=color, font=usr_font)
        elif align == 'left':
            draw.text((x, y - (h / 2)), word, fill=color, font=usr_font)
        elif align == 'right':
            draw.text((x - w, y - (h / 2)), word, fill=color, font=usr_font)
        else: 
		    draw.text((x, y), word, fill=color, font=usr_font)
        self.engine.image = image
