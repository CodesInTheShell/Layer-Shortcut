# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LayerShorcut
                                 A QGIS plugin
 Shortcut key for layers
                             -------------------
        begin                : 2018-01-23
        copyright            : (C) 2018 by CodesInTheShell
        email                : dhans053008@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LayerShorcut class from file LayerShorcut.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .layer_shorcut import LayerShorcut
    return LayerShorcut(iface)
