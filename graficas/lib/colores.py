#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

import random


# Archivo que contiene listas de colores


paleta1 = ['#ADF6B1', '#A1E5AB', '#90BAAD',
           '#8AA2A9', '#717C89']

paleta2 = ['#E9D758', '#297373', '#FF8552',
           '#E6E6E6', '#39393A']

paleta3 = ['#E9FF70', '#FFD670', '#FF9770',
           '#F25F5C', '#50514F']

paleta3_ext = ['#E9FF70', '#FFD670', '#FF9770',
           '#F25F5C', '#50514F', '#202020']

paleta4 = ['#247BA0', '#70C1B3', '#B2DBBF',
           '#F3FFBD', '#FF1654']

paleta5 = ['#96858F', '#6D7993', '#9099A2', '#D5D5D5']

__paleta6 = ['#ff1417', '#ff6611', '#ff8844',
             '#ffee55', '#fefe38', '#ffff99',
             '#aacc22', '#bbdd77', '#c8cf82',
             '#92a77e', '#5599ee', '#0088cc',
             '#226688', '#175279', '#557777',
             '#ddbb33', '#d3a76d', '#a9834b',
             '#aa6688', '#767676']

__paleta7 = ['#7f0000', '#cc0000', '#ff4444',
             '#ff7f7f', '#ffb2b2', '#995100',
             '#cc6c00', '#ff8800', '#ffbb33',
             '#ffe564', '#2c4c00', '#436500',
             '#669900', '#99cc00', '#d2fe4c',
             '#3c1451', '#6b238e', '#9933cc',
             '#aa66cc', '#bc93d1', '#004c66',
             '#007299', '#0099cc', '#33b5e5',
             '#8ed5f0', '#660033', '#b20058',
             '#e50072', '#ff3298', '#ff7fbf']

__paleta8 = ['#f80c12', '#ee1100', '#ff3311',
             '#ff4422', '#ff6644', '#ff9933',
             '#feae2d', '#ccbb33', '#d0c310',
             '#aacc22', '#69d025', '#22ccaa',
             '#12bdb9', '#11aabb', '#4444dd',
             '#3311bb', '#3b0cbd', '#442299']

__paleta9 = ['#0c0600', '#0c0623', '#eedd22',
             '#ffff66', '#668833', '#449977',
             '#11aa99', '#eaeabe', '#ffcc33',
             '#ff4732']


__paleta10 = ['#198100', '#4dc32c', '#bef43d',
              '#387e73', '#33c199', '#87ff9d',
              '#2469ba', '#75cffa', '#bd5dfd',
              '#891bb0', '#f16391', '#feadc0',
              '#c6281c', '#f95a00', '#ff9e32',
              '#ffe07a']

__todas = paleta1 + paleta2 + paleta3 + paleta4 + paleta5 + __paleta6 + __paleta7 + __paleta8 + __paleta9 + __paleta10


# Metodos que devuelven una cantidad exacta de colores
# de las listas mas grandes

def redToGray20(n=20):
    return __paleta6[:n]


def androidPalette30(n=30):
    return __paleta7[:n]


def rainbow18(n=18):
    return __paleta8[:n]


def sailingWithRolfe10(n=10):
    return __paleta9[:n]


def legend16(n=16):
    return __paleta10[:n]


def todasPaletas(n=118):
    return __todas[:n]


def randomPaletas(n=118):
    todas = []
    for i in range(n):
        todas.append(random.choice(__todas))
    return todas
