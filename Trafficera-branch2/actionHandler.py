import os, re, math
from xml.etree import ElementTree
from xml.dom import minidom
from shapefileIO import TAGS, TYPE
from qgis.core import *
from qgis.utils import *
from PyQt4 import QtCore, QtGui

def getSHTypeFromLayername(layer_name):
    parts = layer_name.split("_")
    if len(parts) < 2:
        return 0
    for typeid, tag in TAGS.iteritems():
        if parts[1] == tag:
            return typeid
    return 0

class ActionHandler():
    def __init__(self, sh_dir, canvas):
        ElementTree.register_namespace('geo', "http://www.smart.mit.edu/geo")
        self.sh_dir = sh_dir
        self.data_path = os.path.join(sh_dir, "data.xml")
        self.document = ElementTree.parse(self.data_path)
        self.layers = {}
        self.active_layer = canvas.currentLayer()
        self.active_layer_id = 0

        # add all layers
        for layer in canvas.layers():
            self.layers[getSHTypeFromLayername(layer.name())] = layer

        # current layer
        current_layer_name = self.active_layer.name()
        self.prefix = current_layer_name.split("_")[0]
        self.active_layer_id = getSHTypeFromLayername(current_layer_name)

    def getLayer(self, typeId):
        if typeId not in self.layers:
            QgsMessageLog.logMessage("load file type %s"%typeId, 'SimGDC')
            full_path = os.path.join(self.sh_dir, "%s_%s.shp"%(self.prefix, TAGS[typeId]))
            self.layers[typeId] = QgsVectorLayer(full_path, "%s_isim"%typeId, "ogr")
        return self.layers[typeId]


    def addMultiNode(self, point, nodeData):
        '''ADD FEATURE TO LAYER'''
        msgBox = QtGui.QMessageBox()
        feat = QgsFeature()
        feat.initAttributes(1)
        feat.setAttribute(0, nodeData["id"])
        feat.setGeometry(QgsGeometry.fromPoint(QgsPoint(point.x(),point.y())))
        self.active_layer.dataProvider().addFeatures([feat])
        '''ADD TO data.xml '''
        roadNetwork = self.document.find('road_network')
        nodes = roadNetwork.find('nodes')
        node = ElementTree.SubElement(nodes, 'node')
        #add Id
        ElementTree.SubElement(node, 'id').text = str(nodeData["id"])
        #addType
        ElementTree.SubElement(node, 'node_type').text = str(nodeData["nodeType"])
        #addTrafficLightId

        ElementTree.SubElement(node, 'traffic_light_id').text = str(nodeData["trafficLightID"])
        #addTags
        ElementTree.SubElement(node,'tags').text = str(nodeData["tags"])
        #addTurningGroup
        turningGroupParent = ElementTree.SubElement(node, 'turning_groups')

        #if nodeData["turningGroup"]:
        for tG in nodeData["turningGroup"]:

            turningGroup = ElementTree.SubElement(turningGroupParent, 'turning_group')
            ElementTree.SubElement(turningGroup, 'id').text = str(tG[0])
            ElementTree.SubElement(turningGroup, 'from_link').text = str(tG[1])
            ElementTree.SubElement(turningGroup, 'to_link').text = str(tG[2])
            ElementTree.SubElement(turningGroup, 'phase').text = str(tG[3])
            ElementTree.SubElement(turningGroup, 'rules').text = str(tG[4])
            ElementTree.SubElement(turningGroup, 'visibility').text = str(tG[5])
            ElementTree.SubElement(turningGroup, 'tags').text = str(tG[6])
            if nodeData["turningPath"]:
                turningPathParent = ElementTree.SubElement(turningGroup, 'turning_paths')
                # msgBox.setText("we are here value.")
                # msgBox.exec_()
                # return
                for tP in nodeData["turningPath"]:
                    coordinates = []
                    if tP[0] == tG[0]:
                        turningPath = ElementTree.SubElement(turningPathParent, 'turning_path')
                        ElementTree.SubElement(turningPath, 'group_id').text = str(tP[0])
                        ElementTree.SubElement(turningPath, 'id').text = str(tP[1])
                        ElementTree.SubElement(turningPath, 'from_lane').text = str(tP[2])
                        ElementTree.SubElement(turningPath, 'to_lane').text = str(tP[3])
                        ElementTree.SubElement(turningPath, 'max_speed').text = str(tP[4])
                        ElementTree.SubElement(turningPath, 'tags').text = str(tP[5])
                        polyline = ElementTree.SubElement(turningPath, 'polyline')
                        points = ElementTree.SubElement(polyline, 'points')

                        for lane in roadNetwork.iter('lane'):
                             if lane.find('id').text == str(tP[2]):
                                lane1 = lane
                                for point in lane1.iter('point'):
                                    if int(point.find('seq_id').text) == 1:
                                        pointtp = ElementTree.SubElement(points,'point')
                                        ElementTree.SubElement(pointtp, 'seq_id').text = str(0)
                                        ElementTree.SubElement(pointtp, 'x').text = point.find('x').text
                                        ElementTree.SubElement(pointtp, 'y').text = point.find('y').text
                                        ElementTree.SubElement(pointtp, 'z').text = str(0)
                                        coordinates.extend([QgsPoint(float(point.find('x').text),float(point.find('y').text))])
                             if lane.find('id').text == str(tP[3]):
                                lane2 = lane
                                for point in lane2.iter('point'):
                                    if int(point.find('seq_id').text)==0:
                                        pointtp = ElementTree.SubElement(points,'point')
                                        ElementTree.SubElement(pointtp, 'seq_id').text = str(1)
                                        ElementTree.SubElement(pointtp, 'x').text = point.find('x').text
                                        ElementTree.SubElement(pointtp, 'y').text = point.find('y').text
                                        ElementTree.SubElement(pointtp, 'z').text = str(0)
                                        coordinates.extend([QgsPoint(float(point.find('x').text),float(point.find('y').text))])
                        feat2 = QgsFeature()
                        feat2.initAttributes(2)
                        feat2.setAttribute(0, tP[1])
                        feat2.setAttribute(1, tP[0])
                        feat2.setGeometry(QgsGeometry.fromPolyline(coordinates))
                        self.layers[TYPE.TURNINGPATH].dataProvider().addFeatures([feat2])


        #add location
        point = ElementTree.SubElement(node, 'point')
        ElementTree.SubElement(point, 'x').text = str(feat.geometry().asPoint().x())
        ElementTree.SubElement(point, 'y').text = str(feat.geometry().asPoint().y())
        ElementTree.SubElement(point, 'z').text = str(0)
        #add originalDB_ID
        # ElementTree.SubElement(multiNode, 'originalDB_ID').text = "\"aimsun-id\":\"%s\""%str(nodeData["aimsunId"])


    def updateMultiNode(self, feature, nodeData):
        #update feature if necessary
        attrs = feature.attributes()
        id = int(attrs[0])
        if id != nodeData["id"]:
            attrs = {0 : nodeData["id"]}
            self.active_layer.dataProvider().changeAttributeValues({int(feature.id()) : attrs })
        #get info
        roadNetwork = self.document.find('road_network')
        nodeparent = roadNetwork.find('nodes')
        nodes = nodeparent.findall('node')
        selectedNode = None
        if nodes is not None:
            for node in nodes:
                nodeId = int(node.find("id").text)
                if nodeId == id:
                    selectedNode = node
                    break
        if selectedNode is None:
            QgsMessageLog.logMessage("updateMultiNode cannot find node id %s"%id, 'SimGDC')
            return
        #update id
        selectedNode.find("id").text = str(nodeData["id"])
        #update type
        selectedNode.find("node_type").text = str(nodeData["nodeType"])

        #addTrafficLightID
        if nodeData["trafficLightID"]:
            selectedNode.find("traffic_light_id").text = str(nodeData["trafficLightID"])

        #add Tags
        if nodeData["tags"]:
            selectedNode.find("tags").text = str(nodeData["tags"])

        #addTurningGroup
        turningGroupParent = selectedNode.find("turning_groups")
        turningGroups = turningGroupParent.findall("turning_group")
        turningPaths = turningGroupParent.findall("turning_path")
        # for tG in turningGroupParent.findall('turning_group'):
        #     turningGroupParent.remove(tG)

        # for tG in nodeData["turningGroup"]:
        #     turningGroup = ElementTree.SubElement(turningGroup.text = str(tG[1])
        #     ElementTree.SubElement(turningGroup, 'toLink').text = str(tG[2])
        #     ElementTree.SubElement(turningGroup, 'Phases').text = str(tG[3])
        #     ElementTree.SubElement(turningGroup, 'Rules').text = str(tG[4])
        #     if nodeData["turningPath"]:
        #         turningPathParent = ElementTree.SubElement(turningGroup, 'TurningPaths')
        #         for tP in nodeData["turningPath"]:
        #             if tP[0] == tG[0]:
        #                 turningPath = ElementTree.SubElement(turningPathParent, 'TurningPath')
        #                 ElementTree.SubElement(turningPath, 'groupID').text = str(tP[0])
        #                 ElementTree.SubElement(turningPath, 'ID').text = str(tP[1])
        #                 ElementTree.SubElement(turningPath, 'fromLane').text = str(tP[2])
        #                 ElementTree.SubElement(turningPath, 'toLane').text = str(tP[3])

        #
        # i=0
        # for tG in turningGroups:
        #     j=0
        #     tG.find("id").text = str(nodeData["turningGroup"][i][0])
        #     tG.find("from_link").text = str(nodeData["turningGroup"][i][1])
        #     tG.find("to_link").text = str(nodeData["turningGroup"][i][2])
        #     tG.find("phase").text = str(nodeData["turningGroup"][i][3])
        #     tG.find('rules').text = str(nodeData["turningGroup"][i][4])
        #     tG.find('visibility').text = str(nodeData["turningGroup"][i][5])
        #     tG.find('tags').text = str(nodeData["turningGroup"][i][6])
        #
        #     for tP in turningPaths:
        #         if str(nodeData["turningGroup"][i][0]) == str(nodeData["turningPath"][j][0]):
        #             tP.find("group_id").text = str(nodeData["turningPath"][j][0])
        #             tP.find("id").text = str(nodeData["turningPath"][j][1])
        #             tP.find("from_lane").text = str(nodeData["turningPath"][j][2])
        #             tP.find("to_lane").text = str(nodeData["turningPath"][j][3])
        #             tP.find("max_speed").text = str(nodeData["turningPath"][j][4])
        #             tP.find("tags").text = str(nodeData["turningPath"][j][5])
        #         j+=1
        #     i+=1

        existingIDs = []
        for tG in turningGroups:
            existingIDs.append(tG.find("id").text)


        for tG in nodeData["turningGroup"]:

            if str(tG[0]) not in existingIDs:

                turningGroup = ElementTree.SubElement(turningGroupParent, 'turning_group')
                ElementTree.SubElement(turningGroup, 'id').text = str(tG[0])
                ElementTree.SubElement(turningGroup, 'from_link').text = str(tG[1])
                ElementTree.SubElement(turningGroup, 'to_link').text = str(tG[2])
                ElementTree.SubElement(turningGroup, 'phase').text = str(tG[3])
                ElementTree.SubElement(turningGroup, 'rules').text = str(tG[4])
                ElementTree.SubElement(turningGroup, 'visibility').text = str(tG[5])
                ElementTree.SubElement(turningGroup, 'tags').text = str(tG[6])
                if nodeData["turningPath"]:
                    turningPathParent = ElementTree.SubElement(turningGroup, 'turning_paths')
                    # msgBox.setText("we are here value.")
                    # msgBox.exec_()
                    # return
                    for tP in nodeData["turningPath"]:
                        coordinates = []
                        if tP[0] == tG[0]:
                            turningPath = ElementTree.SubElement(turningPathParent, 'turning_path')
                            ElementTree.SubElement(turningPath, 'group_id').text = str(tP[0])
                            ElementTree.SubElement(turningPath, 'id').text = str(tP[1])
                            ElementTree.SubElement(turningPath, 'from_lane').text = str(tP[2])
                            ElementTree.SubElement(turningPath, 'to_lane').text = str(tP[3])
                            ElementTree.SubElement(turningPath, 'max_speed').text = str(tP[4])
                            ElementTree.SubElement(turningPath, 'tags').text = str(tP[5])
                            polyline = ElementTree.SubElement(turningPath, 'polyline')
                            points = ElementTree.SubElement(polyline, 'points')

                            for lane in roadNetwork.iter('lane'):
                                 if lane.find('id').text == str(tP[2]):
                                    lane1 = lane
                                    for point in lane1.iter('point'):
                                        if int(point.find('seq_id').text) == 1:
                                            pointtp = ElementTree.SubElement(points,'point')
                                            ElementTree.SubElement(pointtp, 'seq_id').text = str(0)
                                            ElementTree.SubElement(pointtp, 'x').text = point.find('x').text
                                            ElementTree.SubElement(pointtp, 'y').text = point.find('y').text
                                            ElementTree.SubElement(pointtp, 'z').text = str(0)
                                            coordinates.extend([QgsPoint(float(point.find('x').text),float(point.find('y').text))])
                                 if lane.find('id').text == str(tP[3]):
                                    lane2 = lane
                                    for point in lane2.iter('point'):
                                        if int(point.find('seq_id').text)==0:
                                            pointtp = ElementTree.SubElement(points,'point')
                                            ElementTree.SubElement(pointtp, 'seq_id').text = str(1)
                                            ElementTree.SubElement(pointtp, 'x').text = point.find('x').text
                                            ElementTree.SubElement(pointtp, 'y').text = point.find('y').text
                                            ElementTree.SubElement(pointtp, 'z').text = str(0)
                                            coordinates.extend([QgsPoint(float(point.find('x').text),float(point.find('y').text))])
                            feat2 = QgsFeature()
                            feat2.initAttributes(2)
                            feat2.setAttribute(0, tP[1])
                            feat2.setAttribute(1, tP[0])
                            feat2.setGeometry(QgsGeometry.fromPolyline(coordinates))
                            self.layers[TYPE.TURNINGPATH].dataProvider().addFeatures([feat2])

        #update aimsunId
        # selectedNode.find("originalDB_ID").text = "\"aimsun-id\":\"%s\""%str(nodeData["aimsunId"])


    def getMultiNode(self, feature):
        #get id from feature
        attrs = feature.attributes()
        id = int(attrs[0])   
        #get info
        roadNetwork = self.document.find('road_network')
        nodeparent = roadNetwork.find('nodes')
        nodes = nodeparent.findall('node')
        selectedNode = None
        if nodes is not None:
            for node in nodes:
                nodeId = int(node.find("id").text)
                if nodeId == id:
                    selectedNode = node
                    break
        if selectedNode is not None:
            info = {}
            info["id"] = selectedNode.find("id").text
            # aimsunIdStr = selectedNode.find("originalDB_ID").text
            # aimsunIds = re.findall(r'[0-9]+', aimsunIdStr)
            # info["aimsunId"] = aimsunIds[0]
            info["nodeType"] = selectedNode.find("node_type").text
            info["trafficLightID"] = selectedNode.find("traffic_light_id").text
            info["tags"] = selectedNode.find("tags").text

            turningGroups = selectedNode.find("turning_groups")

            turningGroup = turningGroups.findall("turning_group")

            info["turningGroup"] = []
            info["turningPath"] = []

            if turningGroup:
                # msgBox = QtGui.QMessageBox()
                # msgBox.setText(turningGroup[1].find("id").text)
                # msgBox.exec_()
                # return
                for tG in turningGroup:

                    if tG.find("tags"):
                        tags = tG.find("tags").text
                    else:
                        tags = ""
                    info["turningGroup"].append([tG.find("id").text,tG.find("from_link").text,tG.find("to_link").text,tG.find("phase").text,tG.find("rules").text,tG.find("visibility").text, tags])
                    # turningPaths = turningGroups.findall("TurningPath")
                    # if turningPaths:
                    for tP in selectedNode.iter('turning_path'):
                        if tP.find("group_id").text == tG.find("id").text:
                            if tP.find("tags"):
                                tags1 = tP.find("tags").text
                            else:
                                tags1 = ""
                            info["turningPath"].append([tP.find("group_id").text,tP.find("id").text,tP.find("from_lane").text,tP.find("to_lane").text,tP.find("max_speed").text, tags1])

            return info

        return None


    def getLinkList(self):
        listLinks = {}
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        links = linkParent.findall('link')
        selectedSegment= None
        if links is not None:
            for link in links:
                linkId = int(link.find("id").text)
                linkName = link.find("road_name").text
                listLinks[linkId] = linkName
        return listLinks

    def getLinkListDetail(self):
        listLinks = {}
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        links = linkParent.findall('link')
        selectedSegment= None
        if links is not None:
            for link in links:
                linkId = int(link.find("id").text)
                linkName = link.find("road_name").text
                startNode = int(link.find("from_node").text)
                endNode = int(link.find("to_node").text)
                tags = link.find("tags").text
                listLinks[linkId] = [linkId, linkName, startNode, endNode, tags]
        return listLinks

    def manageLink(self, data):

        feat = QgsFeature()
        feat.initAttributes(2)
        feat.setAttribute(0, data["id"])
        feat.setAttribute(1, data["roadName"])
        layerfi = iface.activeLayer().dataProvider().dataSourceUri()
        (myDirectory, nameFile) = os.path.split(layerfi)
        tree = ElementTree.parse(myDirectory + '/data.xml')
        root = tree.getroot()

        if data["oldId"] < 1:
            #add new
            roadNetwork = self.document.find('road_network')
            linkParent = roadNetwork.find('links')
            if linkParent is None:
                linkParent = ElementTree.SubElement(roadNetwork, 'links')
            link = ElementTree.SubElement(linkParent, 'link')
            ElementTree.SubElement(link, 'id').text = str(data["id"])
            ElementTree.SubElement(link, 'road_name').text = str(data["roadName"])
            ElementTree.SubElement(link, 'from_node').text = str(data["startingNode"])
            ElementTree.SubElement(link, 'to_node').text = str(data["endingNode"])
            ElementTree.SubElement(link, 'category').text = str(data["category"])
            ElementTree.SubElement(link, 'road_type').text = str(data["road_type"])
            ElementTree.SubElement(link, 'tags').text = str(data["tags"])
            for node in root.iter('node'):
                if int(node.find('id').text) == (data["startingNode"]):
                    point1 = node.find('point')
                if int(node.find('id').text) == (data["endingNode"]):
                    point2 = node.find('point')
            polylines = ElementTree.SubElement(link,'polylines')
            polyline = ElementTree.SubElement(polylines,'polyline')
            points = ElementTree.SubElement(polyline,'points')

            point = ElementTree.SubElement(points,'point')
            ElementTree.SubElement(point,'x').text = point1.find('x').text
            ElementTree.SubElement(point,'y').text = point1.find('y').text

            point = ElementTree.SubElement(points,'point')
            ElementTree.SubElement(point,'x').text = point2.find('x').text
            ElementTree.SubElement(point,'y').text = point2.find('y').text

            feat.setGeometry(QgsGeometry.fromPolyline([QgsPoint(float(point1.find('x').text),float(point1.find('y').text)),QgsPoint(float(point2.find('x').text),float(point2.find('y').text))]))
            self.active_layer.dataProvider().addFeatures([feat])

            ElementTree.SubElement(link, 'segments')
        else:
            roadNetwork = self.document.find('road_network')
            linkParent = roadNetwork.find('links')
            links = linkParent.findall('link')
            selectedLink = None
            if links is not None:
                for link in links:
                    linkId = int(link.find("id").text)
                    if linkId == data["oldId"]:
                        selectedLink = link
                        break
            #update info
            selectedLink.find("id").text = str(data["id"])
            selectedLink.find("road_name").text = str(data["roadName"])
            selectedLink.find("from_node").text = str(data["startingNode"])
            selectedLink.find("to_node").text = str(data["endingNode"])
            selectedLink.find("category").text = str(data["category"])
            selectedLink.find("road_type").text = str(data["road_type"])
            selectedLink.find("tags").text = str(data["tags"])

            #update segment layer when the id is changed
            if data["id"] != data["oldId"]:
                segmentLayer = self.getLayer(TYPE.SEGMENT)
                for feature in segmentLayer.getFeatures():
                    attrs = feature.attributes()
                    if attrs[0] == data["oldId"]:
                        attrs = {0 : data["id"], 1: attrs[1]}
                        self.active_layer.dataProvider().changeAttributeValues({int(feature.id()) : attrs })


    def addSegment(self, point, data):
        '''ADD FEATURE TO LAYER'''
        feat = QgsFeature()
        feat.initAttributes(2)
        distance = 10
        #coordinates = [QgsPoint(point.x(),point.y()), QgsPoint(point.x(), point.y() + distance), QgsPoint(point.x() + 2*distance, point.y() + distance), QgsPoint(point.x() + 2*distance, point.y())]
        coordinates = [QgsPoint(point.x(),point.y()), QgsPoint(point.x() + distance, point.y() + distance)]
        feat.setAttribute(0, data["linkId"])
        feat.setAttribute(1, data["id"])
        feat.setGeometry(QgsGeometry.fromPolyline(coordinates))
        self.active_layer.dataProvider().addFeatures([feat])
        '''ADD TO data.xml '''
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        links = linkParent.findall('link')
        selectedLink = None
        if links is not None:
            for link in links:
                linkId = int(link.find("id").text)
                if linkId == data["linkId"]:
                    selectedLink = link
                    break
        if selectedLink is not None:
            segments = selectedLink.find("segments")
            if segments is None:
                segments = ElementTree.SubElement(selectedLink, 'segments')
            segment = ElementTree.SubElement(segments, 'segment')
            #add Info
            ElementTree.SubElement(segment, 'id').text = str(data["id"])
            ElementTree.SubElement(segment, 'sequence_no').text = str(data["sequence_no"])
            ElementTree.SubElement(segment, 'capacity').text = str(data["capacity"])
            ElementTree.SubElement(segment, 'max_speed').text = str(data["max_speed"])
            ElementTree.SubElement(segment, 'tags').text = str(data["tags"])
            connectors = ElementTree.SubElement(selectedLink, 'connectors')
            for conn in data["connectors"]:
                connector = ElementTree.SubElement(connectors, 'connector')
                ElementTree.SubElement(connector, 'id').text = str(conn[0])
                ElementTree.SubElement(connector, 'from_segment').text = str(conn[1])
                ElementTree.SubElement(connector, 'to_segment').text = str(conn[2])
                ElementTree.SubElement(connector, 'from_lane').text = str(conn[3])
                ElementTree.SubElement(connector, 'to_lane').text = str(conn[4])

        polyline = ElementTree.SubElement(segment, 'polyline')
        points = ElementTree.SubElement(polyline, 'points')

        for i in range(2):
            clkpoint = ElementTree.SubElement(points, 'point')
            ElementTree.SubElement(clkpoint, 'seq_id').text = str(i)
            ElementTree.SubElement(clkpoint, 'x').text = str(point.x() + distance*i)
            ElementTree.SubElement(clkpoint, 'y').text = str(point.y() + distance*i)
            ElementTree.SubElement(clkpoint, 'z').text = str(0)

    def updateSegment(self, feature, data):
        #update feature if necessary
        attrs = feature.attributes()
        oldLinkId = int(attrs[0])
        oldSegmentId = int(attrs[1])
        if oldLinkId != data["linkId"] or oldSegmentId != data["id"]:
            attrs = {0 : data["linkId"], 1: data["id"]}
            self.active_layer.dataProvider().changeAttributeValues({int(feature.id()) : attrs })
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        links = linkParent.findall('link')
        selectedLink = None
        if links is not None:
            for link in links:
                linkId = int(link.find("id").text)
                if linkId == data["linkId"]:
                    selectedLink = link
                    break
        selectedSegment= None
        oldLinkSegments = None
        newLinkSegments = None
        if links is not None:
            for link in links:
                linkId = int(link.find("id").text)
                if linkId == data["linkId"]:
                    newLinkSegments = link.find("segments")
                if linkId == oldLinkId:
                    oldLinkSegments = link.find("segments")
                    segments = oldLinkSegments.findall("segment")
                    for segment in segments:
                        segmentId = int(segment.find("id").text)
                        if segmentId == oldSegmentId:
                            selectedSegment = segment
        if selectedSegment is None:
            QgsMessageLog.logMessage("updateSegment can not find segment id %s"%str(oldSegmentId), 'SimGDC')
            return
        #update info
        selectedSegment.find("id").text = str(data["id"])
        selectedSegment.find("sequence_no").text = str(data["sequence_no"])
        selectedSegment.find("capacity").text = str(data["capacity"])
        selectedSegment.find("max_speed").text = str(data["max_speed"])
        selectedSegment.find("tags").text = str(data["tags"])

        connectorsroot = selectedLink.find("connectors")
        for connector in connectorsroot.findall("connector"):
            connectorsroot.remove(connector)

        for conn in data["connectors"]:
            connector = ElementTree.SubElement(connectorsroot, 'connector')
            ElementTree.SubElement(connector, 'id').text = str(conn[0])
            ElementTree.SubElement(connector, 'from_segment').text = str(conn[1])
            ElementTree.SubElement(connector, 'to_segment').text = str(conn[2])
            ElementTree.SubElement(connector, 'from_lane').text = str(conn[3])
            ElementTree.SubElement(connector, 'to_lane').text = str(conn[4])
            # conn.find("id").text = str(conn[0])
            # conn.find("from_segment").text = str(conn[1])
            # conn.find("to_segment").text = str(conn[2])
            # conn.find("from_lane").text = str(conn[3])
            # conn.find("to_lane").text = str(conn[4])

        #move to new link if necessary
        if oldLinkId != data["linkId"]:
            oldLinkSegments.remove(selectedSegment)
            newLinkSegments.append(selectedSegment)

    def getSegment(self, feature):
        #get id from feature
        attrs = feature.attributes()
        selectedLinkId = int(attrs[0])
        selectedSegmentId = int(attrs[1])
        #get info
        listLinks = {}
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        links = linkParent.findall('link')
        selectedLink = None

        selectedSegment= None
        if links is not None:
            for link in links:
                linkId = int(link.find("id").text)
                linkName = link.find("road_name").text
                listLinks[linkId] = linkName
                if linkId == selectedLinkId:
                    selectedLink = link
                    segments = link.find("segments").findall("segment")
                    for segment in segments:
                        segmentId = int(segment.find("id").text)
                        if segmentId == selectedSegmentId:
                            selectedSegment = segment
        if selectedSegment is not None:
            info = {}
            info["linkId"] = selectedLinkId
            info["id"] = selectedSegment.find("id").text
            # aimsunIdStr = selectedSegment.find("originalDB_ID").text
            # aimsunIds = re.findall(r'[0-9]+', aimsunIdStr)
            # info["aimsunId"] = aimsunIds[0]
            info["sequence_no"] = selectedSegment.find("sequence_no").text
            info["capacity"] = selectedSegment.find("capacity").text
            info["max_speed"] = selectedSegment.find("max_speed").text
            if selectedSegment.find("tags"):
                info["tags"] = selectedSegment.find("tags").text
            else:
                info["tags"] = None
            # info["roadType"] = selectedSegment.find("roadType").text
            # info["category"] = selectedSegment.find("category").text
            info["connectors"] = []
            for link in roadNetwork.iter('link'):
                if str(selectedLinkId)==link.find('id').text:
                    for conn in link.iter('connector'):
                        if conn.find("from_segment").text == str(selectedSegmentId):
                            info["connectors"].append([conn.find("id").text,conn.find("from_segment").text,conn.find("to_segment").text,conn.find("from_lane").text,conn.find("to_lane").text])

            return [listLinks, info]
        return None

    def addCrossing(self, point, data):
        '''ADD FEATURE TO LAYER'''
        feat = QgsFeature()
        feat.initAttributes(2)
        distance = 1000
        coordinates = [QgsPoint(point.x(),point.y()), QgsPoint(point.x() + distance,point.y()), QgsPoint(point.x() + distance,point.y() + distance), QgsPoint(point.x(),point.y() + distance)]
        feat.setAttribute(0, data["segmentId"])
        feat.setAttribute(1, data["id"])
        feat.setGeometry(QgsGeometry.fromPolygon([coordinates]))
        self.active_layer.dataProvider().addFeatures([feat])
        '''ADD TO data.xml '''
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        selectedSegmentId = int(data["segmentId"])
        selectedSegment = None
        if segments is not None:
            for segment in segments:
                segmentId = int(segment.find("id").text)
                if segmentId == selectedSegmentId:
                    selectedSegment = segment
                    break
        if selectedSegment is not None:
            obstacles = selectedSegment.find("Obstacles")
            if obstacles is None:
                obstacles = ElementTree.SubElement(selectedSegment, 'Obstacles')

            crossing = ElementTree.SubElement(obstacles, 'Crossing')
            #add Info
            ElementTree.SubElement(crossing, 'id').text = str(data["id"])
            ElementTree.SubElement(crossing, 'Offset').text = str(data["offset"])

    def updateCrossing(self, feature, data):
        #update feature if necessary
        attrs = feature.attributes()
        selectedsegmentId = int(attrs[0])
        oldCrossingId = int(attrs[1])
        if oldCrossingId != data["id"]:
            attrs = {0 : selectedsegmentId, 1: data["id"]}
            self.active_layer.dataProvider().changeAttributeValues({int(feature.id()) : attrs })
        #get info
        roadNetwork = self.document.find('geospatial/road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        selectedCrossing = None
        if segments is not None:
            for segment in segments:
                segmentId = int(segment.find("id").text)
                if segmentId == selectedsegmentId:
                    obstacles = segment.find("Obstacles")
                    if obstacles is not None: 
                        crossings = obstacles.findall('Crossing')
                        for crossing in crossings:
                            crossingId = int(crossing.find("id").text)
                            if crossingId == oldCrossingId:
                                selectedCrossing = crossing
                    break
        if selectedCrossing is None:
            QgsMessageLog.logMessage("updateCrossing can not find crossing id %s"%str(oldCrossingId), 'SimGDC')
            return
        selectedCrossing.find("id").text = str(data["id"])
        selectedCrossing.find("Offset").text = str(data["offset"])

    def getCrossing(self, feature):
        #get id from feature
        attrs = feature.attributes()
        selectedSegmentId = int(attrs[0])
        selectedCrossingId = int(attrs[1])
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        selectedCrossing = None
        if segments is not None:
            for segment in segments:
                segmentId = int(segment.find("id").text)
                if segmentId == selectedSegmentId:
                    obstacles = segment.find("Obstacles")
                    if obstacles is not None: 
                        crossings = obstacles.findall('Crossing')
                        for crossing in crossings:
                            crossingId = int(crossing.find("id").text)
                            if crossingId == selectedCrossingId:
                                selectedCrossing = crossing
                    break
        if selectedCrossing is not None:
            info = {}
            info["segmentId"] = selectedSegmentId
            info["id"] = selectedCrossing.find("id").text
            info["offset"] = selectedCrossing.find("Offset").text
            return info
        return None


    def addBusstop(self, point, data):
        '''ADD FEATURE TO LAYER'''
        feat = QgsFeature()
        feat.initAttributes(2)
        feat.setAttribute(0, data["segment_id"])
        feat.setAttribute(1, data["id"])
        feat.setGeometry(QgsGeometry.fromPoint(QgsPoint(point.x(),point.y())))
        self.active_layer.dataProvider().addFeatures([feat])
        '''ADD TO data.xml '''       
         #get info
        roadNetwork = self.document.find('road_network')
        # linkParent = roadNetwork.find('links')
        # segments = linkParent.findall('link/segments/segment')
        # selectedSegmentId = int(data["segmentId"])
        # selectedSegment = None
        # if segments is not None:
        #     for segment in segments:
        #         segmentId = int(segment.find("id").text)
        #         if segmentId == selectedSegmentId:
        #             selectedSegment = segment
        #             break
        # if selectedSegment is not None:
        #     obstacles = selectedSegment.find("Obstacles")
        #     if obstacles is None:
        #         obstacles = ElementTree.SubElement(selectedSegment, 'Obstacles')
        pt_stops = roadNetwork.find('pt_stops')
        if not pt_stops:
            pt_stops = ElementTree.SubElement(roadNetwork,'pt_stops')

        busstop = ElementTree.SubElement(pt_stops, 'bus_stop')
        #add Info
        ElementTree.SubElement(busstop, 'id').text = str(data["id"])
        ElementTree.SubElement(busstop, 'segment_id').text = str(data["segment_id"])
        ElementTree.SubElement(busstop, 'code').text = str(data["busstopCode"])
        ElementTree.SubElement(busstop, 'name').text = str(data["name"])
        ElementTree.SubElement(busstop, 'offset').text = str(data["offset"])
        ElementTree.SubElement(busstop, 'is_terminal').text = str(data["isTerminal"])
        ElementTree.SubElement(busstop, 'is_bay').text = str(data["isBay"])
        ElementTree.SubElement(busstop, 'has_shelter').text = str(data["hasShelter"])
        ElementTree.SubElement(busstop, 'length').text = str(data["length"])
        ElementTree.SubElement(busstop, 'tags').text = str(data["tags"])
        point = ElementTree.SubElement(busstop,'point')
        ElementTree.SubElement(point,'x').text = str(feat.geometry().asPoint().x())
        ElementTree.SubElement(point,'y').text = str(feat.geometry().asPoint().y())
        ElementTree.SubElement(point,'z').text = str(0)


    def updateBusstop(self, feature, data):
         #update feature if necessary
        attrs = feature.attributes()
        selectedsegmentId = int(attrs[0])
        oldBusstopId = int(attrs[1])
        if oldBusstopId != data["id"]:
            attrs = {0 : selectedsegmentId, 1: data["id"]}
            self.active_layer.dataProvider().changeAttributeValues({int(feature.id()) : attrs })
        #get info
        roadNetwork = self.document.find('road_network')
        pt_stops = roadNetwork.find('pt_stops')
        busstops = pt_stops.findall('bus_stop')
        selectedBusstop = None
        if busstops is not None:
            for busstop in busstops:
                busstopId = int(busstop.find("id").text)
                if busstopId == oldBusstopId:
                    selectedBusstop = busstop
                    break

        if selectedBusstop is None:
            QgsMessageLog.logMessage("Can not find busstop id %s"%str(oldBusstopId), 'SimGDC')
            return
        selectedBusstop.find("id").text = str(data["id"])
        selectedBusstop.find("segment_id").text = str(data["segment_id"])
        selectedBusstop.find("code").text = str(data["busstopCode"])
        selectedBusstop.find("offset").text = str(data["offset"])
        selectedBusstop.find("name").text = str(data["name"])
        selectedBusstop.find("is_terminal").text = data["isTerminal"]
        selectedBusstop.find("is_bay").text = data["isBay"]   
        selectedBusstop.find("has_shelter").text = data["hasShelter"]   
        selectedBusstop.find("length").text = str(data["length"])

        if data["tags"]:
            selectedBusstop.find("tags").text = str(data["tags"])

    def getBusstop(self, feature):
         #get id from feature
        attrs = feature.attributes()
        selectedSegmentId = int(attrs[0])
        selectedBusstopId = int(attrs[1])       
        #get info
        roadNetwork = self.document.find('road_network')
        pt_stops = roadNetwork.find('pt_stops')
        busstops = pt_stops.findall('bus_stop')
        selectedBusstop = None
        if busstops is not None:
            for busstop in busstops:
                busstopId = int(busstop.find("id").text)
                if busstopId == selectedBusstopId:
                    selectedBusstop = busstop
                    break

        if selectedBusstop is not None:
            info = {}
            info["id"] = selectedBusstop.find("id").text
            info["segment_id"] = selectedBusstop.find("segment_id").text
            info["busstopCode"] = selectedBusstop.find("code").text
            info["offset"] = selectedBusstop.find("offset").text
            info["name"] = selectedBusstop.find("name").text
            info["isTerminal"] = selectedBusstop.find("is_terminal").text
            info["isTerminal"] = info["isTerminal"].strip().lower()
            info["isBay"] = selectedBusstop.find("is_bay").text
            info["isBay"] = info["isBay"].strip().lower()
            info["hasShelter"] = selectedBusstop.find("has_shelter").text
            info["hasShelter"] = info["hasShelter"].strip().lower()
            info["length"] = selectedBusstop.find("length").text
            if selectedBusstop.find("tags"):
                info["tags"] = selectedBusstop.find("tags").text
            else:
                info["tags"] = ""
            return info
        return None

    def addTrainstop(self, point, data):
        '''ADD FEATURE TO LAYER'''
        feat = QgsFeature()
        feat.initAttributes(2)
        feat.setAttribute(0, str(data["segments"]))
        feat.setAttribute(1, data["id"])
        feat.setGeometry(QgsGeometry.fromPoint(QgsPoint(point.x(),point.y())))
        self.active_layer.dataProvider().addFeatures([feat])
        '''ADD TO data.xml '''
         #get info
        roadNetwork = self.document.find('road_network')

        pt_stops = roadNetwork.find('pt_stops')
        if not pt_stops:
            pt_stops = ElementTree.SubElement(roadNetwork,'pt_stops')

        trainstop = ElementTree.SubElement(pt_stops, 'train_stop')
        #add Info
        ElementTree.SubElement(trainstop, 'id').text = str(data["id"])
        segments = ElementTree.SubElement(trainstop, 'segments')
        for segment in data["segments"]:
            ElementTree.SubElement(segments, 'segment_id').text = str(segment)
        ElementTree.SubElement(trainstop, 'platform_name').text = str(data["platform_name"])
        ElementTree.SubElement(trainstop, 'station_name').text = str(data["station_name"])
        ElementTree.SubElement(trainstop, 'type').text = str(data["type"])
        ElementTree.SubElement(trainstop, 'tags').text = str(data["tags"])
        point = ElementTree.SubElement(trainstop,'point')
        ElementTree.SubElement(point,'x').text = str(feat.geometry().asPoint().x())
        ElementTree.SubElement(point,'y').text = str(feat.geometry().asPoint().y())
        ElementTree.SubElement(point,'z').text = str(0)

    def updateTrainstop(self, feature, data):
         #update feature if necessary
        segList = []
        attrs = feature.attributes()
        selectedsegments = str(attrs[0])
        oldTrainstopId = int(attrs[1])
        if oldTrainstopId != data["id"]:
            attrs = {0 : selectedsegments, 1: data["id"]}
            self.active_layer.dataProvider().changeAttributeValues({int(feature.id()) : attrs })
        #get info
        roadNetwork = self.document.find('road_network')
        pt_stops = roadNetwork.find('pt_stops')
        trainstops = pt_stops.findall('train_stop')
        selectedTrainstop = None
        if trainstops is not None:
            for trainstop in trainstops:
                trainstopId = int(trainstop.find("id").text)
                if trainstopId == oldTrainstopId:
                    selectedTrainstop = trainstop
                    break
        if selectedTrainstop is None:
            QgsMessageLog.logMessage("Can not find trainstop id %s"%str(oldTrainstopId), 'SimGDC')
            return
        selectedTrainstop.find("id").text = str(data["id"])
        segments = selectedTrainstop.find("segments")
        for segment in segments.findall('segment_id'):
            segments.remove(segment)

        for segment in data["segments"]:
            ElementTree.SubElement(segments, 'segment_id').text = str(segment)

        selectedTrainstop.find("platform_name").text = str(data["platform_name"])
        selectedTrainstop.find("station_name").text = str(data["station_name"])
        selectedTrainstop.find("type").text = str(data["type"])

        if data["tags"]:
            selectedBusstop.find("tags").text = str(data["tags"])

    def getTrainstop(self, feature):
         #get id from feature
        attrs = feature.attributes()
        selectedSegments = str(attrs[0])
        selectedTrainstopId = int(attrs[1])
        #get info
        roadNetwork = self.document.find('road_network')
        pt_stops = roadNetwork.find('pt_stops')
        trainstops = pt_stops.findall('train_stop')
        selectedTrainstop = None
        if trainstops is not None:
            for trainstop in trainstops:
                trainstopId = int(trainstop.find("id").text)
                if trainstopId == selectedTrainstopId:
                    selectedTrainstop = trainstop
                    break

        if selectedTrainstop is not None:
            info = {}
            info["id"] = selectedTrainstop.find("id").text
            segmentParent = selectedTrainstop.find("segments")
            info["segments"] = []
            for segment in segmentParent.findall("segment_id"):
                info["segments"].append(segment.text)
            info["platform_name"] = selectedTrainstop.find("platform_name").text
            info["station_name"] = selectedTrainstop.find("station_name").text
            info["type"] = selectedTrainstop.find("type").text
            if selectedTrainstop.find("tags"):
                info["tags"] = selectedTrainstop.find("tags").text
            else:
                info["tags"] = ""
            return info
        return None

    def addLane(self, point, data):
        '''ADD FEATURE TO LAYER'''
        feat = QgsFeature()
        feat.initAttributes(2)
        distance = 10
        coordinates = [QgsPoint(point.x(),point.y()), QgsPoint(point.x() + distance,point.y() + distance)]
        feat.setAttribute(0, data["segmentId"])
        feat.setAttribute(1, data["id"])
        feat.setGeometry(QgsGeometry.fromPolyline(coordinates))
        self.active_layer.dataProvider().addFeatures([feat])
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        selectedSegmentId = int(data["segmentId"])
        selectedSegment = None
        if segments is not None:
            for segment in segments:
                segmentId = int(segment.find("id").text)
                if segmentId == selectedSegmentId:
                    selectedSegment = segment
                    break
        if selectedSegment is not None:
            laneParent = selectedSegment.find("lanes")
            if laneParent is None:
                laneParent = ElementTree.SubElement(selectedSegment, 'lanes')
            lane = ElementTree.SubElement(laneParent, 'lane')
            ElementTree.SubElement(lane, 'id').text = str(data["id"])
            ElementTree.SubElement(lane, 'width').text = str(data["width"])
            ElementTree.SubElement(lane, 'vehicle_mode').text = str(data["vehicle_mode"])
            ElementTree.SubElement(lane, 'bus_lane').text = str(data["bus_lane"])
            ElementTree.SubElement(lane, 'can_stop').text = str(data["can_stop"])
            ElementTree.SubElement(lane, 'can_park').text = str(data["can_park"])
            ElementTree.SubElement(lane, 'high_occ_veh').text = str(data["high_occ_veh"])
            ElementTree.SubElement(lane, 'has_road_shoulder').text = str(data["has_road_shoulder"])
            ElementTree.SubElement(lane, 'tags').text = str(data["tags"])

            polyline = ElementTree.SubElement(lane, 'polyline')
            points = ElementTree.SubElement(polyline, 'points')
        i = 0
        for pt in selectedSegment.iter(point):
            clkpoint = ElementTree.SubElement(points, 'point')
            ElementTree.SubElement(clkpoint, 'seq_id').text = i
            ElementTree.SubElement(clkpoint, 'x').text = str(feat.geometry().asPoint().x() + 10*i)
            ElementTree.SubElement(clkpoint, 'y').text = str(feat.geometry().asPoint().y() + 10*i)
            ElementTree.SubElement(clkpoint, 'z').text = str(0)


    def updateLane(self, feature, data):
         #update feature if necessary
        attrs = feature.attributes()
        selectedsegmentId = int(attrs[0])
        oldLaneId = int(attrs[1])
        if oldLaneId != data["id"]:
            attrs = {0 : selectedsegmentId, 1: data["id"]}
            self.active_layer.dataProvider().changeAttributeValues({int(feature.id()) : attrs })
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        selectedLane = None
        if segments is not None:
            for segment in segments:
                segmentId = int(segment.find("id").text)
                if segmentId == selectedsegmentId:
                    laneParent = segment.find("lanes")
                    if laneParent is not None:
                        lanes = laneParent.findall('lane')
                        for lane in lanes:
                            laneId = int(lane.find("id").text)
                            if laneId == oldLaneId:
                                selectedLane = lane
                    break
        if selectedLane is None:
            QgsMessageLog.logMessage("updateLane can not find the lane id %s"%str(oldLaneId), 'SimGDC')
            return
        selectedLane.find("id").text = str(data["id"])
        selectedLane.find("width").text = str(data["width"])
        selectedLane.find("vehicle_mode").text = str(data["vehicle_mode"])
        selectedLane.find("bus_lane").text = str(data["bus_lane"])
        selectedLane.find("can_stop").text = str(data["can_stop"])
        selectedLane.find("can_park").text = str(data["can_park"])
        selectedLane.find("high_occ_veh").text = str(data["high_occ_veh"])
        selectedLane.find("has_road_shoulder").text = str(data["has_road_shoulder"])
        selectedLane.find("tags").text = str(data["tags"])

    def getLane(self, feature):
         #get id from feature
        attrs = feature.attributes()
        selectedSegmentId = int(attrs[0])
        selectedLaneId = int(attrs[1]) 
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        selectedLane = None
        if segments is not None:
            for segment in segments:
                segmentId = int(segment.find("id").text)
                if segmentId == selectedSegmentId:
                    laneParent = segment.find("lanes")
                    if laneParent is not None:
                        lanes = laneParent.findall('lane')
                        for lane in lanes:
                            laneId = int(lane.find("id").text)
                            if laneId == selectedLaneId:
                                selectedLane = lane
                    break
        if selectedLane is not None:
            info = {}
            info["segmentId"] = selectedSegmentId
            info["id"] = selectedLane.find("id").text
            info["width"] = selectedLane.find("width").text 
            info["vehicle_mode"] = int(selectedLane.find("vehicle_mode").text)
            info["bus_lane"] = int(selectedLane.find("bus_lane").text)
            info["can_stop"] = int(selectedLane.find("can_stop").text)
            info["can_park"] = int(selectedLane.find("can_park").text)
            info["high_occ_veh"] = int(selectedLane.find("high_occ_veh").text)
            info["has_road_shoulder"] = int(selectedLane.find("has_road_shoulder").text)

            if selectedLane.find("tags") is not None:
                info["tags"] = selectedLane.find("tags").text

            return info
        return None

    def addLaneEdge(self, point, data):
        '''ADD FEATURE TO LAYER'''
        feat = QgsFeature()
        feat.initAttributes(2)
        distance = 1000
        coordinates = [QgsPoint(point.x(),point.y()), QgsPoint(point.x() + distance,point.y() + distance)]
        feat.setAttribute(0, data["segmentId"])
        feat.setAttribute(1, data["laneNumber"])
        feat.setGeometry(QgsGeometry.fromPolyline(coordinates))
        self.active_layer.dataProvider().addFeatures([feat])
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        selectedSegmentId = int(data["segmentId"])
        selectedSegment = None
        if segments is not None:
            for segment in segments:
                segmentId = int(segment.find("id").text)
                if segmentId == selectedSegmentId:
                    selectedSegment = segment
                    break
        if selectedSegment is not None:
            laneEdgeParent = selectedSegment.find("laneEdgePolylines_cached")
            if laneEdgeParent is None:
                laneEdgeParent = ElementTree.SubElement(selectedSegment, 'laneEdgePolylines_cached')
            laneEdge = ElementTree.SubElement(laneEdgeParent, 'laneEdgePolyline_cached')
            ElementTree.SubElement(laneEdge, 'laneNumber').text = str(data["laneNumber"])

    def updateLaneEdge(self, feature, data):
         #update feature if necessary
        attrs = feature.attributes()
        selectedsegmentId = int(attrs[0])
        oldLaneEdgeNumber = int(attrs[1])
        if oldLaneEdgeNumber != data["laneNumber"]:
            attrs = {0 : selectedsegmentId, 1: data["laneNumber"]}
            self.active_layer.dataProvider().changeAttributeValues({int(feature.id()) : attrs })
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        selectedLaneEdge = None
        if segments is not None:
            for segment in segments:
                segmentId = int(segment.find("id").text)
                if segmentId == selectedsegmentId:
                    laneEdgeParent = segment.find("laneEdgePolylines_cached")
                    if laneEdgeParent is not None:
                        laneEdges = laneEdgeParent.findall('laneEdgePolyline_cached')
                        for laneEdge in laneEdges:
                            laneEdgeNumber = int(laneEdge.find("laneNumber").text)
                            if laneEdgeNumber == oldLaneEdgeNumber:
                                selectedLaneEdge = laneEdge
                    break
        if selectedLaneEdge is None:
            QgsMessageLog.logMessage("updateLaneEdge can not find the lane edge number %s"%str(oldLaneEdgeNumber), 'SimGDC')
            return
        selectedLaneEdge.find("laneNumber").text = str(data["laneNumber"])

    def getLaneEdge(self, feature):
        #get id from feature
        attrs = feature.attributes()
        selectedSegmentId = int(attrs[0])
        selectedLaneEdgeNumber = int(attrs[1])
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        selectedLaneEdge = None
        if segments is not None:
            for segment in segments:
                segmentId = int(segment.find("id").text)
                if segmentId == selectedSegmentId:
                    laneEdgeParent = segment.find("laneEdgePolylines_cached")
                    if laneEdgeParent is not None:
                        laneEdges = laneEdgeParent.findall('laneEdgePolyline_cached')
                        for laneEdge in laneEdges:
                            laneNumber = int(laneEdge.find("laneNumber").text)
                            if laneNumber == selectedLaneEdgeNumber:
                                selectedLaneEdge = laneEdge
                    break
        if selectedLaneEdge is not None:
            info = {}
            info["segmentId"] = selectedSegmentId
            info["laneNumber"] = int(selectedLaneEdge.find("laneNumber").text)
            return info
        return None         

    def generateLaneByNumber(self, feature, nLane, iwidth):
        #find segment
        attrs = feature.attributes()
        selectedLinkId = int(attrs[0])
        selectedSegmentId = int(attrs[1])
        selectedPolyline = feature.geometry().asPolyline()
        listPoints = selectedPolyline

        # gapXTop = (listPoints[1].x() - listPoints[0].x())/nLane
        # gapYTop = (listPoints[1].y() - listPoints[0].y())/nLane
        # gapXBottom = (listPoints[2].x() - listPoints[3].x())/nLane
        # gapYBottom = (listPoints[2].y() - listPoints[3].y())/nLane
        width = 0.1*(iwidth/100)
        # QgsMessageLog.logMessage("test (%s, %s)"%(str(listPoints[0].x()), str(listPoints[0].y())), 'SimGDC')
        #get info
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        links = linkParent.findall('link')
        selectedSegment= None
        if links is not None:
            for link in links:
                linkId = int(link.find("id").text)
                if linkId == selectedLinkId:
                    segments = link.find("segments").findall("segment")
                    for segment in segments:
                        segmentId = int(segment.find("id").text)
                        if segmentId == selectedSegmentId:
                            selectedSegment = segment
        if selectedSegment is None:
            QgsMessageLog.logMessage("selectedSegment not find segment id %s"%str(selectedSegmentId), 'SimGDC')
            return
        laneEdgeLayer = self.getLayer(TYPE.LANEEDGE)
        laneEdges = selectedSegment.find("laneEdgePolylines_cached")
        if laneEdges is not None:
            selectedSegment.remove(laneEdges)
            #delete features from shapefile layer
            delete_lane_edge_feature_ids = []
            for feature in laneEdgeLayer.getFeatures():
                attrs = feature.attributes()
                if attrs[0] == selectedSegmentId:
                    delete_lane_edge_feature_ids.append(feature.id())
            if len(delete_lane_edge_feature_ids) > 0:
                laneEdgeLayer.dataProvider().deleteFeatures(delete_lane_edge_feature_ids)


        #add laneEdge
        # laneEdges = ElementTree.SubElement(selectedSegment, 'laneEdgePolylines_cached')
        # for num in range(0, nLane+1):
        #     laneEdge = ElementTree.SubElement(laneEdges, 'laneEdgePolyline_cached')
        #     ElementTree.SubElement(laneEdge, 'laneNumber').text = str(num)
        #     #add laneEdge shape
        #     feat = QgsFeature()
        #     feat.initAttributes(2)
        #     coordinates = None
        #     if num == (nLane-1)/2 and nLane%2==1:
        #         coordinates = [QgsPoint(listPoints[0]), QgsPoint(listPoints[1])]
        #     elif num < (nLane-1)/2 :
        #         coordinates = [QgsPoint(listPoints[0].x()-(width*i), listPoints[0].y()-(width*i)), QgsPoint(listPoints[1].x()-(width*i), listPoints[1].y()-(width*i))]
        #         i = i-1
        #     elif num > (nLane-1)/2 :
        #         coordinates = [QgsPoint(listPoints[0].x()+(width*j), listPoints[0].y()+(width*j)), QgsPoint(listPoints[1].x()+(width*j), listPoints[1].y()+(width*j))]
        #         j = j-1
        #     feat.setAttribute(0, selectedSegmentId)
        #     feat.setAttribute(1, num)
        #     feat.setGeometry(QgsGeometry.fromPolyline(coordinates))
        #     laneEdgeLayer.dataProvider().addFeatures([feat])


        #remove old lanes
        lanes = selectedSegment.find("lanes")
        laneLayer = self.getLayer(TYPE.LANE)
        if lanes is not None:
            selectedSegment.remove(lanes)
            #delete features from shapefile layer
            delete_lane_feature_ids = []
            for feature in laneLayer.getFeatures():
                attrs = feature.attributes()
                if attrs[0] == selectedSegmentId:
                    delete_lane_feature_ids.append(feature.id())
            if len(delete_lane_feature_ids) > 0:
                laneLayer.dataProvider().deleteFeatures(delete_lane_feature_ids)
        #add lanes
        i = int(nLane/2)
        j = int(nLane/2)
        num_points = len(listPoints)-1
        lanes = ElementTree.SubElement(selectedSegment, 'lanes')

        for num in range(0, nLane):
            lane = ElementTree.SubElement(lanes, 'lane')
            laneId = "%s%s"%(str(selectedSegmentId), str(nLane-num-1))
            ElementTree.SubElement(lane, 'id').text = laneId
            ElementTree.SubElement(lane, 'width').text = "100"
            ElementTree.SubElement(lane, 'vehicle_mode').text = '0010000'
            ElementTree.SubElement(lane, 'bus_lane').text = str(0)
            ElementTree.SubElement(lane, 'can_stop').text = str(0)
            ElementTree.SubElement(lane, 'can_park').text = str(0)
            ElementTree.SubElement(lane, 'high_occ_veh').text = str(0)
            ElementTree.SubElement(lane, 'has_road_shoulder').text = str(0)
            ElementTree.SubElement(lane, 'tags').text = ""
            #add shape
            coordinates = []
            m = []
            del m[:]
            c = []
            del c[:]
            polyline = ElementTree.SubElement(lane, 'polyline')
            points = ElementTree.SubElement(polyline, 'points')



            # coordinates = [QgsPoint(gapXTop/2 + listPoints[0].x() + gapXTop*num, gapYTop/2 + listPoints[0].y() + gapYTop*num), QgsPoint(gapXBottom/2 + listPoints[3].x() + gapXBottom*num, gapYBottom/2 + listPoints[3].y() + gapYBottom*num)]
            for pt in range(num_points):
                listPoints1 = []
                del listPoints1[:]
                listPoints1.append(listPoints[pt])
                listPoints1.append(listPoints[pt+1])
                slope = (listPoints1[1].y()-listPoints1[0].y())/(listPoints1[1].x()-listPoints1[0].x())
                m.append(slope)
                angle = math.atan(slope)
                c.append(listPoints1[0].y()-m[pt]*listPoints1[0].x())

                if num == (nLane-1)/2 and nLane%2==1:
                    coordinates.extend([QgsPoint(listPoints1[0]), QgsPoint(listPoints1[1])])
                elif num == (nLane-1)/2 and nLane%2==0:
                    coordinates.extend([QgsPoint(listPoints1[0].x()-(width*math.sin(angle)*i*pow(-1,pt)), listPoints1[0].y()+(width*math.cos(angle)*i*pow(-1,pt))), QgsPoint(listPoints1[1].x()-(width*math.sin(angle)*i*pow(-1,pt)), listPoints1[1].y()+(width*math.cos(angle)**pow(-1,pt)))])
                elif num < (nLane-1)/2 :
                    coordinates.extend([QgsPoint(listPoints1[0].x()-(width*math.sin(angle)*i*pow(-1,pt)), listPoints1[0].y()+(width*math.cos(angle)*i*pow(-1,pt))), QgsPoint(listPoints1[1].x()-(width*math.sin(angle)*i*pow(-1,pt)), listPoints1[1].y()+(width*math.cos(angle)*i*pow(-1,pt)))])
                elif num > (nLane-1)/2 :
                    coordinates.extend([QgsPoint(listPoints1[0].x()+(width*math.sin(angle)*j*pow(-1,pt)), listPoints1[0].y()-(width*math.cos(angle)*j*pow(-1,pt))), QgsPoint(listPoints1[1].x()+(width*math.sin(angle)*j*pow(-1,pt)), listPoints1[1].y()-(width*math.cos(angle)*j*pow(-1,pt)))])


            if num < (nLane-1)/2 or (num == (nLane-1)/2 and nLane%2==0):
                i = i-1
            elif num > (nLane-1)/2:
                j = j-1
            #
            # if pt == 0:
            #     if num == (nLane-1)/2 and nLane%2==1:
            #         coordinates.extend([QgsPoint(listPoints1[0])])
            #     elif num == (nLane-1)/2 and nLane%2==0:
            #         coordinates.extend([QgsPoint(listPoints1[0].x()-(width*math.sin(angle)*i*pow(-1,pt)), listPoints1[0].y()+(width*math.cos(angle)*i*pow(-1,pt)))])
            #     elif num < (nLane-1)/2 :
            #         coordinates.extend([QgsPoint(listPoints1[0].x()-(width*math.sin(angle)*i*pow(-1,pt)), listPoints1[0].y()+(width*math.cos(angle)*i*pow(-1,pt)))])
            #     elif num > (nLane-1)/2 :
            #         coordinates.extend([QgsPoint(listPoints1[0].x()+(width*math.sin(angle)*j*pow(-1,pt)), listPoints1[0].y()-(width*math.cos(angle)*j*pow(-1,pt)))])
            #
            # elif pt == 1:
            #     if num == (nLane-1)/2 and nLane%2==1:
            #         coordinates.extend([QgsPoint(listPoints1[1])])
            #     elif num == (nLane-1)/2 and nLane%2==0:
            #         coordinates.extend([QgsPoint(listPoints1[1].x()-(width*math.sin(angle)*i*pow(-1,pt)), listPoints1[1].y()+(width*math.cos(angle)**pow(-1,pt)))])
            #     elif num < (nLane-1)/2 :
            #         coordinates.extend([QgsPoint(listPoints1[1].x()-(width*math.sin(angle)*i*pow(-1,pt)), listPoints1[1].y()+(width*math.cos(angle)*i*pow(-1,pt)))])
            #     elif num > (nLane-1)/2 :
            #         coordinates.extend([QgsPoint(listPoints1[1].x()+(width*math.sin(angle)*j*pow(-1,pt)), listPoints1[1].y()-(width*math.cos(angle)*j*pow(-1,pt)))])

            # y1 = (m[0]*c[1] - m[1]*c[0])/(m[0]- m[1])
            # x1 = c[1] - c[0] / m[0] - m[1]
            # coordinates.append(QgsPoint(x1,y1))

            for pts in coordinates:
                clkpoint = ElementTree.SubElement(points, 'point')
                ElementTree.SubElement(clkpoint, 'seq_id').text = str(coordinates.index(pts))
                ElementTree.SubElement(clkpoint, 'x').text = str(pts.x())
                ElementTree.SubElement(clkpoint, 'y').text = str(pts.y())
                ElementTree.SubElement(clkpoint, 'z').text = str(0)

            feat = QgsFeature()
            feat.initAttributes(2)
            feat.setAttribute(0, selectedSegmentId)
            feat.setAttribute(1, int(laneId))
            feat.setGeometry(QgsGeometry.fromPolyline(coordinates))
            laneLayer.dataProvider().addFeatures([feat])

    def delete(self, features):
        if self.active_layer_id == TYPE.NODE:
            self.deleteMulNode(features)
        elif self.active_layer_id == TYPE.LINK:
            self.deleteLink(features)
        elif self.active_layer_id == TYPE.BUSSTOP:
            self.deleteBusStop(features)
        elif self.active_layer_id == TYPE.TRAINSTOP:
            self.deleteTrainStop(features)
        elif self.active_layer_id == TYPE.SEGMENT:
            self.deleteSegment(features)
        elif self.active_layer_id == TYPE.LANE:
            self.deleteLane(features)
        else:
            self.deleteSegmentComponents(features)


    def deleteMulNode(self, features):
        ids = {}
        # delete from shapefile
        attrs=[]
        for feature in features:
            self.active_layer.dataProvider().deleteFeatures([feature.id()])
            attrs = feature.attributes()
            ids[int(attrs[0])] = True
        roadNetwork = self.document.find('road_network')
        nodeParent = roadNetwork.find('nodes')
        for node in nodeParent.findall('node'):
            nodeId = int(node.find('id').text)
            if nodeId==int(attrs[0]):
                nodeParent.remove(node)

    def deleteBusStop(self, features):
        ids = {}
        # delete from shapefile
        attrs=[]
        for feature in features:
            self.active_layer.dataProvider().deleteFeatures([feature.id()])
            attrs = feature.attributes()
            ids[int(attrs[1])] = True
        roadNetwork = self.document.find('road_network')
        pt_stops = roadNetwork.find('pt_stops')
        for busstop in pt_stops.findall('bus_stop'):
            if int(busstop.find('id').text)==int(attrs[1]):
                pt_stops.remove(busstop)

    def deleteTrainStop(self, features):
        ids = {}
        # delete from shapefile
        attrs=[]
        for feature in features:
            self.active_layer.dataProvider().deleteFeatures([feature.id()])
            attrs = feature.attributes()
            ids[int(attrs[1])] = True
        roadNetwork = self.document.find('road_network')
        pt_stops = roadNetwork.find('pt_stops')
        for trainstop in pt_stops.findall('train_stop'):
            if int(trainstop.find('id').text)==int(attrs[1]):
                pt_stops.remove(trainstop)

    def deleteLink(self,features):
        ids = {}
        # delete from shapefile
        attrs=[]
        for feature in features:
            self.active_layer.dataProvider().deleteFeatures([feature.id()])
            attrs = feature.attributes()
            ids[int(attrs[0])] = True
        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        for link in linkParent.findall('link'):
            linkId = int(link.find('id').text)
            if linkId==int(attrs[0]):
                linkParent.remove(link)

    def deleteLane(self, features):
        ids = {}
        # delete from shapefile
        attrs=[]
        for feature in features:
            self.active_layer.dataProvider().deleteFeatures([feature.id()])
            attrs = feature.attributes()
            ids[int(attrs[0])] = True
        roadNetwork = self.document.find('road_network')
        segmentParent = roadNetwork.find('segments')
        for segment in segmentParent.findall('segment'):
            segId = int(segment.find('id').text)
            if segId==int(attrs[0]):
                for lane in segment.findall('lane'):
                    laneID = int(lane.find('id').text)
                    if laneID==int(attrs[1]):
                        segment.remove(lane)

    def deleteSegmentComponents(self, features):                            #for busstop, crossing, laneedge
        ids = {}
        # delete from shapefile
        for feature in features:
            self.active_layer.dataProvider().deleteFeatures([feature.id()])
            attrs = feature.attributes()
            if not ids.has_key(attrs[0]):
                ids[attrs[0]] = {}
            ids[attrs[0]][attrs[1]] = True

        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        segments = linkParent.findall('link/segments/segment')
        for segment in segments:
            segmentId = int(segment.find("id").text)
            if segmentId in ids:
                if self.active_layer_id == TYPE.LANE:
                    laneParent = segment.find("lanes")
                    if laneParent is not None:
                        lanes = laneParent.findall("lane")
                        for lane in lanes:
                            laneId = int(lane.find("id").text)
                            if laneId in ids[segmentId]:
                                laneParent.remove(lane)
                elif self.active_layer_id == TYPE.LANEEDGE:
                    laneEdgeParent = segment.find("laneEdgePolylines_cached")
                    if laneEdgeParent is not None:
                        laneEdges = laneEdgeParent.findall("laneEdgePolyline_cached")
                        for laneEdge in laneEdges:
                            laneEdgeNumber = int(laneEdge.find("laneNumber").text)
                            if laneEdgeNumber in ids[segmentId]:
                                laneEdgeParent.remove(laneEdge)
                elif self.active_layer_id == TYPE.CROSSING:
                    obstacles = segment.find("Obstacles")
                    if obstacles is not None:
                        crossings = obstacles.findall("Crossing")
                        for crossing in crossings:
                            crossing_id = int(crossing.find("id").text)
                            if crossing_id in ids[segmentId]:
                                obstacles.remove(crossing)



    def deleteSegment(self, features):
        ids = {}
        msgBox = QtGui.QMessageBox()
        # delete from shapefile
        for feature in features:
            self.active_layer.dataProvider().deleteFeatures([feature.id()])
            attrs = feature.attributes()
            ids[attrs[1]] = attrs[1]
        # delete inside components
        layers = [self.getLayer(TYPE.LANEEDGE), self.getLayer(TYPE.LANE), self.getLayer(TYPE.CROSSING), self.getLayer(TYPE.BUSSTOP),self.getLayer(TYPE.TRAINSTOP)]
        for layer in layers:
            delete_feature_ids = []
            for feature in layer.getFeatures():
                attrs = feature.attributes()
                if attrs[1] in ids:
                    msgBox.setText("Please delete %s first", layer)
                    msgBox.exec_()
                    return
                    delete_feature_ids.append(feature.id())
            if len(delete_feature_ids) > 0:
                layer.dataProvider().deleteFeatures(delete_feature_ids)

        roadNetwork = self.document.find('road_network')
        linkParent = roadNetwork.find('links')
        if linkParent is not None:
            links = linkParent.findall('link')
            if links is not None:
                for link in links:
                    segmentParent = link.find('segments')
                    if segmentParent is not None:
                        segments = segmentParent.findall('segment')
                        if segments is not None:
                            for segment in segments:
                                segmentId = int(segment.find("id").text)
                                if segmentId in ids:
                                    segmentParent.remove(segment)


    def save(self):
        self.document.write(self.data_path, encoding="utf-8", xml_declaration=True, default_namespace=None, method="xml")