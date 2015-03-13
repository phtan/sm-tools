# -*- coding: utf-8 -*-
"""
/***************************************************************************
 check_network
                                 A QGIS plugin
 This plugin checks the consistency of the traffic network imported into QGIS
                             -------------------
        begin                : 2015-03-04
        copyright            : (C) 2015 by Singapore-MIT Alliance for Research and Technology
        email                : chaitanyamalaviya@gmail.com
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
    """Load check_network class from file check_network.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .consistency_check import check_network
    return check_network(iface)
